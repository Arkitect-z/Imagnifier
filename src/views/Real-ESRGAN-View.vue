<template>
  <div class="box-content p-12">
    <h1 class="text-gray-900 dark:text-white text-3xl font-bold">
      Real-ESRGAN!!!
    </h1>
    <el-scrollbar
      class="my-14 dark:bg-gray-700 mx-18 p-6 shadow-lg rounded-2xl border-opacity-60"
    >
      <el-upload
        multiple
        accept=".jpg,.jpeg,.png,.webp"
        action="http://127.0.0.1:5000/action"
        list-type="picture-card"
        :on-preview="handlePictureCardPreview"
        :on-remove="handleRemove"
        :on-success="uploadSuccessResultMassage"
        :on-error="uploadErrorResultMassage"
      >
        <el-icon><plus /></el-icon>
      </el-upload>
    </el-scrollbar>
    <el-dialog v-model="dialogVisible">
      <el-image width="100%" :src="dialogImageUrl" alt="" />
    </el-dialog>
    <el-button
      type="primary"
      @click="saveImage(fileList)"
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
     <p v-for="item in 20" :key="item" class="scrollbar-demo-item">{{ item }}</p>
  </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import type { UploadFile } from "element-plus/es/components/upload/src/upload.type";

const dialogImageUrl = ref("");
const dialogVisible = ref(false);
// 移除图片
const handleRemove = (file: UploadFile, fileList: UploadFile[]) => {
  console.log(file, fileList);
};
// 文件列表中已上传的文件
const handlePictureCardPreview = (file: UploadFile) => {
  dialogImageUrl.value = file.url!;
  dialogVisible.value = true;
};
// 文件上传时消息
const uploadProgress = (file: UploadFile, fileList: UploadFile[]) => {
  console.log(file.url);
};
// 上传成功消息
const uploadSuccessResultMassage = (
  response: any,
  file: UploadFile,
  fileList: UploadFile[]
) => {
  ElMessage({
    duration:1200,
    showClose: true,
    message: "上传成功!",
    type: "success",
  });
  console.log(fileList);
};
// 上传失败消息
const uploadErrorResultMassage = (
  err: any,
  file: UploadFile,
  fileList: UploadFile[]
) => {
  ElMessage({
    duration:1200,
    showClose: true,
    message: "上传失败!",
    type: "error",
  });
};
const saveImage = (fileList: UploadFile[]) => {
  // 初始化XMLHttpRequest对象
		const xhr = new XMLHttpRequest();
		// 设置请求响应的URL
		const url = "http://127.0.0.1:5000/upload";
    xhr.open("POST", url, false);
    xhr.send(""+fileList);
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
</style>