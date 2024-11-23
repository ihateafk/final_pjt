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

    const articleItemChange = function () {
        boardStore.articleItem = props.article
    }

</script>

<style scoped>

</style>