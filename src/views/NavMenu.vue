<template>
  <div>
    <el-container class="bg-white dark:bg-slate-900">
      <el-aside>
        <el-menu
          router
          default-active="/Guidance"
          class="el-menu-vertical"
          :collapse="true"
        >
          <el-menu-item index="/Guidance">
            <el-icon><Location /></el-icon>
            <template #title>导览</template>
          </el-menu-item>
          <el-menu-item index="/Apps">
            <el-icon><IconMenu /></el-icon>
            <template #title>模型介绍</template>
          </el-menu-item>
          <el-sub-menu index="/ModelSelect">
            <template #title>
              <el-icon><Box /></el-icon>
              <span>模型列表</span>
            </template>
            <el-menu-item-group>
              <template #title><span>可选模型</span></template>
              <el-menu-item index="1-1">Model one</el-menu-item>
              <el-menu-item index="1-2">Model two</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
          <el-menu-item index="/Setting">
            <el-icon><Setting /></el-icon>
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
      <el-main>
        <transition name="el-fade-in-linear">
          <router-view />
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
</style>