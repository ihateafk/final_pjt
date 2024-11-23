<template>
  <div>
    board
    <button @click="router.push({name: 'boardcreate'})">글 추가</button>
    <BoardList/>
  </div>
</template>

<script setup>
  import BoardList from '@/components/boards/BoardList.vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()

</script>

<style scoped>

</style>