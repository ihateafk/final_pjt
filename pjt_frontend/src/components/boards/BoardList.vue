<template>
    <div v-if="!store.articles">
        작성된 글이 없습니다
    </div>
    <div v-else
        v-for="article in store.articles"
        :key="article.pk"
    >
      <BoardListItem :article="article"/>
    </div>
</template>

<script setup>
    import { onMounted } from 'vue'
    import { useBoardsStore } from '@/stores/boards'
    import BoardListItem from '@/components/boards/BoardListItem.vue'
    
    const store = useBoardsStore()

    onMounted(() => {
        store.getArticles()
    })

</script>

<style scoped>

</style>