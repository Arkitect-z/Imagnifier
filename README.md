<img style="align:center" width="160" alt="logo" src="https://user-images.githubusercontent.com/53122135/158972105-8c9f8d81-76ea-4064-8970-b6e58128b1bc.png">

## <div align="center"><b><a href="README.md">English</a> | <a href="README_CN.md">简体中文</a></b></div>

# Imagnifier
> 一个集成 Vue 3 + Vite 2 + Vue-Router 4 + Vuex 4 + TailWindCss + TypeScript + ESLint 等框架与组件的动漫图片放大器的应用实现
> <br/>后端采用Flask作为服务框架，PyQt作为前后端的承载，使用[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)预训练的模型进行图片清晰化操作
> <br/>下一步计划：缩小应用体积，改为单页应用，增加页面自适应效果

## 技术栈

- 构建工具：[Vite 2.x](https://cn.vitejs.dev/)
- 前端框架：[Vue 3.x](https://v3.cn.vuejs.org/)
- 编程语言：[TypeScript 4.x](https://www.typescriptlang.org/zh/) + [JavaScript](https://www.javascript.com/)
- 路由工具：[Vue Router 4.x](https://next.router.vuejs.org/zh/index.html)
- 状态管理：[Vuex 4.x](https://next.vuex.vuejs.org/)
- UI 框架：[Element Plus](https://element-plus.org/#/zh-CN)
- CSS 组件：[TailWindCss](https://www.tailwindcss.cn/) / [Sass](https://sass.bootcss.com/documentation)
- 代码规范：[ESLint](https://eslint.org/)

- 服务与通信框架：[Flask](https://github.com/pallets/flask/)
- 界面框架：[PyQt5](https://github.com/PyQt5/PyQt/)
- 神经网络框架：[PyTorch](https://github.com/pytorch/pytorch/)
- 使用模型来源：[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)   [bilibili](https://github.com/bilibili/ailab)    [waifu2x-chainer](https://github.com/tsurumeso/waifu2x-chainer)

## 演示视频

图片选择与查看

https://user-images.githubusercontent.com/53122135/174570743-8fa41e49-e309-4ece-a2d0-7319f8956ecb.mp4

图片处理与对比结果

https://user-images.githubusercontent.com/53122135/174571635-cba8f875-3d3f-4f66-b3d8-1f0163a52dc1.mp4


## 项目启动步骤

```bash
npm install
```
将[Real-ESRGAN模型库](https://github.com/xinntao/Real-ESRGAN/blob/master/docs/model_zoo.md)下载的模型放入"\BackEnd\experiments\pretrained_models"目录下
接下来：
### 编译以用于可热更新的开发环境

```bash
npm run dev
```

### 编译以用于生产环境

```bash
npm run build
```
## 致谢
感谢[element-plus-vite-starter](https://github.com/element-plus/element-plus-vite-starter)帮我从0开始学习构建Vue项目
<br/>感谢[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)为我提供图像超分辨率的各种技术支持
