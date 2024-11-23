<template>
  <div>
    board
    <div v-if="isLogin">
      <button @click="router.push({name: 'boardcreate'})">글 추가</button>
    </div>
    <BoardList/>
  </div>
</template>

<script setup>
  import BoardList from '@/components/boards/BoardList.vue'
  import { useRouter } from 'vue-router'
  import { useUserStore } from '@/stores/user.js'
  import { ref } from 'vue'

  const userStore = useUserStore()

  const isLogin = ref(userStore.token)

  const router = useRouter()

</script>

<style scoped>

</style>