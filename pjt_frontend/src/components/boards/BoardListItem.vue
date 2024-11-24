<template>
    <div>
        <RouterLink
            :to="{name: 'boardsDetail', params : {id : article.id} }"
            @click="articleItemChange"
        >
            <p>{{ article.user.name }}</p>
            <p>{{ article.title }}</p>
            <p>{{ article.content }}</p>
            
        </RouterLink>
        <p>댓글 수 : {{ article.comment_count }}</p>
        <hr>
    </div>

</template>

<script setup>
    import { defineProps } from 'vue'
    import { RouterLink } from 'vue-router'
    import { useBoardsStore } from '@/stores/boards'

    const boardStore = useBoardsStore()

    const props = defineProps({
        article : Object
    })

    const articleItemChange = async function () {
        boardStore.articleItem = props.article
        await boardStore.getComments(props.article.id)
    }

</script>

<style scoped>

</style>