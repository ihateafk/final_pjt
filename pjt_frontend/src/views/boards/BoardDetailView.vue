<template>
    <RouterLink :to="{ name: 'board' }">뒤로가기</RouterLink>
    <div>
        <p>{{ boardStore.articleItem?.user?.name }}</p>
        <p>{{ boardStore.articleItem?.title }}</p>
        <p>{{ boardStore.articleItem?.content }}</p>
        <p>{{ boardStore.articleItem?.created_at }}</p>

        <div v-if="boardStore.isAuthor">
            <RouterLink
                :to="{
                    name: 'boardUpdate',
                    params: { boardId: boardStore.articleItem.id }
                }"
            >
                수정
            </RouterLink>
            <button @click="isDelete">삭제</button>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted, watch } from 'vue'
import { useBoardsStore } from '@/stores/boards'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const boardStore = useBoardsStore()
const userStore = useUserStore()

const loadArticle = async () => {
    const boardId = router.currentRoute.value.params.boardId
    await boardStore.getArticleDetail(boardId)
}

watch(() => router.currentRoute.value.params.boardId, (newBoardId) => {
    if (newBoardId) {
        loadArticle()
    }
})

onMounted(async () => {
    await userStore.getUserInfo()
    await loadArticle()
})

const isDelete = () => {
    boardStore.deleteArticle(boardStore.articleItem.id)
}
</script>

<style scoped>
</style>
