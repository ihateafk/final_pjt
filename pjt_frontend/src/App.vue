<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useDepositStore } from './stores/deposit';
import { useUserStore } from './stores/user';
import axios from 'axios';

const userStore = useUserStore()
const router = useRouter()

const logout = function () {
  axios({
    method: 'post',
    url: `${userStore.URL}/accounts/logout/`,
  })
    .then((res) => {
      userStore.token = null
      console.log('LOGOUT SUCCESS')
      router.push({ name: 'home' })
    })
    .catch((err) => {
      console.log('LOGOUT FAILED')
      console.log(err.response.data)
    })
}
</script>

<template>
  <header>
    <div>
      <nav>
        <div id="logo">
          <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
        </div>
        <div>
          <RouterLink :to="{ name: 'deposit'}">예금 비교</RouterLink> |
          <RouterLink :to="{ name: 'exchange'}">환율 계산기</RouterLink> |
          <RouterLink :to="{ name: 'map'}">은행 지도</RouterLink> |
          <RouterLink :to="{ name: 'board'}">게시판</RouterLink> |
          <div id="islogout" v-if="userStore.token === null">
            <RouterLink :to="{ name: 'login'}">로그인</RouterLink> |
            <RouterLink :to="{ name: 'signup' }">회원 가입</RouterLink>
          </div>
          <div id="islogin" v-if="userStore.token !== null">
            상품추천링크
            <div id="myprofile">
              <div id="profile">
                <RouterLink :to="{ name: 'profile'}">MyPage</RouterLink>
              </div>
              <div id="logout">
                <button @click="logout">Logout</button>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
