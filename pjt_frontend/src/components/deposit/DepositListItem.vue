<template>
  <RouterLink
    :to="{ name: 'depositDetail', params : {id : deposit.fin_co_no} }"
    @click="depositItemchange"
    class="deposit-item"
  >
    <div class="deposit-content">
      <div class="company-info">
        <h2>{{ deposit.kor_co_nm }}</h2>
        <p class="product-name">{{ deposit.fin_prdt_nm }}</p>
      </div>
      <div class="interest-rates">
        <div class="rate-item">
          <span class="rate-label">6개월</span>
          <span class="rate-value">{{ getInterestRate(6) }}%</span>
        </div>
        <div class="rate-item">
          <span class="rate-label">12개월</span>
          <span class="rate-value">{{ getInterestRate(12) }}%</span>
        </div>
        <div class="rate-item">
          <span class="rate-label">24개월</span>
          <span class="rate-value">{{ getInterestRate(24) }}%</span>
        </div>
      </div>
    </div>
  </RouterLink>
 </template>
 
 <script setup>
 import { useDepositStore } from '@/stores/deposit';
 import { defineProps } from 'vue';
 import { RouterLink } from 'vue-router';
 
 const store = useDepositStore()
 
 const props = defineProps({
  deposit: {
    type: Object,
    required: true
  },
  optionList: {
    type: Array,
    required: true
  }
 })
 
 const depositItemchange = function () {
  store.depositItem = props.deposit
  const options = props.optionList.filter(opt => props.deposit.fin_prdt_cd === opt.fin_prdt_cd)
  store.depositOptionList = options
 }
 
 // 저축 기간별 금리 계산 함수
 const getInterestRate = (month) => {
  const option = props.optionList?.find(opt => 
    opt.save_trm === month.toString() && 
    opt.fin_prdt_cd === props.deposit.fin_prdt_cd
  )
  return option ? option.intr_rate : '-'
 }
 </script>
 
 <style scoped>
 .deposit-item {
  display: block;
  padding: 20px;
  border-radius: 8px;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
 }
 
 .deposit-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
 }
 
 .deposit-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
 }
 
 .company-info h2 {
  font-size: 1.25rem;
  color: #2c3e50;
  margin: 0 0 8px 0;
 }
 
 .product-name {
  font-size: 1rem;
  color: #666;
  margin: 0;
 }
 
 .interest-rates {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  gap: 10px;
 }
 
 .rate-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px;
  background-color: #f8f9fa;
  border-radius: 4px;
  flex: 1;
 }
 
 .rate-label {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 4px;
 }
 
 .rate-value {
  font-size: 1.125rem;
  color: #2c3e50;
  font-weight: bold;
 }
 
 @media (max-width: 768px) {
  .deposit-item {
    padding: 15px;
  }
 
  .company-info h2 {
    font-size: 1.1rem;
  }
 
  .rate-item {
    padding: 6px;
  }
 
  .rate-value {
    font-size: 1rem;
  }
 }
 </style>