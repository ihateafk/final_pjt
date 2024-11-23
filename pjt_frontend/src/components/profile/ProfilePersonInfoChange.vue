<template>
  <div>
    <div id="title">개인 정보 수정</div>
    <div id="body">
      <div id="inputsection">
        <label for="email" class="title">email</label>
        <input type="email" id="email" :value="email" disabled>
      </div>
      <div id="inputsection">
        <span class="title">password</span>
        <button @click="goToPwChange">변경하기</button>
      </div>
      <div id="inputsection">
        <label for="name" class="title">name</label>
        <input type="text" id="name" v-model.trim="name">
      </div>
      <div id="inputsection">
        <label for="age" class="title">age</label>
        <input type="number" id="age" v-model="age">
      </div>
      <div id="inputsection">
        <label for="gender" class="title">gender</label>
        <input type="text" id="gender" v-model.trim="gender">
      </div>
      <div id="inputsection">
        <label for="birthday" class="title">birthday</label>
        <input type="date" id="birthday" v-model="birthday">
      </div>
      <div id="inputsection">
        <label for="address" class="title">address</label>
        <input type="text" id="address" v-model.trim="address">
      </div>
      <div id="inputsection">
        <label for="job" class="title">job</label>
        <input type="text" id="job" v-model.trim="job">
      </div>
    </div>
    <div id="bottom">
      <button @click="changeConfirm(true)">수정하기</button>
      <button @click="changeConfirm(false)">취소</button>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const email = ref(userStore.userdata.email)
const name = ref(userStore.userdata.name)
const age = ref(userStore.userdata.age)
const gender = ref(userStore.userdata.gender)
const birthday = ref(userStore.userdata.birthday)
const address = ref(userStore.userdata.address)
const job = ref(userStore.userdata.job)

const goToPwChange = function () {
  router.push({ name: 'pwchange' })
}

const changeConfirm = function (confirm) {
  if (confirm) {
    axios({
      method: 'put',
      url: `${userStore.URL}/accounts/profile/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      },
      data: {
        name: name.value,
        age: age.value,
        gender: gender.value,
        birthday: birthday.value,
        address: address.value,
        job: job.value,
      },
    })
      .then((res) => {
        console.log('CHANGE SUCCESS')
        console.log(res.data)
        alert('성공적으로 수정되었습니다.')
        router.back()
      })
      .catch((err) => {
        console.log('CHANGE FAILED')
        console.log(err.response)
        alert('유효한 입력 값이 아닙니다.')
        email.value = userStore.userdata.email
        name.value = userStore.userdata.name
        age.value = userStore.userdata.age
        gender.value = userStore.userdata.gender
        birthday.value = userStore.userdata.birthday
        address.value = userStore.userdata.address
        job.value = userStore.userdata.job
      })
  } else {
    router.back()
  }
}
</script>

<style lang="css" scoped>

</style>