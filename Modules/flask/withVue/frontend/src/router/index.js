import { createRouter, createWebHashHistory } from 'vue-router'
import Get from '../views/Get.vue'
import Send from '../views/Send.vue'

const routes = [
  {
    path: '/GET',
    name: 'GET',
    component: Get
  },
  {
    path: '/SEND',
    name: 'SEND',
    component: Send
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
