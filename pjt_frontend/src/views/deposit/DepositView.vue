<template>
  <div class="container">
    <div class="tab-container">
      <div
        class="tab-item"
        :class="{ 'active': selectedView === 'deposit' }"
        @click="selectedView = 'deposit'"
      >
        예금
      </div>
      <div
        class="tab-item"
        :class="{ 'active': selectedView === 'savings' }"
        @click="selectedView = 'savings'"
      >
        적금
      </div>
    </div>

    <div v-if="selectedView === 'deposit'">
      <DepositList />
    </div>
    <div v-if="selectedView === 'savings'">
      <SavingsList />
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import DepositList from '@/components/deposit/DepositList.vue';
  import SavingsList from '@/components/savings/SavingsList.vue';

  const selectedView = ref('deposit');
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.tab-container {
  display: flex;
  align-items: flex-start;
  margin-bottom: 30px;
}

.tab-item {
  padding: 10px 20px;
  border: 1px solid #ddd;
  border-bottom: none;
  border-radius: 4px 4px 0 0;
  background-color: #f5f5f5;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-right: 10px;
}

.tab-item.active {
  background-color: #fff;
  font-weight: bold;
}

.tab-item:not(.active):hover {
  background-color: #e9e9e9;
}
</style>