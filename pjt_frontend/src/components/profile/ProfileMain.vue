<template>
  <div>
    <div id="joinlist">
      <div id="title">가입상품</div>
      <div id="prdt-content">
        <div v-for="product in joinproducts">
          {{ product.fin_prdt_nm }}
        </div>
      </div>
    </div>
    <div id="rate-graph">
      <div v-if="graph">
        <img :src="graph.data" alt="intr_rate graph">
      </div>
      <div v-else>
        <span>가입한 상품이 없습니다</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { onBeforeMount, ref, watch } from 'vue';

const userStore = useUserStore()

const joinproducts = ref('')
const graph = ref(null)

const getGraph = function () {
  axios({
    method: 'post',
    url: `${userStore.URL}/finance/product/graph/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: {
      'joinproducts': joinproducts.value,
    },
  })
    .then((res) => {
      console.log("GRAPH LOAD SUCCESS")
      console.log(res.data)
      graph.value = res.data
    })
    .catch((err) => {
      console.log("GRAPH LOAD FAILED")
      console.log(err.response.data)
    })
}

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
      joinproducts.value = res.data
      console.log(joinproducts.value)
      if (res.data.length > 0) {
        getGraph()
      }
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