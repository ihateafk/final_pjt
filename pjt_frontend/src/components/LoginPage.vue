<template>
  <div>
    <div>
      HomeLogo
    </div>
    <div id="loginbox">
      <div id="formbox">
        <form @submit.prevent="login">
          <div>
            <label for="email">Email</label>
            <input type="text" id="email" v-model.trim="email">
          </div>
          <div>
            <label for="pw">Password</label>
            <input type="text" id="pw" v-model.trim="pw">
          </div>
          <div>
            <input type="submit" value="Sign In">
          </div>
        </form>
      </div>
      <div id="linkbox">
        <div>
          <a href=""></a>
        </div>
        <div>
          <a href=""></a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useDepositStore } from '@/stores/deposit';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const userStore = useUserStore()
const router = useRouter()

const email = ref('')
const pw = ref('')

const login = function () {
  axios({
    method: 'post',
    url: `${userStore.URL}/accounts/login/`,
    data: {
      email: email.value,
      password: pw.value,
    }
  })
    .then((res) => {
      userStore.token = res.data
      console.log("LOGIN SUCCESS")
      router.push({ name: 'home' })
    })
    .catch((err) => {
      console.log('LOGIN FAILED')
      console.log(err.response.data)
    })
}
</script>

<style scoped>

</style>