// user.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

// user.js
export const useUserStore = defineStore('user', () => {
  const URL = ref('http://127.0.0.1:8000')
  const token = ref(null)
  const userId = ref(null)
  const userdata = ref(null)
  const router = useRouter()

  const getUserInfo = function() {
    if (token.value) {
      return axios({
        method: 'get',
        url: `${URL.value}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then((res) => {
        userId.value = res.data.pk
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }

  const login = function (payload) {
    axios({
      method: 'post',
      url: `${URL.value}/accounts/login/`,
      data: {
        username: payload.username,
        password: payload.password
      }
    })
    .then((res) => {
      token.value = res.data.token
      return getUserInfo()
    })
    .then(() => {
      router.push({ name: 'board' })
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logout = function () {
    token.value = null
    userId.value = null
  }

  return {
    URL,
    token,
    userId,
    userdata,
    login,
    logout,
    getUserInfo
  }
}, {persist: true})