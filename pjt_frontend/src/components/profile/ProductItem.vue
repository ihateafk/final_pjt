<template>
  <div>
    <div id="header">
    </div>
    <div id="body">
      <div id="content" @click="goToDetail">
        <div id="title">
          <div id="nm">
            <div id="co_nm">
              <p>회사명 : {{productdata.kor_co_nm}}</p>
            </div>
            <div id="prdt_nm">
              <p>금융 상품명 : {{productdata.fin_prdt_nm}}</p>
            </div>
          </div>
          <div id="favorbtn" v-if="$route.name === 'favorite'">
            <button @click="deleteProductfromList('favorite')">관심상품 삭제</button>
          </div>
        </div>
        <div id="intrrate">
          <div>
            <p>최고 우대 금리 : {{ max_intr_rate }}</p>
          </div>
          <div>
            <p>최저 금리 : {{ min_intr_rate }}</p>
          </div>
        </div>
        <div id="otherinfo">
          <p>만기 후 이자율 : {{productdata.mtrt_int}}</p>
          <p>가입 방법 : {{productdata.join_way}}</p>
          <p>우대 조건 : {{ productdata.spcl_cnd }}</p>
          <p>가입 대상 : {{ productdata.join_member }}</p>
          <p>유의 사항 : {{ productdata.etc_note }}</p>
        </div>
      </div>
    </div>
    <div id="joinbtn" v-if="$route.name === 'subscribe'">
      <button @click="deleteProductfromList('join')">가입한 상품 삭제</button>
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
  if (route.name === 'join') {
    savingStore.savingsItem = props.productdata
    savingStore.savingsOptionList = props.productdata.options
    router.push({ name: 'savingsDetail', params: { id: 99 }})
  }
}
</script>

<style lang="css" scoped>

</style>