<template>
  <div>
    <RouterLink :to="{ name: 'deposit'}"> 돌아가기 </RouterLink>
  </div>
  <div>
    <p>회사명 : {{store.savingsItem.kor_co_nm}}</p>
    <p>금융 상품명 : {{store.savingsItem.fin_prdt_nm}}</p>
    <p>가입 방법 : {{store.savingsItem.join_way}}</p>
    <p>만기 후 이자율 : {{store.savingsItem.mtrt_int}}</p>
    <p>우대 조건 : {{ store.savingsItem.spcl_cnd }}</p>
    <p>가입 대상 : {{ store.savingsItem.join_member }}</p>
    <p>유의 사항 : {{ store.savingsItem.etc_note }}</p>
  </div>
</template>

<script setup>
  import { RouterLink } from 'vue-router';
  import { useSavingsStore } from '@/stores/savings';

  const store = useSavingsStore()

</script>

<style scoped>

</style>