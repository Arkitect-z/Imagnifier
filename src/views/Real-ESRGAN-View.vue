<template>
  <div>
    <h1 class="text-gray-900 dark:text-white text-3xl font-bold">
      Real-ESRGAN!!!
    </h1>
    <el-upload
      drag
      class="mx-52"
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
          Drop file here or <em class="dark:text-white">click to upload</em>
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
</style>