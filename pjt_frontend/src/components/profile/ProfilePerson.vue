<template>
  <div>
    <div id="title">개인정보</div>
    <div id="body">
      <div v-if="userdata">
        <PersonInfoItem
          v-for="(value, key) in userdata"
          :key="key"
          :data="{ key: key, value: value }"
        />
      </div>
    </div>
    <div id="bottom">
      <!-- <button @click="goToChangePage">수정하기</button> -->
    </div>
  </div>
</template>

<script setup>
import PersonInfoItem from '@/components/profile/PersonInfoItem.vue'
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { onBeforeMount, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const userStore = useUserStore()

const userdata = ref(null)

const goToChangePage = function () {
  router.push({ name: 'infochange' })
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
      userdata.value = res.data
    })
    .catch((err) => {
      console.log("LOAD FAILED")
      console.log(err.response.data)
    })
})
</script>

<style lang="css" scoped>

</style>