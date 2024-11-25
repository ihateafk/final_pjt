<template>
  <div class="container p-4">
    <h5 class="mb-4">PASSWORD 변경</h5>
    
    <div class="row justify-content-center">
      <div class="col-12 col-md-8 col-lg-6">
        <div class="card shadow-sm">
          <div class="card-body p-4">
            <div class="mb-3">
              <div class="small text-dark mb-1">현재 비밀번호</div>
              <input 
                type="password" 
                class="form-control" 
                id="old_password" 
                v-model.trim="old_password"
                placeholder="현재 비밀번호를 입력하세요"
              >
            </div>

            <div class="mb-3">
              <div class="small text-dark mb-1">새 비밀번호</div>
              <input 
                type="password" 
                class="form-control" 
                id="new_password1" 
                v-model.trim="new_password1"
                placeholder="새 비밀번호를 입력하세요"
              >
            </div>

            <div class="mb-4">
              <div class="small text-dark mb-1">새 비밀번호 확인</div>
              <input 
                type="password" 
                class="form-control" 
                id="new_password2" 
                v-model.trim="new_password2"
                placeholder="새 비밀번호를 다시 입력하세요"
              >
            </div>

            <div class="d-flex gap-2 justify-content-center">
              <button 
                @click="pwChangeConfirm" 
                class="btn btn-primary px-4"
              >
                변경하기
              </button>
              <button 
                @click="$router.back" 
                class="btn btn-secondary px-4"
              >
                취소
              </button>
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

<style scoped>
.form-control {
  height: auto;
  min-height: 44px;
  font-size: 0.875rem;
  padding: 0.75rem;
}

.form-control:focus {
  box-shadow: none;
  border-color: #dee2e6;
}

.btn-primary {
  background-color: #3182F6;
  border-color: #3182F6;
}

.btn-primary:hover {
  background-color: #2b74db;
  border-color: #2b74db;
}

.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5c636a;
  border-color: #565e64;
}

.card {
  border: none;
}
</style>