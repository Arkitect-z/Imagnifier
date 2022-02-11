import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import NavMenu from '../views/NavMenu.vue'
import NonePage from '../views/404.vue'
import Guidance from '../views/Guidance.vue'
import Apps from '../views/Apps.vue'
import Setting from '../views/Setting.vue'
import Waifu2x from '../views/Waifu2x-View.vue'
import RealESRGAN from '../views/Real-ESRGAN-View.vue'

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: NavMenu,
        redirect: '/Guidance',
        children: [
            {
                path: '/Guidance',
                component: Guidance,
            },
            {
                path: '/Apps',
                component: Apps,
            },
            {
                path: '/Setting',
                component: Setting,
            },
            {
                path: '/Waifu2x',
                component: Waifu2x,
            },
            {
                path: '/Real-ESRGAN',
                component: RealESRGAN,
            },
            {
                path: '/:pathMatch(.*)*',
                name: '404',
                component: NonePage,
            }
        ]
    },
    
]


const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router