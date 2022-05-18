<template>
  <div class="box-content p-12">
    <h1 class="text-gray-900 dark:text-white text-3xl font-bold">
      Magnifier!!!
    </h1>
    <el-scrollbar
      class="
        my-14
        dark:bg-gray-700
        mx-18
        p-6
        shadow-lg
        rounded-2xl
        border-opacity-60
      "
    >
      <el-upload
        multiple
        accept=".jpg,.jpeg,.png,.webp"
        :http-request="uploadImage"
        action="#"
        list-type="picture-card"
        :on-change="uploadSuccessResultMassage"
        :on-preview="handlePictureCardPreview"
        :on-remove="handleRemove"
      >
        <el-icon><plus /></el-icon>
      </el-upload>
    </el-scrollbar>
    <el-dialog v-model="dialogVisible">
      <el-image width="100%" :src="dialogImageUrl" alt="" />
    </el-dialog>
    <div
      style="margin-left: 10vw; margin-right: 10vw"
      class="text-gray-900 dark:text-white"
    >
      <el-form :model="form" label-width="180px" label-position="left">
        <el-form-item label="选用模型" class="text-gray-900 dark:text-white">
          <el-cascader
            v-model="form.model_name"
            :options="options"
            :props="{ expandTrigger: 'hover' }"
            @change="handleChange"
            :show-all-levels="false"
            placeholder="还未装载任何模型"
          />
        </el-form-item>
        <el-form-item label="放大品质 (默认4)">
          <el-slider
            v-model="form.sliderValue"
            :min="1"
            :max="4"
            show-input
            class="hidden-sm-and-down"
          />
          <el-input-number
            v-model="form.sliderValue"
            :min="1"
            :max="10"
            class="hidden-md-and-up"
          />
        </el-form-item>
        <el-form-item label="启用面部增强 (默认否)">
          <el-switch v-model="form.face_enhance" />
        </el-form-item>
        <el-form-item label="输出图片格式">
          <el-radio-group v-model="form.out_ext">
            <el-radio-button label="png" />
            <el-radio-button label="jpg" />
            <el-radio-button label="webp" />
          </el-radio-group>
        </el-form-item>
      </el-form>
    </div>
    <el-button
      type="primary"
      @click="saveImage"
      :loading="isLoading"
      class="
        mt-6
        bg-blue-500
        hover:bg-blue-400
        dark:bg-blue-900 dark:hover:bg-blue-800
      "
      >选好了</el-button
    >
    <el-progress
      style="margin-left: 20vw; margin-right: 20vw"
      class="mt-10 hidden-sm-and-down"
      :text-inside="true"
      :stroke-width="20"
      :percentage="percentage"
      status="success"
    >
      <span class="text-gray-900">{{ percentageText }}</span>
    </el-progress>
    <br />
    <el-progress
      type="circle"
      :percentage="percentage"
      class="my-14 hidden-md-and-up"
    />

    <el-divider></el-divider>
    <el-scrollbar height="600px">
      <el-row justify="center">
        <el-col
          v-for="(eachImage, index) in uploadFileListForShow"
          :key="eachImage"
          :span="6"
          class="grid gap-4"
        >
          <el-card
            shadow="hover"
            class="m-2 bg-white dark:bg-gray-800"
            style="width: 210px; height: 380px"
          >
            <div class="image-contain">
              <img :src="eachImage['url']" class="image" />
            </div>
            <div
              class="w-full grid grid-flow-row auto-rows-max place-self-center"
            >
              <div class="mt-6 text-black dark:text-white">
                <el-scrollbar max-height="24px">
                  <span style="width: 168px; word-break: break-all">{{
                    eachImage["name"]
                  }}</span>
                </el-scrollbar>
              </div>
              <div>
                <el-button
                  type="primary"
                  @click="showResult(eachImage.name)"
                  style="width: 50%"
                  class="
                    my-6
                    bg-blue-500
                    hover:bg-blue-400
                    dark:bg-blue-900 dark:hover:bg-blue-800
                  "
                  >查看对比</el-button
                >
              </div>
              <div>
                <el-button
                  type="primary"
                  @click="saveResult(eachImage.name)"
                  style="width: 50%"
                  class="
                    mb-4
                    text-white
                    hover:text-white
                    bg-blue-500
                    hover:bg-blue-400
                    dark:bg-blue-900 dark:hover:bg-blue-800
                  "
                  >保存本地</el-button
                >
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <el-dialog v-model="dialogVisibleResult">
        <el-scrollbar height="400px" style="max-heigt: 400px">
          <ImgComparisonSlider class="image_compare m-6 self-stretch">
            <figure slot="first" class="before">
              <img style="width: 100%" :src="beforeImageUrl" />
              <figcaption>Before</figcaption>
            </figure>
            <figure slot="second" class="after">
              <img style="width: 100%" :src="afterImageUrl" />
              <figcaption>After</figcaption>
            </figure>
          </ImgComparisonSlider>
        </el-scrollbar>
      </el-dialog>
    </el-scrollbar>
  </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import type { UploadFile } from "element-plus/es/components/upload/src/upload.type";
import { ImgComparisonSlider } from "@img-comparison-slider/vue";
import { reactive } from "vue";
import "element-plus/theme-chalk/display.css";

const cacheImageUrl = ref("/BackEnd/cache/result/");
const downloadUrl = ref("/download/");
const options = ref([]);
// 获得当前设置
const xhrGetSetting = new XMLHttpRequest();
const urlGetSetting = "http://127.0.0.1:5000/getSetting";
xhrGetSetting.onreadystatechange = function () {
  if (xhrGetSetting.readyState == 4 && xhrGetSetting.status == 200) {
    let responseText = JSON.parse(xhrGetSetting.responseText);
    options.value = responseText.model;
    cacheImageUrl.value = responseText.path.cacheImageUrl;
    downloadUrl.value = responseText.path.downloadUrl;
  }
};
xhrGetSetting.open("GET", urlGetSetting, false);
xhrGetSetting.send(null);
// 按钮加载中
const isLoading = ref(false);
// 进度条值
const percentage = ref(0);
const percentageText = ref("需要上传图片");
// 文件存储
const singleFIleSend = new FormData();
const uploadImage = (fileParams: any) => {
  singleFIleSend.append("files", fileParams.file);
};
// 上传的文件字典
const uploadFileList = ref([] as UploadFile[]);
let uploadFileListForList = [] as UploadFile[];
let uploadFileListForShow = ref([] as UploadFile[]);
// 图片预览显示
const dialogImageUrl = ref("");
const dialogVisible = ref(false);
// 图片结果显示
const beforeImageUrl = ref("");
const afterImageUrl = ref("");
const isButtonClicked = ref(false);
const dialogVisibleResult = ref(false);
// 表单
const form = reactive({
  // 图片品质滑块值
  model_name: ["RealESRGAN", "RealESRGAN_x4plus"],
  sliderValue: 4,
  face_enhance: false,
  out_ext: "png",
});
const handleChange = () => {
  console.log(form);
};
// 上传成功消息
const uploadSuccessResultMassage = (
  file: UploadFile,
  fileList: UploadFile[]
) => {
  uploadFileList.value = fileList;
  ElMessage({
    duration: 1500,
    showClose: true,
    message: "上传成功!",
    type: "success",
    grouping: true,
  });
  percentage.value = 10;
  percentageText.value = "图片选择完成";
};
// 移除图片
const handleRemove = (file: UploadFile, fileList: UploadFile[]) => {
  uploadFileList.value = fileList;
  ElMessage({
    duration: 1500,
    showClose: true,
    message: "移除成功!",
    grouping: true,
  });
  // 当图片删除干净时，进度条重置为0
  if (fileList.length == 0) {
    percentage.value = 0;
    percentageText.value = "需要上传图片";
  }
};
// 文件列表中已上传的文件
const handlePictureCardPreview = (file: UploadFile) => {
  dialogImageUrl.value = file.url!;
  dialogVisible.value = true;
};
// 点击"选好了"按钮事件
const saveImage = () => {
  if (uploadFileList.value.length != 0) {
    isLoading.value = true;
    isButtonClicked.value = true;
    isLoading.value = true;
    let readyToSend = new FormData();
    // 添加需要的POST字段
    readyToSend.append("sendData", JSON.stringify(uploadFileList));
    readyToSend.append("form", JSON.stringify(form));
    // 初始化XMLHttpRequest对象
    const xhrFileList = new XMLHttpRequest();
    // 设置请求响应的URL，此处为图片选择时的请求
    const url = "http://127.0.0.1:5000/upload";
    xhrFileList.open("POST", url, false);
    xhrFileList.send(singleFIleSend);
    // 发送选定的文件信息
    // 初始化XMLHttpRequest对象
    const xhrChosenFile = new XMLHttpRequest();
    // 设置请求响应的URL，此处为点击"选好了"按钮时的请求
    const urlChosenFile = "http://127.0.0.1:5000/action";
    xhrChosenFile.open("POST", urlChosenFile, true);
    // 绑定响应状态事件监听函数
    xhrChosenFile.onreadystatechange = function () {
      if (xhrChosenFile.readyState == 4) {
        // 监听HTTP状态码
        if (xhrChosenFile.status == 200 || xhrChosenFile.status == 0) {
          // 接收数据
          percentage.value = 20;
          percentageText.value = "上传完成，正在处理";
        }
      }
    };
    xhrChosenFile.send(readyToSend);
    // 清除缓存
    singleFIleSend.delete("files");
    // 获得图片处理进度
    getStateFromBackend();
  } else {
    ElMessage({
      duration: 1500,
      showClose: true,
      message: "还没有选择任何图片!",
      grouping: true,
    });
  }
};

// 进度条进度
const getStateFromBackend = () => {
  let responseText = "20";
  // 初始化XMLHttpRequest对象
  const xhrGetState = new XMLHttpRequest();
  // 设置请求响应的URL，此处为点击"选好了"按钮时的请求
  const urlGetState = "http://127.0.0.1:5000/state";
  xhrGetState.onreadystatechange = function () {
    //服务器返回值的处理函数，此处使用匿名函数进行实现
    if (xhrGetState.readyState == 4 && xhrGetState.status == 200) {
      responseText = xhrGetState.responseText;
      percentage.value = parseInt(responseText);
    }
  };
  // 设置定时获取进度
  let setIntervalTime: NodeJS.Timeout | null = setInterval(function () {
    xhrGetState.open("GET", urlGetState, false);
    xhrGetState.send(null);
    if (parseInt(responseText) == 100) {
      clearInterval(Number(setIntervalTime));
      percentageText.value = "处理完成，请下滑查看结果";
      // 显示结果
      uploadFileListForList = uploadFileList.value;
      uploadFileListForShow.value = uploadFileListForList;
      // 按钮置为可用状态
      isLoading.value = false;
    }
  }, 500);
};

// 处理结果展示
const showResult = (imageName: string) => {
  beforeImageUrl.value = "../../BackEnd/cache/image/" + imageName;
  afterImageUrl.value = "../../BackEnd/cache/result/" + imageName.split(".")[0] + "." + form.out_ext;
  dialogVisibleResult.value = true;
};

// 保存处理结果
const saveResult = (imageName: string) => {
  let readyToSend = new FormData();
  readyToSend.append("imageName", imageName.split(".")[0] + "." + form.out_ext);
  const xhrSaveResult = new XMLHttpRequest();
  const urlSaveResult = "http://127.0.0.1:5000/saveResult";
  xhrSaveResult.onreadystatechange = function () {
    if (xhrSaveResult.readyState == 4 && xhrSaveResult.status == 200) {
      let saveResultReturn = xhrSaveResult.responseText;
      ElMessage({
        duration: 3000,
        showClose: true,
        message: saveResultReturn,
        grouping: true,
      });
    }
  };
  xhrSaveResult.open("POST", urlSaveResult, true);
  xhrSaveResult.send(readyToSend);
};
</script>
<style>
.dark .el-upload {
  --tw-bg-opacity: 1;
  background-color: rgb(107 114 128 / var(--tw-bg-opacity));
}
.dark .el-upload-dragger .el-upload__text em {
  color: #93c5fd;
}
.dark .el-upload-list--picture .el-upload-list__item {
  background-color: #4b5563;
}
.dark .el-upload-list__item-name,
.dark .el-form-item__label {
  color: #ffffff;
}
.dark .el-upload-list__item .el-icon--close {
  color: #ffffff;
}
.image_compare {
  transition: box-shadow 200ms ease-in-out;
  border-radius: 15px;
}
.image_compare:focus {
  outline: none;
  box-shadow: 0px 0px 10px 2px #929792;
}
.before,
.after {
  margin: 0;
}
.before figcaption,
.after figcaption {
  background: #fff;
  border: 1px solid #c0c0c0;
  border-radius: 12px;
  color: #2e3452;
  opacity: 0.8;
  padding: 12px;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  line-height: 100%;
}
.before figcaption {
  left: 12px;
}
.after figcaption {
  right: 12px;
}
.image-contain {
  width: 168px;
  height: 168px;
}
.image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}
.dark .el-dialog {
  --tw-bg-opacity: 1;
  --el-dialog-bg-color: rgb(55 65 81 / var(--tw-bg-opacity));
}
.el-radio-button__inner {
  padding: 8px 22px;
}
.dark .el-radio-button__inner {
  --tw-bg-opacity: 1;
  background: rgb(55 65 81 / var(--tw-bg-opacity));
  color: white;
  border: 1px solid #042b4d;
}
.dark .el-radio-button:first-child .el-radio-button__inner {
  border-left: 1px solid #042b4d;
}
.dark .el-input__inner {
  --tw-bg-opacity: 1;
  background-color: rgb(55 65 81 / var(--tw-bg-opacity));
  border: rgb(55 65 81 / var(--tw-bg-opacity));
  color: white;
}
</style>