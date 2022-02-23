import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
import './styles/index.scss'
// 消息样式
import 'element-plus/theme-chalk/src/message.scss'
// 消息角标
import 'element-plus/theme-chalk/el-badge.css'

const app = createApp(App)
// app.use(ElementPlus);
app.use(router).mount("#app")
