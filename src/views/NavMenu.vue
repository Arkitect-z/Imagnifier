<template>
  <div class="h-screen">
    <el-container
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
          <el-sub-menu index="/ModelSelect" class="dark:hover:bg-gray-500">
            <template #title>
              <div class="dark:text-white">
                <el-icon><Box /></el-icon>
              </div>
              <span>模型列表</span>
            </template>
            <div>
              <el-menu-item-group class="dark:bg-gray-700">
                <template #title><span>可选模型</span></template>
                <el-menu-item
                  index="/Waifu2x"
                  class="dark:text-white dark:hover:bg-gray-500"
                  >Waifu2x</el-menu-item
                >
                <el-menu-item
                  index="/Real-ESRGAN"
                  class="dark:text-white dark:hover:bg-gray-500"
                  >Real-ESRGAN</el-menu-item
                >
              </el-menu-item-group>
            </div>
          </el-sub-menu>
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
        <router-view v-slot="{ Component }">
          <transition name="el-fade-in-linear">
            <component :is="Component" />
          </transition>
        </router-view>
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