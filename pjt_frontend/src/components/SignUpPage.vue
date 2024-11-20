<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signup">
      <div>
        <label for="username">username</label>
        <input type="text" id="username" v-model.trim="username">
      </div>

      <div>
        <label for="password1">password1</label>
        <input type="text" id="password1" v-model.trim="password1">
      </div>

      <div>
        <label for="password2">password2</label>
        <input type="text" id="password2" v-model.trim="password2">

      </div>

      <div>
        <label for="name">name</label>
        <input type="text" id="name" v-model.trim="name">
      </div>

      <div>
        <label for="email">email</label>
        <input type="text" id="email" v-model.trim="email">
      </div>

      <div>
        <label for="age">age</label>
        <input type="text" id="age" v-model.trim="age">
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
        <label for="job_id">job_id</label>
        <input type="text" id="job_id" v-model.trim="job_id">
      </div>

      <input type="submit" value="가입하기">
    </form>

    <div>
      {{ error }}
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { computed, ref } from 'vue';


const username = ref('')
const password1 = ref('')
const password2 = ref('')
const name = ref('')
const email = ref('')
const age = ref('')
const gender = ref('')
const birthday = ref('')
const address = ref('')
const job_id = ref('')

const error = ref(null)

const signup = function () {
  console.log({
    // username: username.value,
    password1: password1.value,
    password2: password2.value,
    name: name.value,
    email: email.value,
    age: Number(age.value),
    gender: gender.value,
    birthday: birthday.value,
    address: address.value,
    job_id: Number(job_id.value),
  });

  axios({
    method: 'POST',
    url: 'http://127.0.0.1:8000/accounts/signup/',
    data: {
      // username: username.value,
      password1: password1.value,
      password2: password2.value,
      name: name.value,
      email: email.value,
      age: Number(age.value),
      gender: gender.value,
      birthday: birthday.value,
      address: address.value,
      job_id: Number(job_id.value),
    }
  })
    .then((res) => {
      console.log("SUCCESS")
      console.log(res.data)
    })
    .catch((err) => {
      console.log("FAIL")
      console.log("Sent Data:", {
        // username: username.value,
        password1: password1.value,
        password2: password2.value,
        name: name.value,
        email: email.value,
        age: typeof(Number(age.value)), // 변환된 값 확인
        gender: gender.value,
        birthday: birthday.value,
        address: address.value,
        job_id: typeof(Number(job_id.value)),
      });
      error.value = err.response.data
    })
}

computed(() => error.value)
</script>

<style lang="css" scoped>

</style>