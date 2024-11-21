<template>
  <RouterLink
    :to="{ name: 'depositDetail', params : {id : deposit.fin_co_no} }"
    @click="depositItemchange"
  >
    <div>
      <p>회사명 : {{ deposit.kor_co_nm }}</p>
      <p>상품명 : {{ deposit.fin_prdt_nm }}</p>
      
    </div>
  </RouterLink>
  <hr>
</template>

<script setup>
  import { useDepositStore } from '@/stores/deposit';
  import { defineProps } from 'vue';
  import { RouterLink } from 'vue-router';

  const store = useDepositStore()

  const props = defineProps({
    deposit: Object
  })
  
  const depositItemchange = function () {
    store.depositItem = props.deposit
  }

</script>

<style scoped>

</style>