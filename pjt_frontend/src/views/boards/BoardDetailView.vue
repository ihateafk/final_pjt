<template>
    <div class="container py-4">
        <RouterLink :to="{ name: 'board' }" class="back-link text-decoration-none">
            <i class="bi bi-arrow-left me-2"></i>뒤로가기
        </RouterLink>
        
        <div class="content-section bg-white rounded p-4 my-4">
            <div class="mb-4">
                <h5 class="mb-3">{{ boardStore.articleItem?.title }}</h5>
                <div class="d-flex justify-content-between align-items-center text-secondary small">
                    <span>{{ boardStore.articleItem?.user?.name }}</span>
                    <span>{{ boardStore.articleItem?.created_at }}</span>
                </div>
            </div>

            <p class="content-text mb-4">{{ boardStore.articleItem?.content }}</p>

            <div v-if="boardStore.isAuthor" class="d-flex gap-2 justify-content-end">
                <RouterLink
                    :to="{
                        name: 'boardUpdate',
                        params: { boardId: boardStore.articleItem.id }
                    }"
                    class="btn btn-outline-secondary btn-sm"
                >
                    수정
                </RouterLink>
                <button @click="isDelete" class="btn btn-outline-danger btn-sm">삭제</button>
            </div>
        </div>

        <div class="comments-section bg-white rounded p-4">
            <h6 class="mb-3">댓글 ({{ boardStore.comments.length }})</h6>
            
            <div class="comment-form mb-4" v-if="userStore.token !== null">
                <textarea 
                    v-model="commentContent" 
                    placeholder="댓글을 입력하세요"
                    rows="3"
                    class="form-control mb-2"
                ></textarea>
                <div class="d-flex justify-content-end">
                    <button @click="submitComment" class="btn btn-primary btn-sm">댓글 작성</button>
                </div>
            </div>

            <div class="comments-list">
                <div 
                    v-for="comment in boardStore.comments" 
                    :key="comment.id" 
                    class="comment-item d-flex gap-3 py-3 border-bottom"
                >
                    <div class="profile-image">
                        <i class="bi bi-person-circle fs-4 text-secondary"></i>
                    </div>
                    <div class="flex-grow-1">
                        <p class="comment-author mb-1">{{ comment.user?.name }}</p>
                        <p class="comment-content mb-0">{{ comment.comment }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
// 스크립트 부분은 그대로 유지
import { computed, onMounted, watch, ref } from 'vue'
import { useBoardsStore } from '@/stores/boards'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const boardStore = useBoardsStore()
const userStore = useUserStore()
const commentContent = ref('')

const submitComment = async () => {
    if (!commentContent.value.trim()) return
    await boardStore.createComment(commentContent.value)
    commentContent.value = ''
}

const loadArticle = async () => {
    const boardId = router.currentRoute.value.params.boardId
    if (boardId) {
        await boardStore.getArticleDetail(boardId)
        await boardStore.getComments(boardId)
    }
}

watch(
    () => router.currentRoute.value.params.boardId,
    (newBoardId) => {
        if (newBoardId) {
            loadArticle()
        }
    },
    { immediate: true }
)

onMounted(async () => {
    await userStore.getUserInfo()
})

const isDelete = () => {
    boardStore.deleteArticle(boardStore.articleItem.id)
}
</script>

<style scoped>
.container {
    max-width: 768px;
}

.back-link {
    color: #333;
    display: inline-flex;
    align-items: center;
}

.content-section {
    border: 1px solid #eee;
}

.content-text {
    white-space: pre-wrap;
    color: #333;
    line-height: 1.6;
}

.comments-section {
    border: 1px solid #eee;
}

.comment-form textarea {
    resize: none;
    border-color: #dee2e6;
}

.comment-form textarea:focus {
    box-shadow: none;
    border-color: #86b7fe;
}

.comment-author {
    font-size: 0.9rem;
    font-weight: 500;
    color: #333;
}

.comment-content {
    font-size: 0.9rem;
    color: #666;
    white-space: pre-wrap;
}

@media (max-width: 768px) {
    .container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>