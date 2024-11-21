<template>
  <div>
    <RouterLink :to="{name:'deposit'}">돌아가기</RouterLink>
  </div>
  <div>
    <p>회사명 : {{store.depositItem.kor_co_nm}}</p>
    <p>금융 상품명 : {{store.depositItem.fin_prdt_nm}}</p>
    <p>가입 방법 : {{store.depositItem.join_way}}</p>
    <p>만기 후 이자율 : {{store.depositItem.mtrt_int}}</p>
    <p>우대 조건 : {{ store.depositItem.spcl_cnd }}</p>
    <p>가입 대상 : {{ store.depositItem.join_member }}</p>
    <p>유의 사항 : {{ store.depositItem.etc_note }}</p>
    <p>최고 한도 : {{ store.depositItem.max_limit }}</p>
  </div>
  <hr>
</template>

<script setup>
  import { useDepositStore } from '@/stores/deposit';
  import { RouterLink } from 'vue-router';

  const store = useDepositStore()

</script>

<style scoped>

</style>