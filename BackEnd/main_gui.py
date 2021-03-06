# 导入常用组件
import shutil
import sys
import os
import threading
import json

# 导入QT
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView

# 导入flask
from flask import Flask, make_response, request
from flask_cors import CORS

# 导入放大器
import inference_realesrgan as realesrgan
import experiments.waifu2x_chainer.waifu2x as waifu2x

# 导入下载组件
import wget

# 设置任务栏图标
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

UPLOAD_FOLDER = os.getcwd() + '/BackEnd/cache/image'
MAGNIFIED_FOLDER = os.getcwd() + '/BackEnd/cache/result/'
CONFIG_FILE = os.getcwd() + "/BackEnd/setting.config.json"
MODEL_FOLDER = os.getcwd() + "/BackEnd/models"

# 模型链接
url_RealESRGAN_x4plus = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"
url_RealESRNet_x4plus = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.1/RealESRNet_x4plus.pth"
url_RealESRGAN_x4plus_anime_6B = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth"

# 打开后端端口
flask_app = Flask(__name__)

# 支持跨域访问
CORS(flask_app, supports_credentials=True)

# 用于接收上传文件数据,button事件


@flask_app.route('/action', methods=['POST'])
def chosen_file():
    # 放大功能进度条的数值
    global magnify_percentage
    # 预防NameError
    pic_data = request.form["sendData"]
    form_data = request.form["form"]
    print(json.loads(form_data))
    if pic_data:
        if not os.path.exists(MAGNIFIED_FOLDER):
            os.makedirs(MAGNIFIED_FOLDER)
        # 前端传来待处理文件列表
        file_list = json.loads(pic_data).get("_value")
        # 文件列表长度
        file_list_length = len(file_list)
        # 每处理完一个文件，进度条前进数量
        each_percentage = 80.0 / file_list_length
        for each_file in file_list:
            file_name = os.path.join(UPLOAD_FOLDER, each_file.get("name"))
            # 设置多线程，防止与主界面相互干扰
            magnifier = threading.Thread(
                target=image_magnifier, args=(file_name, each_percentage, json.loads(form_data), ))
            # 设置守护线程，使端口随系统关闭
            magnifier.setDaemon(True)
            # 启动线程
            magnifier.start()
    return "For Get Chosen File!"


# 用于接收上传文件数据,upload事件
@flask_app.route('/upload', methods=['POST'])
def upload_file():
    global magnify_percentage
    magnify_percentage = 20
    # 预防NameError
    files = request.files.getlist("files")
    if files:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        for each_file in files:
            each_file.save(os.path.join(UPLOAD_FOLDER, each_file.filename))
    return "For Upload!"

# 下载功能
@flask_app.route('/manageField', methods=['POST'])
def manage_model():
    global setting_data
    global manage_state
    manage_state = False
    manageOperate = request.form["manageOperate"]
    modelName = request.form["modelName"]
    if manageOperate == '"download"':
        if modelName == '"Waifu2x"':
            setting_data["model"][0]["children"][0]["disabled"] = False
        elif modelName == '"RealESRGAN_x4plus"':
            setting_data["model"][1]["children"][0]["disabled"] = False
        elif modelName == '"RealESRNet_x4plus"':
            setting_data["model"][1]["children"][1]["disabled"] = False
        elif modelName == '"RealESRGAN_x4plus_anime_6B"':
            setting_data["model"][1]["children"][2]["disabled"] = False
        elif modelName == '"Real_CUGAN"':
            setting_data["model"][2]["children"][0]["disabled"] = False
    else:
        if modelName == '"Waifu2x"':
            setting_data["model"][0]["children"][0]["disabled"] = True
        elif modelName == '"RealESRGAN_x4plus"':
            setting_data["model"][1]["children"][0]["disabled"] = True
        elif modelName == '"RealESRNet_x4plus"':
            setting_data["model"][1]["children"][1]["disabled"] = True
        elif modelName == '"RealESRGAN_x4plus_anime_6B"':
            setting_data["model"][1]["children"][2]["disabled"] = True
        elif modelName == '"Real_CUGAN"':
            setting_data["model"][2]["children"][0]["disabled"] = True
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(setting_data, f)
    manage_state = True
    return "For Download!"

# 返回下载结果
@flask_app.route('/manageResult', methods=['GET'])
def manage_result():
    global manage_state
    if manage_state:
        return "done"
    else:
        return "no"

# 前端获取后端处理状态
@flask_app.route('/state', methods=['GET'])
def get_percentage():
    global magnify_percentage
    # 防止进度条溢出
    if magnify_percentage > 99:
        magnify_percentage = 100
    return str(int(magnify_percentage))


# 获取配置信息
@flask_app.route('/getSetting', methods=['GET'])
def get_setting():
    global setting_data
    return setting_data


# 保存处理结果
@flask_app.route('/saveResult', methods=['POST'])
def save_result():
    global setting_data
    source_url = MAGNIFIED_FOLDER + request.form["imageName"]
    target_url = setting_data["path"]["downloadUrl"] + \
        request.form["imageName"]
    try:
        shutil.copyfile(source_url, target_url)
        return "成功保存到" + target_url
    except IOError as e:
        return "保存失败,缺少写入权限 %s" % e
    except:
        return "保存遇到未知错误", sys.exc_info()


# 设置-保存文件位置
@flask_app.route('/setSaveLocation', methods=['GET'])
def set_save_location():
    global setting_data
    save_loaction = QFileDialog.getExistingDirectory(
        None, "选取文件夹", setting_data["path"]["downloadUrl"])
    setting_data["path"]["downloadUrl"] = save_loaction + "/"
    setting_data["path"]["pathRevised"] = True
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(setting_data, f)
    return str(setting_data["path"]["downloadUrl"])


# flask活动的多线程
def vue_thread():
    global setting_data
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        setting_data = json.load(f)
        if not setting_data["path"]["pathRevised"]:
            setting_data["path"]["downloadUrl"] = os.getcwd() + "/download/"
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(setting_data, f)
    os.system("npm run dev")


def flask_thread():
    flask_app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)


# 清理cache的多线程
def clear_cache_thread():
    # 上传文件夹
    cache_file_path = UPLOAD_FOLDER
    # 处理结果文件夹
    cache_result_path = MAGNIFIED_FOLDER
    if os.path.exists(cache_file_path):
        shutil.rmtree(cache_file_path)
    if os.path.exists(cache_result_path):
        shutil.rmtree(cache_result_path)


def image_magnifier(file_name, each_percentage, form_data):
    global magnify_percentage
    parser = {
        'input_file_path': file_name,
        'output_file_path': MAGNIFIED_FOLDER,
        'model_name': form_data["model_name"][-1],
        "outscale": form_data["sliderValue"],
        'face_enhance': form_data["face_enhance"],
        'half': True,
        'extension': form_data["out_ext"]
    }
    if form_data["model_name"][-1] == "Waifu2x":
        waifu2x.prepare_model(parser)
    else:
        realesrgan.prepare_model(parser)
    magnify_percentage += each_percentage
    print(magnify_percentage)


class MainWindow(QMainWindow):

    def __init__(self):
        # 对继承自父类的属性进行初始化
        super(MainWindow, self).__init__()
        # 用父类的初始化方法来初始化继承的属性
        self.browser = QWebEngineView()
        self.initUI()

    def initUI(self):
        # 将窗口设置为动图大小
        self.resize(1680, 1050)
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.4)
        # 获取相对路径
        url = "http://localhost:3000/"
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

        # 添加窗口标题
        self.setWindowTitle("图片智能放大App")
        self.setWindowIcon(QIcon(os.getcwd() + "/BackEnd/logo.ico"))
        # icon = QIcon().addPixmap(QPixmap(os.getcwd() + "/BackEnd/logo.ico"), QIcon.Normal, QIcon.Off)
        # self.setWindowIcon(icon)


if __name__ == '__main__':
    start_vue = threading.Thread(target=vue_thread)
    start_vue.setDaemon(True)
    start_vue.start()
    app = QApplication(sys.argv)
    # 创建一个主窗口
    mainWin = MainWindow()
    # mainWin.setMinimumSize(1680, 1050)
    # 显示
    mainWin.show()
    # 在线程中清除缓存
    clear_cache = threading.Thread(target=clear_cache_thread)
    clear_cache.start()
    # 设置多线程，防止与主界面相互干扰
    upload_thread = threading.Thread(target=flask_thread)
    # 设置守护线程，使端口随系统关闭
    upload_thread.setDaemon(True)
    # 启动线程
    upload_thread.start()
    # 主循环
    sys.exit(app.exec_())
