<template>
    <div class="container py-4">
        <!-- 헤더 -->
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h5 class="mb-0">게시글 수정</h5>
        </div>
 
        <!-- 수정 폼 -->
        <form @submit.prevent="updateArticle" class="bg-white rounded p-4 border">
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
                <button 
                    type="button" 
                    @click="cancel"
                    class="btn btn-outline-secondary"
                >
                    취소
                </button>
                <button 
                    type="submit"
                    class="btn btn-primary"
                >
                    수정하기
                </button>
            </div>
        </form>
    </div>
 </template>
 
 <script setup>
 import { ref, onMounted } from 'vue'
 import { useRouter, useRoute } from 'vue-router'
 import { useBoardsStore } from '@/stores/boards'
 
 const router = useRouter()
 const route = useRoute()
 const boardStore = useBoardsStore()
 
 const title = ref('')
 const content = ref('')
 
 onMounted(async () => {
    const boardId = route.params.id
    await boardStore.getArticleDetail(boardId)
    
    if (boardStore.articleItem) {
        title.value = boardStore.articleItem.title
        content.value = boardStore.articleItem.content
    }
 })
 
 const updateArticle = () => {
    const boardId = route.params.id
    boardStore.updateArticle(boardId, {
        title: title.value,
        content: content.value
    })
 }
 
 const cancel = () => {
    router.push({
        name: 'boardsDetail',
        params: { id: route.params.id }
    })
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