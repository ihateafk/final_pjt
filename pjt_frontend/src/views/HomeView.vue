<template>
  <div id="background">
    <div id="body" @click="$router.push({ name: 'recommend' })">
      <div id="logo"><h1>HomePage Logo</h1></div>
      <div id="search">
        <div id="searchbox">
          <input type="text" :value="textvalue" disabled>
        </div>
        <div id="routerbtn">
          <button id="logobtn"><img src="/search_logo_x64.png" alt="search logo"></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import { onBeforeMount, ref } from 'vue';

const userStore = useUserStore()

const textvalue = userStore.token !== null ? 'AI 상담사에게 물어보기' : '로그인하고 즉시 상담'
</script>

<style lang="css" scoped>
#background {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70vh;
  margin: 0;
}

#search {
  display: flex;
  justify-content: center;
  align-items: center;
}

#logobtn {
  background: none;
  border: none;
}

input[type="text"] {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1.5rem;
  text-align: center;
}
</style>