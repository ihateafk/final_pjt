import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DepositView from '@/views/deposit/DepositView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'
import BoardView from '@/views/BoardView.vue'
import DepositDetailView from '@/views/deposit/DepositDetailView.vue'
import SavingsDetailView from '@/views/savings/SavingsDetailView.vue'
import { useUserStore } from '@/stores/user'

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
      component: () => import('@/components/accounts/SignUpPage.vue'),

      beforeEnter: (to, from, next) => {
        const userStore = useUserStore()

        if (userStore.token !== null) {
          alert('이미 로그인 되어 있습니다.')
          next({ name: 'home' })
        }
        else {
          next()
        }
      }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/components/accounts/LoginPage.vue'),

      beforeEnter: (to, from, next) => {
        const userStore = useUserStore()

        if (userStore.token !== null) {
          alert('이미 로그인 되어 있습니다.')
          next(from)
        }
        else {
          next()
        }
      }
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
      path: '/savings/:id',
      name: 'savingsDetail',
      component: SavingsDetailView
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
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/profile/ProfileView.vue'),
      children: [
        { path: 'main', name: 'profilemain', component: () => import('@/components/profile/ProfileMain.vue') },
        { path: 'favorate', name: 'favorate', component: () => import('@/components/profile/ProfileFavorate.vue') },
        { path: 'subscribe', name: 'subscribe', component: () => import('@/components/profile/ProfileSubscribe.vue') },
        {
          path: 'person',
          name: 'person',
          component: () => import('@/components/profile/ProfilePerson.vue'),
          children: [
            {
              path: 'change',
              name: 'infochange',
              component: () => import('@/components/profile/ProfilePersonInfoChange.vue'),
              children: [
                {
                  path: 'pw',
                  name: 'pwchange',
                  component: () => import('@/components/profile/ProfilePwChange.vue')
                },
              ]
            },
          ]
        },
      ],

      beforeEnter: (to, from, next) => {
        const userStore = useUserStore()

        if (userStore.token !== null) {
          next()
        } else {
          alert('로그인이 필요합니다.')
          next({ name: 'login' })
        }
      }
    }
  ],
})

export default router
