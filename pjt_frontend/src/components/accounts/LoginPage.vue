<template>
  <div class="login-container">
    <div class="logo">
      <span>㉧</span>
    </div>
    
    <div class="login-form">
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="email">Email</label>
          <input 
            type="text" 
            id="email"
            v-model.trim="email" 
            ref="email_input"
            placeholder="Value"
          >
        </div>
        
        <div class="form-group">
          <label for="pw">Password</label>
          <input 
            type="password" 
            id="pw"
            v-model.trim="pw"
            placeholder="Value"
          >
        </div>
        
        <div>
          <input type="submit" value="Sign In">
        </div>
        
        <div class="links">
          <a href="">Forgot password?</a>
          <RouterLink :to="{ name: 'signup' }">Don't have any account?</RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { useDepositStore } from '@/stores/deposit';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const userStore = useUserStore()
const router = useRouter()

const email = ref('')
const pw = ref('')
const email_input = ref(null)

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
      userStore.token = res.data.key
      console.log("LOGIN SUCCESS")
      router.back()
    })
    .catch((err) => {
      console.log('LOGIN FAILED')
      console.log(err.response.data)
      alert('존재하지 않은 이메일이거나 비밀번호가 틀렸습니다')
    })
}

onMounted(() => {
  email_input.value.focus()
})
</script>

<style scoped>
.login-container {
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

.login-form {
  width: 100%;
  max-width: 400px;
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-size: 0.9rem;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

input[type="text"]::placeholder,
input[type="password"]::placeholder {
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
  margin-bottom: 1rem;
}

input[type="submit"]:hover {
  background-color: #78B6D1;
}

.links {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  text-align: center;
}

.links a {
  color: #333;
  text-decoration: underline;
  font-size: 0.9rem;
}

.links a:hover {
  color: #666;
}
</style>