<template>
    <div v-if="!store.articles">
        작성된 글이 없습니다
    </div>
    <div v-else
        v-for="article in store.articles"
        :key="article.pk"
    >
      <p> 작성자 : {{ article.user.name }} </p>
      <p> 제목 : {{ article.title }}</p>
      <p> 내용 : {{ article.content }} </p>
      <hr>
    </div>
</template>

<script setup>
    import { onMounted } from 'vue'
    import { useBoardsStore } from '@/stores/boards'
    
    const store = useBoardsStore()

    onMounted(() => {
        store.getArticles()
    })

</script>

<style scoped>

</style>