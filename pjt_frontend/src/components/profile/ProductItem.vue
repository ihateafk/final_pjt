<template>
  <div class="container-fluid p-3">
    <div class="card border-0 shadow-sm hover-shadow">
      <!-- Product Header -->
      <div class="card-body p-4">
        <div class="cursor-pointer mb-4" @click="goToDetail">
          <h6 class="text-secondary mb-2">{{ productdata.kor_co_nm }}</h6>
          <h5 class="card-title fw-bold">{{ productdata.fin_prdt_nm }}</h5>
        </div>

        <!-- Interest Rates -->
        <div class="row mb-4">
          <div class="col-6">
            <div class="p-3 bg-light rounded-3">
              <div class="small text-secondary mb-1">최고 우대 금리</div>
              <div class="fs-4 text-primary fw-bold">{{ max_intr_rate }}</div>
            </div>
          </div>
          <div class="col-6">
            <div class="p-3 bg-light rounded-3">
              <div class="small text-secondary mb-1">최저 금리</div>
              <div class="fs-4 text-primary fw-bold">{{ min_intr_rate }}</div>
            </div>
          </div>
        </div>

        <!-- Product Details -->
        <div class="mb-4">
          <div class="mb-3">
            <div class="small text-secondary mb-1">만기 후 이자율</div>
            <div>{{ productdata.mtrt_int }}</div>
          </div>
          
          <div class="mb-3">
            <div class="small text-secondary mb-1">가입 방법</div>
            <div>{{ productdata.join_way }}</div>
          </div>
          
          <div class="mb-3">
            <div class="small text-secondary mb-1">우대 조건</div>
            <div>{{ productdata.spcl_cnd }}</div>
          </div>
          
          <div class="mb-3">
            <div class="small text-secondary mb-1">가입 대상</div>
            <div>{{ productdata.join_member }}</div>
          </div>
          
          <div>
            <div class="small text-secondary mb-1">유의 사항</div>
            <div>{{ productdata.etc_note }}</div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="d-flex justify-content-end">
          <button 
            v-if="$route.name === 'favorite'" 
            class="btn btn-outline-danger px-4"
            @click="deleteProductfromList('favorite')"
          >
            관심상품 삭제
          </button>
          <button 
            v-if="$route.name === 'subscribe'" 
            class="btn btn-danger px-4"
            @click="deleteProductfromList('join')"
          >
            가입한 상품 삭제
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useDepositStore } from '@/stores/deposit';
import { useSavingsStore } from '@/stores/savings';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const props = defineProps({
  productdata: Object,
})
const emit = defineEmits(['refreshdata'])
const userStore = useUserStore()
const depositStore = useDepositStore()
const savingStore = useSavingsStore()
const route = useRoute()
const router = useRouter()

const max_intr_rate = ref(0)
const min_intr_rate = ref(100)

props.productdata.options.forEach((option) => {
  if (option.intr_rate2 > max_intr_rate.value) {
    max_intr_rate.value = option.intr_rate2
  }
  if (option.intr_rate < min_intr_rate.value) {
    min_intr_rate.value = option.intr_rate
  }
})

max_intr_rate.value = Number.parseFloat(max_intr_rate.value).toFixed(2) + "%"
min_intr_rate.value = Number.parseFloat(min_intr_rate.value).toFixed(2) + "%"

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

const goToDetail = function () {
  if (route.name === 'favorite') {
    depositStore.depositItem = props.productdata
    depositStore.depositOptionList = props.productdata.options
    router.push({ name: 'depositDetail', params: { id: 99 }})
  }
  if (route.name === 'subscribe') {
    savingStore.savingsItem = props.productdata
    savingStore.savingsOptionList = props.productdata.options
    router.push({ name: 'savingsDetail', params: { id: 99 }})
  }
}
</script>

<style scoped>
.hover-shadow {
  transition: all 0.3s ease;
}

.hover-shadow:hover {
  transform: translateY(-2px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
}

.cursor-pointer {
  cursor: pointer;
}

.card {
  background-color: #ffffff;
}

.bg-light {
  background-color: #f8f9fa !important;
}

.btn-danger, .btn-outline-danger {
  padding: 0.5rem 1.5rem;
}

.fs-4 {
  font-size: 1.5rem !important;
}
</style>