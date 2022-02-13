<template>
  <div class="box-content p-10">
    <h1 class="text-gray-900 dark:text-white text-3xl font-bold">
      Real-ESRGAN!!!
    </h1>
    <el-upload
      drag
      class="my-14 mx-72"
      multiple
      action="#"
      :http-request="getUrl"
      :on-remove="handleRemove"
      :on-success="SuccessResultMassage"
      :on-error="ErrorResultMassage"
      :file-list="fileList"
      list-type="picture"
    >
      <div class="dark:bg-gray-500">
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text dark:text-white">
          拖动文件到此 或 <em>点击来上传</em>
        </div>
      </div>
    </el-upload>
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
  </div>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";
import { UploadFilled } from "@element-plus/icons-vue";
import type { UploadFile } from "element-plus/es/components/upload/src/upload.type";

let fileList = ref([]);
const handleRemove = (file: UploadFile, fileList: UploadFile[]) => {
  console.log(file, fileList);
};
const handlePreview = (file: UploadFile) => {
  console.log(file);
};
const SuccessResultMassage = () => {
  ElMessage({
    message: "上传成功!",
    type: "success",
  });
};
const ErrorResultMassage = () => {
  ElMessage.error("上传失败!");
};
const getUrl = (fileList: UploadFile[]) => {
  console.log(fileList);
};
const saveImage = (fileList: UploadFile[]) => {
  for (let eachIamge in fileList) {
    console.log(eachIamge);
  }
};
</script>

<style>
.dark .el-upload-dragger {
  --tw-bg-opacity: 1;
  background-color: rgb(107 114 128 / var(--tw-bg-opacity));
}
.dark .el-upload-dragger .el-upload__text em {
  color: #93c5fd;
}
.dark .el-upload-list--picture .el-upload-list__item {
  background-color: #4B5563;
}
.dark .el-upload-list__item-name {
  color: #ffffff;
}
.dark .el-upload-list__item .el-icon--close {
  color: #ffffff;
}
</style>