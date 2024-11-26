<template>
  <div class="container vh-70 d-flex align-items-center justify-content-center">
    <div class="row w-100 search-container">
      <div class="col-12 text-center mb-4">
        <h1>HomePage Logo</h1>
      </div>
      <div class="col-12">
        <div class="search-wrapper d-flex align-items-stretch" @click="$router.push({ name: 'recommend' })">
          <div class="flex-grow-1">
            <button 
              class="btn w-100 h-100 py-2 border text-center search-btn rounded-end-0" 
              :class="{
                'btn-outline-primary': !userStore.token,
                'btn-outline-success': userStore.token
              }"
            >
              {{ textvalue }}
            </button>
          </div>
          <div>
            <button class="btn border h-100 search-logo-btn rounded-start-0 d-flex align-items-center justify-content-center">
              <img 
                src="/search_logo_x48.png" 
                alt="search logo" 
                style="height: 24px; width: 24px;"
              >
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()

const textvalue = userStore.token !== null 
  ? 'AI 상담사에게 물어보기' 
  : '로그인하고 즉시 상담'
</script>

<style scoped>
.vh-70 {
  height: 70vh;
}

.search-container {
  max-width: 500px;
  width: 100%;
  padding: 0 15px;
}

.search-wrapper {
  width: 100%;
  max-width: 350px;
  margin: 0 auto;
}

.search-btn {
  width: 100%;
  max-width: none;
}

.search-logo-btn {
  aspect-ratio: 1;
  padding: 0;
  width: auto;
}

@media (max-width: 576px) {
  .search-wrapper {
    max-width: 100%;
  }
}
</style>