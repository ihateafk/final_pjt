<template>
  <div class="container-fluid my-4">
    <div id="body" class="border rounded-3 p-4 shadow-sm">
      <div id="nm" class="d-flex flex-column mb-3" @click="goToDetail">
        <div id="co_nm" class="fw-bold">{{ productdata.kor_co_nm }}</div>
        <div id="prdt_nm fs-4">{{ productdata.fin_prdt_nm }}</div>
      </div>
      <div id="intrrate" class="d-flex justify-content-between mb-3">
        <div>
          <p class="mb-1">최고 우대 금리</p>
          <p class="text-primary fw-bold">{{ max_intr_rate }}</p>
        </div>
        <div>
          <p class="mb-1">최저 금리</p>
          <p class="text-primary fw-bold">{{ min_intr_rate }}</p>
        </div>
      </div>
      <div id="otherinfo">
        <p class="mb-2">
          <span class="fw-bold">만기 후 이자율:</span> {{ productdata.mtrt_int }}
        </p>
        <p class="mb-2">
          <span class="fw-bold">가입 방법:</span> {{ productdata.join_way }}
        </p>
        <p class="mb-2">
          <span class="fw-bold">우대 조건:</span> {{ productdata.spcl_cnd }}
        </p>
        <p class="mb-2">
          <span class="fw-bold">가입 대상:</span> {{ productdata.join_member }}
        </p>
        <p class="mb-2">
          <span class="fw-bold">유의 사항:</span> {{ productdata.etc_note }}
        </p>
      </div>
      <div id="favorbtn" v-if="$route.name === 'favorite'" class="d-flex justify-content-end">
        <button class="btn btn-outline-danger" @click="deleteProductfromList('favorite')">관심상품 삭제</button>
      </div>
      <div id="joinbtn" v-if="$route.name === 'subscribe'" class="d-flex justify-content-end">
        <button class="btn btn-danger" @click="deleteProductfromList('join')">가입한 상품 삭제</button>
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

<style lang="css" scoped>

</style>