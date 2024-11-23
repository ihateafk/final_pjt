<template>
  <div>
    <div id="title">
      <span>PASSWORD 변경</span>
    </div>
    <div id="body">
      <div>
        <label for="old_password">현재 비밀번호</label>
        <input type="password" id="old_password" v-model.trim="old_password">
      </div>
      <div>
        <label for="new_password1">새 비밀번호</label>
        <input type="password" id="new_password1" v-model.trim="new_password1">
      </div>
      <div>
        <label for="new_password2">새 비밀번호 확인</label>
        <input type="password" id="new_password2" v-model.trim="new_password2">
      </div>
    </div>
    <div id="botton">
      <button @click="pwChangeConfirm">변경하기</button>
      <button @click="$router.back">취소</button>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const userStore = useUserStore()
const router = useRouter()

const old_password = ref('')
const new_password1 = ref('')
const new_password2 = ref('')

const pwChangeConfirm = function () {
  axios({
    method: 'post',
    url: `${userStore.URL}/accounts/password/change/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    },
    data: {
      old_password: old_password.value,
      new_password1: new_password1.value,
      new_password2: new_password2.value,
    }
  })
    .then((res) => {
      console.log('PW CHANGE SUCCESS')
      console.log(res.data)
      old_password.value = ''
      new_password1.value = ''
      new_password2.value = ''
      alert('성공적으로 변경되었습니다.')
      router.back()
    })
    .catch((err) => {
      console.log('PW CHANGE FAILED')
      console.log(err)
      alert('유효한 비밀번호가 아닙니다.')
      old_password.value = ''
      new_password1.value = ''
      new_password2.value = ''
    })
}
</script>

<style lang="css" scoped>

</style>