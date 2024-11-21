import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DepositView from '@/views/deposit/DepositView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'
import BoardView from '@/views/BoardView.vue'
import LoginPage from '@/components/LoginPage.vue'
import DepositDetailView from '@/views/deposit/DepositDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/components/SignUpPage.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/deposit/:id',
      name: 'depositDetail',
      component: DepositDetailView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView
    },
  ],
})

export default router
