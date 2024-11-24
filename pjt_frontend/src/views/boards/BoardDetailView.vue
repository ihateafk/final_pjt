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

    <div class="comments-section">
        <h3>댓글 ({{ boardStore.comments.length }})</h3>
        <div class="comment-form" v-if="userStore.token !== null">
            <textarea 
                v-model="commentContent" 
                placeholder="댓글을 입력하세요"
                rows="3"
            ></textarea>
            <button @click="submitComment">댓글 작성</button>
        </div>

        <div class="comments-list">
            <div 
                v-for="comment in boardStore.comments" 
                :key="comment.id" 
                class="comment-item"
            >
                <p class="comment-author">{{ comment.user?.name }}</p>
                <p class="comment-content">{{ comment.comment }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted, watch, ref } from 'vue'
import { useBoardsStore } from '@/stores/boards'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const boardStore = useBoardsStore()
const userStore = useUserStore()
const commentContent = ref('')

// 댓글 작성 함수
const submitComment = async () => {
    if (!commentContent.value.trim()) return  // 공백일 경우 작성하지 않음
    
    await boardStore.createComment(commentContent.value)  // 댓글 작성
    commentContent.value = ''  // 작성 후 입력창 초기화
}

// 게시글과 댓글을 불러오는 함수
const loadArticle = async () => {
    const boardId = router.currentRoute.value.params.boardId
    if (boardId) {
        await boardStore.getArticleDetail(boardId)  // 게시글 상세 가져오기
        await boardStore.getComments(boardId)  // 해당 게시글의 댓글 목록 가져오기
    }
}

// URL 파라미터로 boardId가 변경될 때마다 게시글과 댓글을 불러오기
watch(
    () => router.currentRoute.value.params.boardId,
    (newBoardId) => {
        if (newBoardId) {
            loadArticle()  // 새로운 boardId에 대해 게시글과 댓글을 다시 불러옴
        }
    },
    { immediate: true }  // 최초에 한 번 호출
)

onMounted(async () => {
    await userStore.getUserInfo()  // 사용자 정보 로드
})

// 게시글 삭제 함수
const isDelete = () => {
    boardStore.deleteArticle(boardStore.articleItem.id)  // 게시글 삭제
}
</script>

<style scoped>
.comments-section {
    margin-top: 2rem;
    padding: 1rem;
    border-top: 1px solid #eee;
}

.comment-form {
    margin-bottom: 1rem;
}

.comment-form textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.comment-item {
    padding: 1rem;
    border-bottom: 1px solid #eee;
}

.comment-author {
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.comment-content {
    white-space: pre-wrap;
}
</style>
