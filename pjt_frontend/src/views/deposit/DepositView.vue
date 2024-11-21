<template>
  <div>
    <p @click="selectedView = 'deposit'">예금</p>
    <p @click="selectedView = 'savings'">적금</p>
  </div>

  <div v-if="selectedView === 'deposit'">
    <DepositList/>
  </div>
  <div v-if="selectedView === 'savings'">
    <SavingsList/>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import DepositList from '@/components/deposit/DepositList.vue';
  import SavingsList from '@/components/savings/SavingsList.vue';

  const selectedView = ref('deposit')

</script>

<style scoped>

</style>