<template>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
        <div>
            <label for="title">제목:</label>
            <input 
                type="text" 
                id="title" 
                v-model="title" 
                required
            >
        </div>
        <div>
            <label for="content">내용:</label>
            <textarea 
                id="content" 
                v-model="content" 
                required
            ></textarea>
        </div>
        <div class="button-group">
            <button type="submit">수정하기</button>
            <button type="button" @click="cancel">취소</button>
        </div>
    </form>
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
</style>