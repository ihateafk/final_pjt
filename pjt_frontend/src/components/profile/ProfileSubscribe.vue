<template>
  <div>
    <div id="title">가입 상품</div>
    <div id="itembox" v-if="products">
      <ProductItem
        v-for="productdata in products"
        :key="productdata['fin_prdt_cd']"
        :productdata="productdata"
        @refreshdata="getproductdata('join')"
      />
    </div>
  </div>
</template>

<script setup>
import { onBeforeMount, ref } from 'vue';
import ProductItem from './ProductItem.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const userStore = useUserStore()
const products = ref(null)

const getproductdata = function (which) {
  axios({
    method: 'get',
    url: `${userStore.URL}/finance/product/${which}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log("LOAD SUCCESS")
      console.log(res.data)
      products.value = res.data
    })
    .catch((err) => {
      console.log("LOAD FAILED")
      console.log(err.response.data)
    })
}

onBeforeMount(() => {
  getproductdata('join')
})
</script>

<style lang="css" scoped>

</style>