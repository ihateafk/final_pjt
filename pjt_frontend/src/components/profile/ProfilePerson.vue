<template>
  <div>
    <div id="title">개인정보</div>
    <div id="body">
      <PersonInfoItem />
    </div>
    <div id="button">
      <!-- <button @click="goToChangePage">수정하기</button> -->
    </div>
  </div>
</template>

<script setup>
import PersonInfoItem from '@/components/profile/PersonInfoItem.vue'
import { useRouter } from 'vue-router';

const router = useRouter()

const goToChangePage = function () {
  router.push({ name: 'infochange' })
}
</script>

<style lang="css" scoped>

</style>