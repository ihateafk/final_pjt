<template>
  <div class="container-fluid h-100 py-4 d-flex">
    <div class="border border-light rounded-end shadow mx-4" id="menu" style="width: 280px; height: 100%; flex-shrink: 0;">
      <nav class="h-100 d-flex flex-column justify-content-between">
        <div>
          <div id="title" class="fw-bold mb-3">Menu</div>
          <div id="menulist">
            <div class="my-4 pb-4 border-bottom border-gray-300">
              <RouterLink :to="{ name: 'profilemain' }" class="nav-link">마이 페이지</RouterLink>
            </div>
            <div class="my-4 pb-4 border-bottom border-gray-300">
              <RouterLink :to="{ name: 'person' }" class="nav-link">개인 정보</RouterLink>
            </div>
            <div class="my-4 pb-4">
              <RouterLink :to="{ name: 'favorite' }" class="nav-link">관심 상품</RouterLink>
            </div>
            <div class="my-4 pb-4">
              <RouterLink :to="{ name: 'subscribe' }" class="nav-link">가입 상품</RouterLink>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <div class="flex-grow-1 d-flex flex-column">
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
#menu {
  padding: 1.5rem;
}

#title {
  font-size: 1.25rem;
}

.nav-link {
  color: #495057;
  text-decoration: none;
}

.nav-link.router-link-active {
  font-weight: bold;
  color: #007bff;
}
</style>