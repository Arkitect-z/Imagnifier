import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import NavMenu from '../views/NavMenu.vue'
import NonePage from '../views/404.vue'
import Guidance from '../views/Guidance.vue'
import Apps from '../views/Apps.vue'

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