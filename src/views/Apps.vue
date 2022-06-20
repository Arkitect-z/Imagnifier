<template>
  <div class="box-content px-12 h-screen" :style="bgImage">
    <div class="container">
      <div class="b-game-card ">
        <!-- 初始图片 -->
        <div class="b-game-card__cover" @click="changeBack()">
          <div class="mt-4 text-black p-2">原图片</div>
          <div class="mt-2 p-2 text-black break-all">图片初始分辨率</div>
          </div>
      </div>
      <!-- 图片放大的原图 -->
      <div class="b-game-card">
        <div class="b-game-card__cover" @click="changeBackOrigin()">
          <div class="mt-4 text-black p-2">放大前图片</div>
          <div class="p-2 text-black break-all">对图片进行模糊化处理</div>
        </div>
      </div>
      <div class="b-game-card">
        <div class="b-game-card__cover" @click="changeBackWaifu2x()">
          <div class="mt-4 text-black p-2">Waifu2x</div>
          <div class="mt-6 text-black break-all">推荐指数</div>
          <div class="text-black break-all">★★✰✰✰</div>
        </div>
      </div>
      <div class="b-game-card">
        <div class="b-game-card__cover" @click="changeBackRealESRGAN1()">
          <div class="mt-4 text-black break-all p-2">RealESRGAN_x4plus</div>
          <div class="text-black break-all">推荐指数</div>
          <div class="text-black break-all">★★★★✰</div>
        </div>
      </div>
      <div class="b-game-card">
        <div class="b-game-card__cover" @click="changeBackRealESRGAN2()">
          <div class="mt-4 text-black break-all p-2">RealESRNet_x4plus</div>
          <div class="text-black break-all">推荐指数</div>
          <div class="text-black break-all">★★★✰✰</div>
        </div>
      </div>
      <div class="b-game-card">
        <div class="b-game-card__cover" @click="changeBackRealESRGAN3()">
          <div class="mt-4 text-black break-all p-2">RealESRGAN_x4plus_anime_6B</div>
          <div class="mt-2 text-black break-all">推荐指数</div>
          <div class="text-black break-all">★★★★★</div>
        </div>
      </div>
      <div class="b-game-card">
        <div class="b-game-card__cover" @click="changeBackSelf()">
          <div class="mt-4 text-black p-2">SelfTrained</div>
          <div class="mt-6 text-black break-all">推荐指数</div>
          <div class="text-black break-all">★★★✰✰</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const bgImage = ref("background-image: url(src/assets/dlam.jpg); background-repeat:no-repeat; background-size: cover;")

const changeBack = () => {
  bgImage.value = "background-image: url(src/assets/dlam.jpg); background-repeat:no-repeat; background-size: cover;"
};
const changeBackOrigin = () => {
  bgImage.value = "background-image: url(src/assets/dlamOri.jpg); background-repeat:no-repeat; background-size: cover;"
};
const changeBackWaifu2x = () => {
  bgImage.value = "background-image: url(src/assets/dlamWaifu2x.png); background-repeat:no-repeat; background-size: cover;"
};
const changeBackRealESRGAN1 = () => {
  bgImage.value = "background-image: url(src/assets/dlamRealESRGAN1.png); background-repeat:no-repeat; background-size: cover;"
};
const changeBackRealESRGAN2 = () => {
  bgImage.value = "background-image: url(src/assets/dlamRealESRGAN2.png); background-repeat:no-repeat; background-size: cover;"
};
const changeBackRealESRGAN3 = () => {
  bgImage.value = "background-image: url(src/assets/dlamRealESRGAN3.png); background-repeat:no-repeat; background-size: cover;"
};
const changeBackSelf = () => {
  bgImage.value = "background-image: url(src/assets/dlamSelf.png); background-repeat:no-repeat; background-size: cover;"
};
</script>


<style lang="scss" scoped>
// Settings
$c_0: #000000;
$c_1: #353540;
// Basic reset
.el-scrollbar__view{
  height: 1000px !important;
}
.container {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-gap: 30px;
  padding: 30px;

  @media screen {
    grid-template-columns: repeat(7, 1fr);
    max-width: 100%;
  }
}
.b-game-card {
  position: relative;
  z-index: 1;
  width: 100%;
  padding-bottom: 150%;
  perspective: 1000px;

  &__cover {
    position: absolute;
    z-index: 1;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-image: linear-gradient(120deg, #ffffff 0%, #ffffff 100%);
    background-size: cover;
    perspective-origin: 50% 50%;
    transform-style: preserve-3d;
    transform-origin: top center;
    will-change: transform;
    transform: skewX(0.001deg);
    transition: transform 0.35s ease-in-out;

    // Gloss

    &::after {
      display: block;
      content: "";
      position: absolute;
      z-index: 100;
      top: 0;
      left: 0;
      width: 100%;
      height: 120%;
      background: linear-gradient(
        226deg,
        rgba(255, 255, 255, 0.4) 0%,
        rgba(255, 255, 255, 0.4) 35%,
        rgba(255, 255, 255, 0.2) 42%,
        rgba(255, 255, 255, 0) 60%
      );
      transform: translateY(-20%);
      will-change: transform;
      transition: transform 0.65s cubic-bezier(0.18, 0.9, 0.58, 1);
    }
  }

  &:hover &__cover {
    transform: rotateX(7deg) translateY(-6px);
    &::after {
      transform: translateY(0%);
    }
  }

  // Shadows

  &::before {
    display: block;
    content: "";
    position: absolute;
    top: 5%;
    left: 5%;
    width: 90%;
    height: 90%;
    background: rgba($c_0, 0.5);
    box-shadow: 0 6px 12px 12px rgba($c_0, 0.4);
    will-change: opacity;
    transform-origin: top center;
    transform: skewX(0.001deg);
    transition: transform 0.35s ease-in-out, opacity 0.5s ease-in-out;
  }

  &:hover::before {
    opacity: 0.6;
    transform: rotateX(7deg) translateY(-6px) scale(1.05);
  }
}
</style>