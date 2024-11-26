<template>
    <RouterLink
      :to="{ name: 'boardsDetail', params: { id: article.id } }"
      @click="articleItemChange"
      class="text-decoration-none w-100"
    >
      <div class="d-flex justify-content-between align-items-center">
        <div class="flex-grow-1 d-flex align-items-center gap-3">
          <h6 class="article-title mb-0">{{ article.title }}</h6>
          <span class="author-name">{{ article.user.name }}</span>
        </div>
        
        <div class="d-flex align-items-center comment-section">
          <span class="comment-count">
            댓글 {{ article.comment_count }}
          </span>
          <i class="bi bi-chevron-right ms-2"></i>
        </div>
      </div>
    </RouterLink>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useBoardsStore } from '@/stores/boards'
  
  const boardStore = useBoardsStore()
  
  const props = defineProps({
    article: Object
  })
  
  const articleItemChange = async function () {
    boardStore.articleItem = props.article
    await boardStore.getComments(props.article.id)
  }
  </script>
  
  <style scoped>
  .author-name {
    font-size: 0.875rem;
    color: #666;
  }
  
  .article-title {
    color: #333;
    font-size: 1rem;
    font-weight: 500;
  }
  
  .comment-section {
    color: #666;
  }
  
  .comment-count {
    font-size: 0.875rem;
  }
  
  :deep(.board-item:hover) {
    .article-title {
      color: #000;
    }
  
    .comment-section {
      color: #444;
    }
  }
  
  @media (max-width: 768px) {
    .article-title {
      font-size: 0.9rem;
    }
    
    .author-name, 
    .comment-count {
      font-size: 0.8rem;
    }
  }
  </style>