import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useUserStore } from './user'
import axios from 'axios'

export const useBoardsStore = defineStore('boards', () => {
    const userStore = useUserStore()
    
    const articles = ref([])
    const articleItem = ref(null)
    const comments = ref([])

    const router = useRouter()

    const isLogin = computed(() => {
        if (userStore.token === null) {
            return false
        } else {
            return true
        }
    })

    const getArticles = function () {
        axios({
            method : 'GET',
            url: 'http://127.0.0.1:8000/boards/',
            headers: {
                Authorization : `Token ${userStore.token}`,
            }
        })
        .then((res) => {
            articles.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }

    const createArticle = function ({ title, content }) {
        axios({
            method : 'POST',
            url: 'http://127.0.0.1:8000/boards/',
            data: {
                title,
                content
            },
            headers: {
                Authorization : `Token ${userStore.token}`,
            }
        })
        .then((res) => {
            router.push({name: 'board'})
        })
        .catch((err) => {
            console.log(err)
        })
    }

    const getArticleDetail = function (boardId) {
        if (!boardId) return
        
        articleItem.value = null
        
        return axios({
            method: 'GET',
            url: `${userStore.URL}/boards/${boardId}/`,
            headers: {
                Authorization: `Token ${userStore.token}`
            }
        })
        .then((res) => {
            articleItem.value = res.data
            getComments(boardId)
            return res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }

    const updateArticle = function (boardId, { title, content }) {
        return axios({
            method: 'PUT',
            url: `${userStore.URL}/boards/${boardId}/`,
            data: {
                title,
                content
            },
            headers: {
                Authorization: `Token ${userStore.token}`,
            }
        })
        .then((res) => {
            articleItem.value = res.data;
    
            router.push({ 
                name: 'boardsDetail',
                params: { id: boardId }
            });
        })
        .catch((err) => {
            console.log(err);
            if (err.response && err.response.status === 403) {
                alert('수정 권한이 없습니다.');
            } else {
                alert('수정 중 오류가 발생했습니다.');
            }
        });
    };
    

    const isAuthor = computed(() => {
        return articleItem.value?.user?.pk === userStore.userId
    })

    const deleteArticle = function (boardId) {
        if (confirm('정말 삭제하시겠습니까?')) {
            axios({
                method: 'DELETE',
                url: `http://127.0.0.1:8000/boards/${boardId}/`,
                headers: {
                    Authorization: `Token ${userStore.token}`,
                }
            })
            .then(() => {
                router.push({ name: 'board' })
            })
            .catch((err) => {
                console.log(err)
                if (err.response.status === 403) {
                    alert('삭제 권한이 없습니다.')
                }
            })
        }
    }

    const createComment = function (comment) {
        if (!articleItem.value) return
    
        axios({
            method: 'POST',
            url: `${userStore.URL}/boards/${articleItem.value.id}/comments/`,
            data: {
                comment: comment
            },
            headers: {
                Authorization: `Token ${userStore.token}`
            }
        })
        .then((res) => {
            getComments(articleItem.value.id)
        })
        .catch((err) => {
            console.log(err)
            if (err.response && err.response.status === 401) {
                alert('로그인이 필요합니다.')
            } else {
                alert('댓글 작성 중 오류가 발생했습니다.')
            }
        })
    }

    const getComments = function (boardId) {
        if (!boardId) return
    
        comments.value = []
    
        axios({
            method: 'GET',
            url: `${userStore.URL}/boards/${boardId}/comment/`,
            headers: {
                Authorization: `Token ${userStore.token}`
            }
        })
        .then((res) => {
            comments.value = res.data
            console.log('댓글 데이터:', res.data)
        })
        .catch((err) => {
            console.log('댓글 조회 에러:', err)
        })
    }

    const deleteComment = function(commentId) {
        if (!commentId) return
        
        if (confirm('댓글을 삭제하시겠습니까?')) {
            axios({
                method: 'DELETE',
                url: `${userStore.URL}/boards/${articleItem.value.id}/comment/${commentId}/`,
                headers: {
                    Authorization: `Token ${userStore.token}`
                }
            })
            .then(() => {
                getComments(articleItem.value.id)
            })
            .catch((err) => {
                console.log(err)
                if (err.response && err.response.status === 403) {
                    alert('댓글 삭제 권한이 없습니다.')
                } else {
                    alert('댓글 삭제 중 오류가 발생했습니다.')
                }
            })
        }
    }



    return { articles, getArticles, createArticle, isLogin, articleItem, updateArticle, deleteArticle, getArticleDetail, isAuthor, createComment, comments, getComments, deleteComment }
}, {persist : true},)
