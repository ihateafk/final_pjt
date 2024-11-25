<template>
  <div class="container my-5">
    <div class="row">
      <div class="col-12">
        <div class="card border-0 shadow-sm">
          <div class="card-header border-0 bg-white">
            <h4 class="card-title mb-0">가입상품</h4>
          </div>
          <div class="card-body">
            <div v-for="product in joinproducts" class="mb-3 ps-2">
              <p> {{ product.fin_prdt_nm }}</p>
            </div>
            <div v-if="joinproducts.length === 0">
              <p class="text-muted">가입한 상품이 없습니다.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-4">
      <div class="col-12">
        <div class="card border-0 shadow-sm">
          <div class="card-header border-0 bg-white">
          </div>
          <div class="card-body d-flex justify-content-center align-items-center">
            <div v-if="graph">
              <img :src="graph.data" alt="intr_rate graph" class="img-fluid">
            </div>
            <div v-else>
              <p class="text-muted">가입한 상품이 없습니다.</p>
            </div>
          </div>
        </div>
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
.card {
  border-radius: 0.5rem;
}

.card-header {
  border-bottom: none;
}

.card-title {
  font-weight: 600;
}

.card-subtitle {
  color: #6c757d;
}
</style>