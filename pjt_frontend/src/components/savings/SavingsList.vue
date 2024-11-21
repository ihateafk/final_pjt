<template>
  <div>
    <h1>적금 상품 목록</h1>
    <div>
      <input type="text" placeholder="은행명 또는 상품명으로 검색">
    </div>
    <div>
      <SavingsListItem
        v-for="list in filteredSavingsList"
        :key="list.fin_prdt_cd"
        :savings="list"
        :optionList="savingsOptionList"
      />
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue';
  import axios from 'axios';
  import SavingsListItem from './SavingsListItem.vue';

  const savingsList = ref([])
  const savingsOptionList = ref([])
  const searchQuery = ref('')

  const filteredSavingsList = computed(() => {
    const query = searchQuery.value.toLowerCase()
    if (!query) return savingsList.value

    return savingsList.value.filter(item =>
      item.kor_co_nm.toLowerCase().includes(query) ||
      item.fin_prdt_nm.toLowerCase().includes(query)
    )
  })

  const callSavings = async () => {
    try {
      const response = await axios.get('https://cors-anywhere.herokuapp.com/http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json', {
        params: {
          auth: import.meta.env.VITE_APP_API_KEY,
          topFinGrpNo: '020000',
          pageNo: 1
        },
      })

      savingsList.value = response.data.result.baseList
      savingsOptionList.value = response.data.result.optionList
    } catch (err) {
      console.error('API 호출 에러 : ', err)
    }
  }

  onMounted(() => {
    callSavings()
  })

</script>

<style scoped>

</style>