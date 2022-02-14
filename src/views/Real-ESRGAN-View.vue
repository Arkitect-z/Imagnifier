<template>
  <div class="box-content p-10">
    <h1 class="text-gray-900 dark:text-white text-3xl font-bold">
      Real-ESRGAN!!!
    </h1>
    <el-upload
      class="my-14 mx-72"
      multiple
      action="https://jsonplaceholder.typicode.com/posts/"
      list-type="picture-card"
      :on-preview="handlePictureCardPreview"
      :on-remove="handleRemove"
    >
      <el-icon><plus /></el-icon>
    </el-upload>
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
  </div>
</template>
<script lang="ts" setup>
import { ref, reactive } from "vue";
import { ElMessage } from "element-plus";
import { Plus, UploadFilled } from "@element-plus/icons-vue";
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
  ElMessage.error("上传失败!");
  ElMessage({
    message: "上传成功!",
    type: "success",
    appendTo: "el-main el-upload",
  });
  console.log(err);
};
// 覆盖上传图片默认的 xhr 行为
const getUrl = (fileList: UploadFile[]) => {
  console.log(fileList);
};
const saveImage = () => {};
// 模型标签页
const activeName = ref("first");
// 标签页点击监听
const handleClick = (tab: string, event: Event) => {
  console.log(tab, event);
};
// 表单内容
const form = reactive({
  name: "",
  region: "",
  date1: "",
  date2: "",
  delivery: false,
  type: [],
  resource: "",
  desc: "",
});
// 提交表单
const onSubmit = () => {
  console.log("submit!");
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