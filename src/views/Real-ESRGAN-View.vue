<template>
  <div class="box-content p-12">
    <h1 class="text-gray-900 dark:text-white text-3xl font-bold">
      Real-ESRGAN!!!
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
    <el-button
      type="primary"
      @click="saveImage"
      class="
        bg-blue-600
        hover:bg-blue-500
        dark:bg-blue-900 dark:hover:bg-blue-800
      "
      >选好了</el-button
    >
    <el-progress
      class="my-14 mx-72"
      :text-inside="true"
      :stroke-width="20"
      :percentage="0"
      status="success"
    >
      <span>需要上传图片</span>
    </el-progress>
    <el-scrollbar height="600px" class="mx-32">
      <div v-for="item in fileNum" :key="item">
        <ImgComparisonSlider class="image_compare">
          <figure slot="first" class="before">
            <img
              style="width: 100%"
              src="https://img-comparison-slider.sneas.io/demo/images/before.webp"
            />
            <figcaption>Before</figcaption>
          </figure>
          <figure slot="second" class="after">
            <img
              style="width: 100%"
              src="https://img-comparison-slider.sneas.io/demo/images/after.webp"
            />
            <figcaption>After</figcaption>
          </figure>
        </ImgComparisonSlider>
        <el-divider></el-divider>
      </div>
    </el-scrollbar>
  </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import type { UploadFile } from "element-plus/es/components/upload/src/upload.type";
import { ImgComparisonSlider } from "@img-comparison-slider/vue";

const singleFIleSend = new FormData();
let fileNum = 0;
const uploadImage = (fileParams: any) => {
  singleFIleSend.append("files", fileParams.file);
};
// 上传的文件字典
let uploadFileList: UploadFile[] = [];
const dialogImageUrl = ref("");
const dialogVisible = ref(false);
// 上传成功消息
const uploadSuccessResultMassage = (
  file: UploadFile,
  fileList: UploadFile[]
) => {
  uploadFileList = fileList;
  ElMessage({
    duration: 1500,
    showClose: true,
    message: "上传成功!",
    type: "success",
    grouping: true,
  });
};
// 移除图片
const handleRemove = (file: UploadFile, fileList: UploadFile[]) => {
  uploadFileList = fileList;
  ElMessage({
    duration: 1500,
    showClose: true,
    message: "移除成功!",
    grouping: true,
  });
};
// 文件列表中已上传的文件
const handlePictureCardPreview = (file: UploadFile) => {
  dialogImageUrl.value = file.url!;
  dialogVisible.value = true;
};
const saveImage = () => {
  fileNum = uploadFileList.length;
  console.log(fileNum);
  const readyToSend = new FormData();
  // 重写以简化POST字段
  readyToSend.append("sendData", JSON.stringify(uploadFileList));
  // 初始化XMLHttpRequest对象
  const xhrFileList = new XMLHttpRequest();
  // 设置请求响应的URL
  const url = "http://127.0.0.1:5000/upload";
  xhrFileList.open("POST", url, false);
  xhrFileList.send(singleFIleSend);
  // 发送选定的文件信息
  // 初始化XMLHttpRequest对象
  const xhrChosenFile = new XMLHttpRequest();
  // 设置请求响应的URL
  const urlChosenFile = "http://127.0.0.1:5000/action";
  xhrChosenFile.open("POST", urlChosenFile, false);
  xhrChosenFile.send(readyToSend);

  // 清除缓存
  singleFIleSend.delete("files");
  console.log(uploadFileList);
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
.dark .el-upload-list__item-name {
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
  box-shadow: 0px 0px 15px 3px #929792;
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
</style>