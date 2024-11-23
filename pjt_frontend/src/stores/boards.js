import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useUserStore } from './user'
import axios from 'axios'

export const useBoardsStore = defineStore('boards', () => {
    const userStore = useUserStore()
    const articles = ref([])
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
            console.log(res)
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

    return { articles, getArticles, createArticle, isLogin}
}, {persist : true},)
