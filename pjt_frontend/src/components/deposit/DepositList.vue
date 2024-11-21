<template>
  <div>
    <h1>deposit list</h1>
    <div>
      <DepositListItem
        v-for="list in depositList"
        :deposit="list"
      />
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import DepositListItem from './DepositListItem.vue';

  const depositList = ref([])
  const depositOptionList = ref([])

  const callDeposit = () => {
    // 프록시 서버 제공해 주는 사이트로 ~com까지 사이트 들어가서 버튼 활성화 해야 처리됨
    // 백엔드 store 처리 시 원래 url로 수정 필요
    axios.get('https://cors-anywhere.herokuapp.com/http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json', {
      params: {
        auth: import.meta.env.VITE_APP_API_KEY,
        topFinGrpNo:'020000',
        pageNo: 1,
      },
    })
      .then((res) => {
        const parsedDepositList = res.data.result.baseList
        depositList.value = parsedDepositList

        const parsedDepositOptionList = res.data.result.optionList
        depositOptionList.value = parsedDepositOptionList
        
      })
      .catch((err) => {
        console.log(err)
      })
  }

  onMounted(() => {
    callDeposit()
  })

</script>

<style scoped>

</style>