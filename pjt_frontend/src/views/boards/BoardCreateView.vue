<template>
    <div>
      boardcreateView
      <div>
        <form @submit.prevent="submitData">
          <label for="title">제목</label>
          <input type="text" id="title" v-model="title">
          <label for="content">내용</label>
          <input type="text" id="content" v-model="content">

          <button @submit.prevent="submitData">생성</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue'
    import { useBoardsStore } from '@/stores/boards.js'

    const store = useBoardsStore()

    const title = ref('')
    const content = ref('')

    const submitData = function () {
      const article = {
        title : title.value,
        content : content.value,
      }

      store.createArticle(article)
      title.value = ''
      content.value = ''
    }
  </script>
  
  <style scoped>
  
  </style>