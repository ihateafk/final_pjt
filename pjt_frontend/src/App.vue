<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView, useRouter } from 'vue-router';
import { useDepositStore } from './stores/deposit';
import { useUserStore } from './stores/user';
import axios from 'axios';

const userStore = useUserStore();
const router = useRouter();

const activeLink = ref('');

const setActiveLink = (link) => {
  activeLink.value = link;
};

const removeActiveLink = () => {
  activeLink.value = '';
};

const logout = function () {
  axios({
    method: 'post',
    url: `${userStore.URL}/accounts/logout/`,
  })
    .then((res) => {
      userStore.token = null;
      console.log('LOGOUT SUCCESS');
      router.push({ name: 'home' });
    })
    .catch((err) => {
      console.log('LOGOUT FAILED');
      console.log(err.response.data);
    });
};
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <RouterLink class="navbar-brand" :to="{ name: 'home' }">Home</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'deposit'}" @mouseover="setActiveLink('deposit')" @mouseleave="removeActiveLink">예금 비교</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'exchange'}" @mouseover="setActiveLink('exchange')" @mouseleave="removeActiveLink">환율 계산기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'map'}" @mouseover="setActiveLink('map')" @mouseleave="removeActiveLink">은행 지도</RouterLink>
            </li>
            <li class="nav-item" v-if="userStore.token !== null">
              <RouterLink class="nav-link" :to="{ name: 'board'}" @mouseover="setActiveLink('board')" @mouseleave="removeActiveLink">게시판</RouterLink>
            </li>
          </ul>
          <ul class="navbar-nav" v-if="userStore.token === null">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'login'}">로그인</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'signup' }">회원 가입</RouterLink>
            </li>
          </ul>
          <ul class="navbar-nav" v-if="userStore.token !== null">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                더 보기
              </a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li>
                  <RouterLink class="dropdown-item" :to="{ name: 'profile'}">MyPage</RouterLink>
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="logout">Logout</a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
  .nav-item {
    border-radius: 7px;
  }

  .nav-link {
    transition: background-color 0.3s;
    border-radius: 7px;
  }

  .nav-link:hover,
  .nav-link.active {
    background-color: blue;
    color: white;
  }

  .nav-link.router-link-active {
    background-color: blue;
    color: white;
  }
</style>
