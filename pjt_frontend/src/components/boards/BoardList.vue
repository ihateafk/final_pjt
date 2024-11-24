<template>
    <div class="container">
      <div v-if="!store.articles" class="no-articles">
        <p>작성된 글이 없습니다.</p>
      </div>
      <div v-else class="board-list">
        <div
          v-for="article in store.articles"
          :key="article.pk"
          class="board-item"
        >
          <BoardListItem :article="article" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { onMounted } from 'vue'
    import { useBoardsStore } from '@/stores/boards'
    import BoardListItem from '@/components/boards/BoardListItem.vue'
  
    const store = useBoardsStore()
  
    onMounted(() => {
      store.getArticles()
    })
  </script>
  
  <style scoped>
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .no-articles {
    text-align: center;
    color: #666;
    padding: 40px 0;
  }
  
  .board-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .board-item {
    display: flex;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .board-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  }
  </style>