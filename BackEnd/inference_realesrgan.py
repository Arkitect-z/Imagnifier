import cv2
import glob
import os
from basicsr.archs.rrdbnet_arch import RRDBNet

from realesrgan import RealESRGANer
from realesrgan.archs.srvgg_arch import SRVGGNetCompact

# 传入字典：
#     input_path:输入图像路径（JPG / PNG / WEPP）或目录
#     output_path:输出图像路径（JPG / PNG / WEPP）或目录
# parser = {
#     'input_file_path': '',
#     'output_file_path': '',
#     'model_name': '',
#     'face_enhance': False,
#     'half': True,
#     'extension': 'auto'
# }


# 准备模型功能
def prepare_model(parser):
    args = parser
    # determine models according to model names
    # 根据模型名来决定选用模型
    args['model_name'] = args['model_name'].split('.')[0]
    if args['model_name'] in ['RealESRGAN_x4plus', 'RealESRNet_x4plus']:  # x4 RRDBNet model
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
        netscale = 4
    elif args['model_name'] in ['RealESRGAN_x4plus_anime_6B']:  # x4 RRDBNet model with 6 blocks
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=6, num_grow_ch=32, scale=4)
        netscale = 4
    elif args['model_name'] in ['RealESRGAN_x2plus']:  # x2 RRDBNet model
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)
        netscale = 2
    elif args['model_name'] in [
        'RealESRGANv2-anime-xsx2', 'RealESRGANv2-animevideo-xsx2-nousm', 'RealESRGANv2-animevideo-xsx2'
    ]:  # x2 VGG-style model (XS size)
        model = SRVGGNetCompact(num_in_ch=3, num_out_ch=3, num_feat=64, num_conv=16, upscale=2, act_type='prelu')
        netscale = 2
    elif args['model_name'] in [
        'RealESRGANv2-anime-xsx4', 'RealESRGANv2-animevideo-xsx4-nousm', 'RealESRGANv2-animevideo-xsx4'
    ]:  # x4 VGG-style model (XS size)
        model = SRVGGNetCompact(num_in_ch=3, num_out_ch=3, num_feat=64, num_conv=16, upscale=4, act_type='prelu')
        netscale = 4

    # determine model paths  os.getcwd() + 
    model_path = os.path.join('D:\PythonProjects\Imagnifier\python\experiments/pretrained_models', args['model_name'] + '.pth')
    if not os.path.isfile(model_path):
        model_path = os.path.join('D:\PythonProjects\Imagnifier\python/realesrgan/weights', args['model_name'] + '.pth')
    if not os.path.isfile(model_path):
        raise ValueError(f"Model {args['model_name']} does not exist.")

    # restorer
    upsampler = RealESRGANer(
        scale=netscale,
        model_path=model_path,
        model=model,
        # Tile size, 0 for no tile during testing
        tile=0,
        # Tile padding
        tile_pad=10,
        # Pre padding size at each border
        pre_pad=0,
        half=args['half'])

    if args['face_enhance']:  # Use GFPGAN for face enhancement
        from gfpgan import GFPGANer
        face_enhancer = GFPGANer(
            model_path='D:\PythonProjects\Imagnifier\python/experiments/face_enhancer/GFPGANCleanv1-NoCE-C2.pth',
            upscale=4,
            arch='clean',
            channel_multiplier=2,
            bg_upsampler=upsampler)
    os.makedirs(args['output_file_path'], exist_ok=True)

    if os.path.isfile(args['input_file_path']):
        paths = [args['input_file_path']]
    else:
        paths = sorted(glob.glob(os.path.join(args['input_file_path'], '*')))

    for idx, path in enumerate(paths):
        imgname, extension = os.path.splitext(os.path.basename(path))
        print('Testing', idx, imgname)

        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if len(img.shape) == 3 and img.shape[2] == 4:
            img_mode = 'RGBA'
        else:
            img_mode = None

        try:
            if args['face_enhance']:
                _, _, output = face_enhancer.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
            else:
                output, _ = upsampler.enhance(img, outscale=4)
        except RuntimeError as error:
            print('Error', error)
            print('If you encounter CUDA out of memory, try to set --tile with a smaller number.')
        else:
            if args['extension'] == 'auto':
                extension = extension[1:]
            else:
                extension = args["extension"]
            if img_mode == 'RGBA':  # RGBA images should be saved in png format
                extension = 'png'
            # Suffix of the restored image
            # f"{imgname}_{'out'}.{extension}"
            save_path = os.path.join(args['output_file_path'], f"{imgname}.{extension}")
            cv2.imwrite(save_path, output)
    print(imgname + " done!")

