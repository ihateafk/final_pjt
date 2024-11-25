<template>
  <div>
    <div id="homelink">
      Homelink Logo
    </div>
    <div id="signupbox">
      <div id="frombox">
        <form @submit.prevent="signup">
          <div>
            <label for="email">email</label>
            <input type="email" id="email" v-model.trim="email" ref="email_input">
          </div>

          <div>
            <label for="password1">password1</label>
            <input type="password" id="password1" v-model.trim="password1">
          </div>

          <div>
            <label for="password2">password2</label>
            <input type="password" id="password2" v-model.trim="password2">

          </div>

          <div>
            <label for="name">name</label>
            <input type="text" id="name" v-model.trim="name">
          </div>

          <div>
            <label for="age">age</label>
            <input type="number" id="age" v-model.trim="age">
          </div>

          <div>
            <label for="gender">gender</label>
            <input type="text" id="gender" v-model.trim="gender">
          </div>

          <div>
            <label for="birthday">birthday</label>
            <input type="text" id="birthday" v-model.trim="birthday">
          </div>

          <div>
            <label for="address">address</label>
            <input type="text" id="address" v-model.trim="address">
          </div>

          <div>
            <label for="job">job</label>
            <input type="text" id="job" v-model.trim="job">
          </div>

          <input type="submit" value="가입하기">
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { computed, onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';


const userStore = useUserStore()
const router = useRouter()

const password1 = ref('')
const password2 = ref('')
const name = ref('')
const email = ref('')
const age = ref('')
const gender = ref('')
const birthday = ref('')
const address = ref('')
const job = ref('')
const email_input = ref(null)


const signup = function () {
  axios({
    method: 'POST',
    url: `${userStore.URL}/accounts/signup/`,
    data: {
      email: email.value,
      password1: password1.value,
      password2: password2.value,
      name: name.value,
      age: age.value,
      gender: gender.value,
      birthday: birthday.value,
      address: address.value,
      job: job.value,
    }
  })
    .then((res) => {
      console.log("SIGNUP SUCCESS")
      router.push({ name: "login" })
    })
    .catch((err) => {
      console.log("SIGNUP FAILED")
      console.log(err.response.data)
    })
}

onMounted(() => {
  email_input.value.focus()
})
</script>

<style lang="css" scoped>

</style>