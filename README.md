<div align="center"><img width="160" alt="logo" src="https://user-images.githubusercontent.com/53122135/158972105-8c9f8d81-76ea-4064-8970-b6e58128b1bc.png"></div>

## <div align="center"><b><a href="README.md">English</a> | <a href="README_CN.md">简体中文</a></b></div>

# Imagnifier
> An implementation of an anime image amplifier application that integrates Vue 3 + Vite 2 + Vue-Router 4 + Vuex 4 + TailWindCss + TypeScript + ESLint and other frameworks and components.
> <br/>The backend adopts Flask as the service framework and PyQt as the front-end and back-end host, and uses pre-trained models from [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) for image clarification operations
> <br/>Next plans: reduce the size of the app to a single page app, add page adaptive effects

## Tech stack

- Build tool: [Vite 2.x](https://cn.vitejs.dev/)
- Front-end framework: [Vue 3.x](https://v3.cn.vuejs.org/)
- Programming Languages: [TypeScript 4.x](https://www.typescriptlang.org/zh/) + [JavaScript](https://www.javascript.com/)
- Routing Tools: [Vue Router 4.x](https://next.router.vuejs.org/zh/index.html)
- State Management: [Vuex 4.x](https://next.vuex.vuejs.org/)
- UI framework: [Element Plus](https://element-plus.org/#/zh-CN)
- CSS Components: [TailWindCss](https://www.tailwindcss.cn/) / [Sass](https://sass.bootcss.com/documentation)
- Code Specifications: [ESLint](https://eslint.org/)

- Service and Communication Framework: [Flask](https://github.com/pallets/flask/)
- Interface framework: [PyQt5](https://github.com/PyQt5/PyQt/)
- Neural network framework: [PyTorch](https://github.com/pytorch/pytorch/)
- Using model sources: [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) [bilibili](https://github.com/bilibili/ailab) [waifu2x-chainer](https. //github.com/tsurumeso/waifu2x-chainer)

## Demo

Image Selection and Viewing

https://user-images.githubusercontent.com/53122135/174570743-8fa41e49-e309-4ece-a2d0-7319f8956ecb.mp4

Image Processing and Results Comparison

https://user-images.githubusercontent.com/53122135/174571635-cba8f875-3d3f-4f66-b3d8-1f0163a52dc1.mp4


## Build

```bash
npm install
```
Put the models downloaded from [Real-ESRGAN Model Library](https://github.com/xinntao/Real-ESRGAN/blob/master/docs/model_zoo.md) into the "\BackEnd\experiments\pretrained_models" directory. 

```bash
npm run dev
```

```bash
npm run build
```
## Acknowledgement
Thanks to[element-plus-vite-starter](https://github.com/element-plus/element-plus-vite-starter) Help me learn how to build Vue projects from scratch
<br/>Thanks to[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
