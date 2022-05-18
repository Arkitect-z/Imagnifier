<template>
  <div class="h-screen">
    <el-container
      style="height: 100%"
      class="bg-white dark:bg-gray-800 transition duration-300 ease-linear"
    >
      <el-aside>
        <el-menu
          router
          default-active="/Guidance"
          class="
            h-screen
            py-10
            dark:bg-gray-700 dark:border-gray-700
            transition
            duration-300
            ease-linear
          "
          :collapse="true"
        >
          <el-menu-item index="/Guidance" class="dark:hover:bg-gray-500">
            <div class="dark:text-white">
              <el-icon><Location /></el-icon>
            </div>
            <template #title>导览</template>
          </el-menu-item>
          <el-menu-item index="/Apps" class="dark:hover:bg-gray-500">
            <div class="dark:text-white">
              <el-icon><IconMenu /></el-icon>
            </div>
            <template #title>模型介绍</template>
          </el-menu-item>
          <el-menu-item index="/Magnifier" class="dark:hover:bg-gray-500">
            <div class="dark:text-white">
              <el-icon><Box /></el-icon>
            </div>
            <template #title>
              <span>工作台</span>
            </template>
          </el-menu-item>
          <el-menu-item index="/Setting" class="dark:hover:bg-gray-500">
            <div class="dark:text-white">
              <el-icon><Setting /></el-icon>
            </div>
            <template #title>设置</template>
          </el-menu-item>
          <el-switch
            v-model="switchValtue"
            class="mt-2"
            inline-prompt
            :active-icon="Moon"
            :inactive-icon="Sunny"
            @click="darkMode"
          >
          </el-switch>
        </el-menu>
      </el-aside>
      <el-main class="shadow-inner dark:shadow-inner">
        <transition name="el-fade-in-linear">
          <keep-alive>
            <el-scrollbar height="100%">
              <router-view />
            </el-scrollbar>
          </keep-alive>
        </transition>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import {
  Location,
  Box,
  Menu as IconMenu,
  Setting,
  Sunny,
  Moon,
} from "@element-plus/icons-vue";

// 禁用右键与文字选中
document.body.onselectstart = document.body.oncontextmenu = function () {
  return false;
};

const switchValtue = ref(false);

const darkMode = () => {
  const clsList = document.documentElement.classList;
  if (!clsList.contains("dark")) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
};
</script>

<style>
.el-main {
  --el-main-padding: 0px;
}
.el-aside {
  --el-aside-width: auto;
}
.dark .el-menu {
  --tw-bg-opacity: 1;
  --el-menu-bg-color: rgb(55 65 81 / var(--tw-bg-opacity));
}
.dark .el-popper.is-light {
  border: 0px;
  --tw-bg-opacity: 1;
  background: rgb(55 65 81 / var(--tw-bg-opacity));
}
.dark .el-sub-menu__title:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(107, 114, 128, var(--tw-bg-opacity));
}
</style>