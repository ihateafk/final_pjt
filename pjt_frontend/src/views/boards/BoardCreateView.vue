<template>
  <div class="container py-4">
      <!-- 헤더 -->
      <div class="d-flex justify-content-between align-items-center mb-4">
          <h5 class="mb-0">게시글 작성</h5>
      </div>

      <!-- 작성 폼 -->
      <form @submit.prevent="submitData" class="bg-white rounded p-4 border">
          <div class="mb-3">
              <label for="title" class="form-label">제목</label>
              <input 
                  type="text" 
                  id="title" 
                  v-model="title" 
                  required
                  class="form-control"
                  placeholder="제목을 입력하세요"
              >
          </div>
          <div class="mb-4">
              <label for="content" class="form-label">내용</label>
              <textarea 
                  id="content" 
                  v-model="content" 
                  required
                  class="form-control"
                  rows="10"
                  placeholder="내용을 입력하세요"
              ></textarea>
          </div>
          <div class="d-flex justify-content-end gap-2">
              <RouterLink 
                  :to="{ name: 'board' }"
                  class="btn btn-outline-secondary"
              >
                  취소
              </RouterLink>
              <button 
                  type="submit"
                  class="btn btn-primary"
              >
                  작성하기
              </button>
          </div>
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBoardsStore } from '@/stores/boards.js'
import { RouterLink } from 'vue-router'

const store = useBoardsStore()

const title = ref('')
const content = ref('')

const submitData = function () {
  const article = {
      title: title.value,
      content: content.value,
  }

  store.createArticle(article)
  title.value = ''
  content.value = ''
}
</script>

<style scoped>
.container {
  max-width: 768px;
}

.form-control:focus {
  box-shadow: none;
  border-color: #86b7fe;
}

textarea.form-control {
  resize: none;
}

@media (max-width: 768px) {
  .container {
      padding-left: 1rem;
      padding-right: 1rem;
  }
}
</style>