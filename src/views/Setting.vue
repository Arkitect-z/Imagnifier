<template>
  <div class="px-12 py-2">
    <h2>放大结果保存位置</h2>
    <div class="mt-4">
      <el-input v-model="saveLocation" placeholder="Please input">
        <template #append>
          <el-button :icon="Edit" @click="saveLocationFolder" />
        </template>
      </el-input>
    </div>
    <h2>模型库</h2>
    <h3>在此处管理本地的模型</h3>
    <p>Waifu2x</p>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card
          shadow="hover"
          :body-style="{ padding: '20px 10px', height: '64px' }"
        >
          <div class="container">
            <div class="modelName w-40">
              <el-scrollbar height="24px">
                <span class="break-normal">{{
                  options.model[0].children[0].label
                }}</span></el-scrollbar
              >
            </div>
            <div class="blank"></div>
            <div class="buttonDownload">
              <el-button
                :icon="Download"
                :disabled="!options.model[0].children[0].disabled"
                circle
                @click="manageModel('download', 'Waifu2x')"
              ></el-button>
            </div>
            <div class="buttonDelete">
              <el-button
                type="danger"
                :icon="Delete"
                style="text-align: right"
                :disabled="options.model[0].children[0].disabled"
                circle
                plain
                @click="manageModel('delete', 'Waifu2x')"
              />
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <p>RealESRGAN</p>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card
          shadow="hover"
          :body-style="{ padding: '20px 10px', height: '64px' }"
        >
          <div class="container">
            <div class="modelName w-40">
              <el-scrollbar height="24px">
                <span class="break-normal">{{
                  options.model[1].children[0].label
                }}</span></el-scrollbar
              >
            </div>
            <div class="blank"></div>
            <div class="buttonDownload">
              <el-button
                :icon="Download"
                :disabled="!options.model[1].children[0].disabled"
                circle
                @click="manageModel('download', 'RealESRGAN_x4plus')"
              ></el-button>
            </div>
            <div class="buttonDelete">
              <el-button
                type="danger"
                :icon="Delete"
                style="text-align: right"
                :disabled="options.model[1].children[0].disabled"
                circle
                plain
                @click="manageModel('delete', 'RealESRGAN_x4plus')"
              />
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card
          shadow="hover"
          :body-style="{ padding: '20px 10px', height: '64px' }"
        >
          <div class="container">
            <div class="modelName w-40">
              <el-scrollbar height="24px">
                <span class="break-normal">{{
                  options.model[1].children[1].label
                }}</span></el-scrollbar
              >
            </div>
            <div class="blank"></div>
            <div class="buttonDownload">
              <el-button
                :icon="Download"
                :disabled="!options.model[1].children[1].disabled"
                circle
                @click="manageModel('download', 'RealESRNet_x4plus')"
              ></el-button>
            </div>
            <div class="buttonDelete">
              <el-button
                type="danger"
                :icon="Delete"
                style="text-align: right"
                :disabled="options.model[1].children[1].disabled"
                circle
                plain
                @click="manageModel('delete', 'RealESRNet_x4plus')"
              />
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card
          shadow="hover"
          :body-style="{ padding: '20px 10px', height: '64px' }"
        >
          <div class="container">
            <div class="modelName w-40">
              <el-scrollbar height="24px">
                <span class="break-normal">{{
                  options.model[1].children[2].label
                }}</span></el-scrollbar
              >
            </div>
            <div class="blank"></div>
            <div class="buttonDownload">
              <el-button
                :icon="Download"
                :disabled="!options.model[1].children[2].disabled"
                circle
                @click="manageModel('download', 'RealESRGAN_x4plus_anime_6B')"
              ></el-button>
            </div>
            <div class="buttonDelete">
              <el-button
                type="danger"
                :icon="Delete"
                style="text-align: right"
                :disabled="options.model[1].children[2].disabled"
                circle
                plain
                @click="manageModel('delete', 'RealESRGAN_x4plus_anime_6B')"
              />
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <p>Bilibili</p>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card
          shadow="hover"
          :body-style="{ padding: '20px 10px', height: '64px' }"
        >
          <div class="container">
            <div class="modelName w-40">
              <el-scrollbar height="24px">
                <span class="break-normal">{{
                  options.model[2].children[0].label
                }}</span></el-scrollbar
              >
            </div>
            <div class="blank"></div>
            <div class="buttonDownload">
              <el-button
                :icon="Download"
                :disabled="!options.model[2].children[0].disabled"
                circle
                @click="manageModel('download', 'Real_CUGAN')"
              ></el-button>
            </div>
            <div class="buttonDelete">
              <el-button
                type="danger"
                :icon="Delete"
                style="text-align: right"
                :disabled="options.model[2].children[0].disabled"
                circle
                plain
                @click="manageModel('delete', 'Real_CUGAN')"
              />
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { Download, Delete, Edit } from "@element-plus/icons-vue";
import { ref } from "vue";
import { ElMessage } from "element-plus";

const saveLocation = ref("");

const downloadProcess = ref("");
const options = ref();
// 获得当前设置
const getState = () => {
  const xhrGetSetting = new XMLHttpRequest();
  const urlGetSetting = "http://127.0.0.1:5000/getSetting";
  xhrGetSetting.onreadystatechange = function () {
    if (xhrGetSetting.readyState == 4 && xhrGetSetting.status == 200) {
      let responseText = JSON.parse(xhrGetSetting.responseText);
      options.value = responseText;
    }
  };
  xhrGetSetting.open("GET", urlGetSetting, false);
  xhrGetSetting.send(null);
  saveLocation.value = options.value.path.downloadUrl;
};

getState();

const saveLocationFolder = () => {
    const xhrSaveLocation = new XMLHttpRequest();
    const urlSaveLocation = "http://127.0.0.1:5000/setSaveLocation";
    xhrSaveLocation.onreadystatechange = function () {
      if (xhrSaveLocation.readyState == 4 && xhrSaveLocation.status == 200) {
        saveLocation.value = xhrSaveLocation.responseText;
      }
    };
    xhrSaveLocation.open("GET", urlSaveLocation, false);
    xhrSaveLocation.send(null);
  };
  
// 下载模型
const manageModel = (manageOperate: String, modelName: String) => {
  let manageState = "no";
  let manageField = new FormData();
  manageField.append("manageOperate", JSON.stringify(manageOperate));
  manageField.append("modelName", JSON.stringify(modelName));
  const xhrSendManageField = new XMLHttpRequest();
  const xhrGetManageResult = new XMLHttpRequest();
  // 设置请求响应的URL，此处为点击"选好了"按钮时的请求
  const urlSendManageField = "http://127.0.0.1:5000/manageField";
  const urlGetManageResult = "http://127.0.0.1:5000/manageResult";
  xhrSendManageField.open("POST", urlSendManageField, false);
  xhrSendManageField.send(manageField);
  xhrGetManageResult.onreadystatechange = function () {
    //服务器返回值的处理函数，此处使用匿名函数进行实现
    if (
      xhrGetManageResult.readyState == 4 &&
      xhrGetManageResult.status == 200
    ) {
      manageState = xhrGetManageResult.responseText;
      console.log(manageState);
    }
  };
  // 设置定时获取进度
  let setIntervalTime: NodeJS.Timeout | null = setInterval(function () {
    xhrGetManageResult.open("GET", urlGetManageResult, false);
    xhrGetManageResult.send(null);
    if ("done" == manageState) {
      clearInterval(Number(setIntervalTime));
      if (manageOperate == "download") {
        ElMessage({
          duration: 2000,
          showClose: true,
          message: modelName + " 下载完成",
          grouping: true,
        });
      } else {
        ElMessage({
          duration: 2000,
          showClose: true,
          message: modelName + " 删除完成",
          grouping: true,
        });
      }
      getState();
    }
  }, 500);
};
</script>

<style scoped>
.dark * {
  color: #ffffff;
}
h2 {
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 2rem;
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
.container {
  display: grid;
  grid-template-columns: 1.3fr 0.4fr 0.4fr 0.4fr;
  grid-template-rows: 1fr;
  gap: 0px 0px;
  grid-auto-flow: column;
  grid-template-areas: "modelName blank buttonDownload buttonDelete";
}

.buttonDownload {
  grid-area: buttonDownload;
}

.buttonDelete {
  grid-area: buttonDelete;
}

.blank {
  grid-area: blank;
}

.modelName {
  grid-area: modelName;
}

.dark .el-card {
  background-color: #4b5563;
}
</style>