<template>
  <div class="p-12">
    <h2>模型库</h2>
    <h3>在此处管理本地的模型</h3>
    <p>Waifu2x</p>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="hover" class="model" :body-style="{ padding: '20px 10px' }">
          <span class="modelName">{{options[0].label}}</span>
          <div style="float: right;">
          <el-button :icon="Download" circle></el-button>
          <el-button type="danger" :icon="Delete" :disabled="options[0].disabled" circle  plain/>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <p>RealESRGAN</p>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="hover" class="model" :body-style="{ padding: '20px 10px' }">
          <span class="modelName break-normal">{{options[1].children[0].label}}</span>
          <div style="float: right;">
          <el-button :icon="Download" circle></el-button>
          <el-button type="danger" :icon="Delete" style="text-align: right;" :disabled="options[1].children[0].disabled" circle  plain/>
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="model" :body-style="{ padding: '20px 10px' }">
          <span class="modelName break-normal">{{options[1].children[1].label}}</span>
          <div style="float: right;">
          <el-button :icon="Download" circle></el-button>
          <el-button type="danger" :icon="Delete" style="text-align: right;" :disabled="options[1].children[1].disabled" circle  plain/>
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="model" :body-style="{ padding: '20px 10px' }">
          <span class="modelName break-normal">{{options[1].children[2].label}}</span>
          <div style="float: right;">
          <el-button :icon="Download" circle></el-button>
          <el-button type="danger" :icon="Delete" style="text-align: right;" :disabled="options[1].children[2].disabled" circle  plain/>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { Download, Delete } from "@element-plus/icons-vue";
import { ref } from "vue";

const downloadProcess = ref("");
const options = ref([]);
// 获得当前设置
const xhrGetSetting = new XMLHttpRequest();
const urlGetSetting = "http://127.0.0.1:5000/getSetting";
xhrGetSetting.onreadystatechange = function () {
  if (xhrGetSetting.readyState == 4 && xhrGetSetting.status == 200) {
    let responseText = JSON.parse(xhrGetSetting.responseText);
    options.value = responseText.model;
  }
};
xhrGetSetting.open("GET", urlGetSetting, false);
xhrGetSetting.send(null);
</script>

<style scoped>
.dark * {
  color: #ffffff;
}
h2 {
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 1rem;
  padding-bottom: 0.75rem;
  line-height: 1.25;
  font-size: 1.65rem;
}
h3 {
  display: flex;
  align-items: center;
  position: relative;
  margin-bottom: 0.6rem;
}
p {
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 1rem;
  margin-bottom: 0.6rem;
}
.model {
  width: 100%;
  display: block;
}
.modelName{
  align-items: center;
  text-align: left;
}
.dark .model {
  background-color: #4b5563;
}
</style>