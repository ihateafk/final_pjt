<template>
  <div>
    <div id="menu">
      <nav>
        <div id="title">Menu</div>
        <div id="menulist">
          <div>
            <RouterLink :to="{ name: 'profilemain' }">마이 페이지</RouterLink>
          </div>
          <div>
            <RouterLink :to="{ name: 'person' }">개인 정보</RouterLink>
          </div>
          <div>
            <RouterLink :to="{ name: 'favorate' }">관심 상품</RouterLink>
          </div>
          <div>
            <RouterLink :to="{ name: 'subscribe' }">가입 상품</RouterLink>
          </div>
        </div>
      </nav>
    </div>
    <div>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUpdated, watch } from 'vue';
import { onBeforeRouteUpdate, useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute()

onMounted(() => {
  router.push({ name: 'profilemain' })
})

watch(() => route.name, () => {
  if (route.name === 'profile') {
    router.push({ name: 'profilemain' })
  }
})
</script>

<style lang="css" scoped>

</style>