<template>
  <div class="signup-container">
    <div class="logo">
      <span>㉧</span>
    </div>
    
    <div class="signup-form">
      <form @submit.prevent="signup">
        <div class="form-row">
          <div class="form-group">
            <label for="email">이메일</label>
            <input 
              type="email" 
              id="email" 
              v-model.trim="email" 
              ref="email_input"
            >
          </div>

          <div class="form-group">
            <label for="name">이름</label>
            <input 
              type="text" 
              id="name" 
              v-model.trim="name"
            >
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="password1">비밀번호</label>
            <input 
              type="password" 
              id="password1" 
              v-model.trim="password1"
            >
          </div>

          <div class="form-group">
            <label for="password2">비밀번호 확인</label>
            <input 
              type="password" 
              id="password2" 
              v-model.trim="password2"
            >
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="age">나이</label>
            <input 
              type="number" 
              id="age" 
              v-model.trim="age"
            >
          </div>

          <div class="form-group">
            <label for="gender">성별</label>
            <input 
              type="text" 
              id="gender" 
              v-model.trim="gender"
            >
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="birthday">생일</label>
            <input 
              type="date" 
              id="birthday" 
              v-model.trim="birthday"
            >
          </div>

          <div class="form-group">
            <label for="job">직업</label>
            <input 
              type="text" 
              id="job" 
              v-model.trim="job"
            >
          </div>
        </div>

        <div class="form-group full-width">
          <label for="address">주소</label>
          <input 
            type="text" 
            id="address" 
            v-model.trim="address"
          >
        </div>

        <div>
          <input type="submit" value="가입하기">
        </div>
      </form>
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

<style scoped>
.signup-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
}

.logo {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.signup-form {
  width: 100%;
  max-width: 800px;  /* 폼의 최대 너비를 늘림 */
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-row {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.form-group {
  flex: 1;
  min-width: 0;  /* flex item 최소 너비 설정 */
}

.full-width {
  width: 100%;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-size: 0.9rem;
}

input[type="email"],
input[type="password"],
input[type="text"],
input[type="number"],
input[type="date"] {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

input::placeholder {
  color: #999;
}

input[type="submit"] {
  width: 100%;
  padding: 0.75rem;
  background-color: #87CEEB;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  margin-top: 1rem;
}

input[type="submit"]:hover {
  background-color: #78B6D1;
}
</style>