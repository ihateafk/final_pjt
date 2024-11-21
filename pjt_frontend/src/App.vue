<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
        <RouterLink :to="{ name: 'deposit'}">예금 비교</RouterLink> |
        <RouterLink :to="{ name: 'exchange'}">환율 계산기</RouterLink> |
        <RouterLink :to="{ name: 'map'}">은행 지도</RouterLink> |
        <RouterLink :to="{ name: 'board'}">게시판</RouterLink> |
        <RouterLink :to="{ name: 'login'}">로그인</RouterLink> |
        <RouterLink :to="{ name: 'signup' }">회원 가입</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
