import { createRouter, createWebHistory } from 'vue-router'
import UserLogin from '../views/Admin/UserLogin.vue'
import CreateService from '@/views/Admin/CreateService.vue'
import DashBoard from '@/views/Admin/DashBoard.vue'
import AdminSummary from '@/views/Admin/AdminSummary.vue'
import ServicePage from '@/views/Admin/ServicePage.vue'
import ProfessionalRequest from '@/views/Admin/ProfessionalRequest.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'UserLogin',
      component: UserLogin
    },
    {
      path:'/create-service',
      name:'CreateService',
      component: CreateService
    },
    {
      path:'/dashboard/admin',
      name:'Dashboard',
      component: DashBoard
    },
    {
      path:'/dashboard/summary',
      name:'Summary',
      component:AdminSummary
    },
    {
      path:'/admin/services',
      name:'Services',
      component:ServicePage
    },
    {
      path:'/admin/professional_request',
      name:'ProfessionalRequest',
      component:ProfessionalRequest
    }
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

export default router
