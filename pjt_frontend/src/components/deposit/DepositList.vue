<template>
  <div class="container">
    <h1 class="title">예금 상품 목록</h1>
    <div class="search-container">
      <input 
        type="text" 
        v-model="searchQuery"
        placeholder="은행명 또는 상품명으로 검색"
        class="search-input"
        @input="handleSearch"
      >
    </div>
    <div class="deposit-list">
      <DepositListItem
        v-for="list in filteredDepositList"
        :key="list.fin_prdt_cd"
        :deposit="list"
        :optionList="depositOptionList"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import DepositListItem from './DepositListItem.vue';

const depositList = ref([])
const depositOptionList = ref([])
const searchQuery = ref('')

// 검색 결과를 필터링하는 computed 속성
const filteredDepositList = computed(() => {
  const query = searchQuery.value.toLowerCase()
  if (!query) return depositList.value
  
  return depositList.value.filter(item => 
    item.kor_co_nm.toLowerCase().includes(query) || 
    item.fin_prdt_nm.toLowerCase().includes(query)
  )
})

const callDeposit = async () => {
  try {
    const response = await axios.get('https://cors-anywhere.herokuapp.com/http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json', {
      params: {
        auth: import.meta.env.VITE_APP_API_KEY,
        topFinGrpNo: '020000',
        pageNo: 1
      },
    })

    depositList.value = response.data.result.baseList
    depositOptionList.value = response.data.result.optionList
  } catch (err) {
    console.error('API 호출 에러:', err)
  }
}

onMounted(() => {
  callDeposit()
})
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  text-align: center;
  margin-bottom: 30px;
  color: #2c3e50;
}

.search-container {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
}

.search-input {
  width: 100%;
  max-width: 400px;
  padding: 10px 15px;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #3498db;
}

.deposit-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

@media (max-width: 768px) {
  .container {
    padding: 10px;
  }
  
  .deposit-list {
    grid-template-columns: 1fr;
  }
}
</style>