<template>
  <div class="container-fluid my-4">
    <div id="title" class="fw-bold fs-4 mb-3">개인정보</div>
    <div id="body" class="border rounded-3 p-4 shadow-sm">
      <div v-if="userStore.userdata">
        <PersonInfoItem
          v-for="(value, key) in userStore.userdata"
          :key="key"
          :data="{ key: key, value: value }"
        />
      </div>
    </div>
    <div id="bottom" class="d-flex justify-content-center mt-3">
      <button class="btn btn-primary" @click="goToChangeInfo">개인 정보 수정</button>
    </div>
  </div>
</template>

<script setup>
import PersonInfoItem from '@/components/profile/PersonInfoItem.vue'
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { computed, onBeforeMount, ref } from 'vue';
import { useRouter } from 'vue-router';


const router = useRouter()
const userStore = useUserStore()


const goToChangeInfo = function () {
  router.push({
    name: 'infochange'
  })
}

onBeforeMount(() => {
  axios({
    method: 'get',
    url: `${userStore.URL}/accounts/profile/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log("LOAD SUCCESS")
      userStore.userdata = res.data
    })
    .catch((err) => {
      console.log("LOAD FAILED")
      console.log(err.response.data)
    })
})
</script>

<style lang="css" scoped>

</style>