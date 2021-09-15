import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/*',
    component: 'NotFound'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
