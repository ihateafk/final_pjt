<template>
  <div>
    <div>
      <RouterLink :to="{name:'deposit'}">돌아가기</RouterLink>
    </div>
    <div id="body">
      <div id="content">
        <div id="title">
          <div id="nm">
            <div id="co_nm">
              <p>회사명 : {{store.savingsItem.kor_co_nm}}</p>
            </div>
            <div id="prdt_nm">
              <p>금융 상품명 : {{store.savingsItem.fin_prdt_nm}}</p>
            </div>
          </div>
          <div id="favorbtn">
            <button @click="addProduct('favorite')">관심상품 등록</button>
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
          <p>만기 후 이자율 : {{store.savingsItem.mtrt_int}}</p>
          <p>가입 방법 : {{store.savingsItem.join_way}}</p>
          <p>우대 조건 : {{ store.savingsItem.spcl_cnd }}</p>
          <p>가입 대상 : {{ store.savingsItem.join_member }}</p>
          <p>유의 사항 : {{ store.savingsItem.etc_note }}</p>
        </div>
      </div>
    </div>
    <div>
      <button @click="addProduct('join')">가입한 상품 추가하기</button>
    </div>
  </div>
</template>

<script setup>
  import { RouterLink } from 'vue-router';
  import { useSavingsStore } from '@/stores/savings';
  import { ref } from 'vue';
  import { useUserStore } from '@/stores/user';
  import axios from 'axios';

  const store = useSavingsStore()
  const userStore = useUserStore()

  const max_intr_rate = ref(0)
  const min_intr_rate = ref(100)

  store.savingsOptionList.forEach((option) => {
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
        base: store.savingsItem,
        options: store.savingsOptionList,
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

</style>