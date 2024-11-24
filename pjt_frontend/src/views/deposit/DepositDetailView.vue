<template>
  <div class="container py-4">
    <!-- 뒤로가기 버튼 -->
    <RouterLink :to="{name:'deposit'}" class="back-link text-decoration-none">
      <i class="bi bi-arrow-left me-2"></i>돌아가기
    </RouterLink>
 
    <!-- 상품 상세 카드 -->
    <div class="card mt-4">
      <!-- 상품 헤더 -->
      <div class="card-header bg-white border-bottom p-4">
        <div class="d-flex justify-content-between align-items-start">
          <div>
            <h5 class="mb-2">{{ store.depositItem.fin_prdt_nm }}</h5>
            <p class="text-secondary mb-0">{{ store.depositItem.kor_co_nm }}</p>
          </div>
          <button 
            @click="addProduct('favorite')" 
            class="btn btn-outline-primary btn-sm"
          >
            <i class="bi bi-star me-1"></i>관심상품 등록
          </button>
        </div>
      </div>
 
      <!-- 금리 정보 -->
      <div class="card-body p-4">
        <div class="row mb-4">
          <div class="col-6">
            <div class="interest-rate">
              <small class="text-secondary">최고 우대 금리</small>
              <h3 class="text-primary mb-0">{{ max_intr_rate }}</h3>
            </div>
          </div>
          <div class="col-6">
            <div class="interest-rate">
              <small class="text-secondary">최저 금리</small>
              <h3 class="text-secondary mb-0">{{ min_intr_rate }}</h3>
            </div>
          </div>
        </div>
 
        <!-- 상품 상세 정보 -->
        <div class="product-details">
          <div class="info-item mb-3">
            <small class="text-secondary d-block mb-1">만기 후 이자율</small>
            <p class="mb-0">{{ store.depositItem.mtrt_int }}</p>
          </div>
          <div class="info-item mb-3">
            <small class="text-secondary d-block mb-1">가입 방법</small>
            <p class="mb-0">{{ store.depositItem.join_way }}</p>
          </div>
          <div class="info-item mb-3">
            <small class="text-secondary d-block mb-1">우대 조건</small>
            <p class="mb-0">{{ store.depositItem.spcl_cnd }}</p>
          </div>
          <div class="info-item mb-3">
            <small class="text-secondary d-block mb-1">가입 대상</small>
            <p class="mb-0">{{ store.depositItem.join_member }}</p>
          </div>
          <div class="info-item">
            <small class="text-secondary d-block mb-1">유의 사항</small>
            <p class="mb-0">{{ store.depositItem.etc_note }}</p>
          </div>
        </div>
      </div>
 
      <!-- 가입하기 버튼 -->
      <div class="card-footer bg-white border-top p-4">
        <button 
          @click="addProduct('join')" 
          class="btn btn-primary w-100"
        >
          가입한 상품 추가하기
        </button>
      </div>
    </div>
  </div>
 </template>
 
 <script setup>
 import { useDepositStore } from '@/stores/deposit';
 import { useUserStore } from '@/stores/user';
 import axios from 'axios';
 import { onBeforeMount, ref } from 'vue';
 import { RouterLink } from 'vue-router';
 
 const store = useDepositStore()
 const userStore = useUserStore()
 
 const max_intr_rate = ref(0)
 const min_intr_rate = ref(100)
 
 store.depositOptionList.forEach((option) => {
  if (option.intr_rate2 > max_intr_rate.value) {
    max_intr_rate.value = option.intr_rate2
  }
  if (option.intr_rate < min_intr_rate.value) {
    min_intr_rate.value = option.intr_rate
  }
 })
 
 max_intr_rate.value = Number.parseFloat(max_intr_rate.value).toFixed(2) + "%"
 min_intr_rate.value = Number.parseFloat(min_intr_rate.value).toFixed(2) + "%"
 
 const addProduct = function (which) {
  axios({
    method: 'post',
    url: `${userStore.URL}/finance/product/${which}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: {
      fin_category: 1,
      base: store.depositItem,
      options: store.depositOptionList,
    }
  })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err.response.data)
    })
 }

 const deleteProductfromList = function (which) {
  axios({
    method: 'delete',
    url: `${userStore.URL}/finance/product/${which}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: {
      product_id: props.productdata.id
    }
  })
    .then((res) => {
      console.log(res)
      emit('refreshdata')
    })
    .catch((err) => {
      console.log(err.response.data)
    })
}
 </script>
 
 <style scoped>
 .container {
  max-width: 768px;
 }
 
 .back-link {
  color: #333;
  display: inline-flex;
  align-items: center;
 }
 
 .card {
  border: 1px solid #eee;
  border-radius: 8px;
 }
 
 .interest-rate {
  text-align: center;
  padding: 1rem;
  background-color: #f8f9fa;
  border-radius: 8px;
 }
 
 .product-details p {
  color: #333;
  line-height: 1.5;
 }
 
 @media (max-width: 768px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
 }
 </style>