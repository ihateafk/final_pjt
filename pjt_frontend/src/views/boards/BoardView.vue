<template>
  <div class="container">
    <div class="board-header">
      <h1 class="title">게시판</h1>
      <div v-if="isLogin" class="add-button-container">
        <button class="add-button" @click="router.push({ name: 'boardcreate' })">
          글 추가
        </button>
      </div>
    </div>
    <BoardList />
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
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.board-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.title {
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
}

.add-button-container {
  text-align: right;
}

.add-button {
  padding: 8px 16px;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.add-button:hover {
  background-color: #2980b9;
}
</style>