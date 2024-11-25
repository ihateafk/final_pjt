<template>
  <div class="container p-4">
    <h5 class="mb-4">개인 정보 수정</h5>
    
    <div class="row g-3">
      <!-- Email Field -->
      <div class="col-12 col-md-6">
        <div class="small text-dark mb-1">Email</div>
        <input 
          type="email" 
          class="form-control bg-light" 
          :value="email" 
          disabled
        >
      </div>

      <!-- Password Change Button -->
      <div class="col-12 col-md-6">
        <div class="small text-dark mb-1">Password</div>
        <button 
          @click="goToPwChange" 
          class="form-control text-primary border d-flex align-items-center"
        >
          변경하기
        </button>
      </div>

      <!-- Name Field -->
      <div class="col-12 col-md-6">
        <div class="small text-dark mb-1">Name</div>
        <input 
          type="text" 
          class="form-control" 
          v-model.trim="name"
        >
      </div>

      <!-- Age Field -->
      <div class="col-12 col-md-6">
        <div class="small text-dark mb-1">Age</div>
        <input 
          type="number" 
          class="form-control" 
          v-model="age"
        >
      </div>

      <!-- Gender Field -->
      <div class="col-12 col-md-6">
        <div class="small text-dark mb-1">Gender</div>
        <input 
          type="text" 
          class="form-control" 
          v-model.trim="gender"
        >
      </div>

      <!-- Birthday Field -->
      <div class="col-12 col-md-6">
        <div class="small text-dark mb-1">Birthday</div>
        <input 
          type="date" 
          class="form-control" 
          v-model="birthday"
        >
      </div>

      <!-- Address Field -->
      <div class="col-12">
        <div class="small text-dark mb-1">Address</div>
        <input 
          type="text" 
          class="form-control" 
          v-model.trim="address"
        >
      </div>

      <!-- Job Field -->
      <div class="col-12 col-md-6">
        <div class="small text-dark mb-1">Job</div>
        <input 
          type="text" 
          class="form-control" 
          v-model.trim="job"
        >
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="d-flex gap-2 justify-content-center mt-4">
      <button 
        @click="changeConfirm(true)" 
        class="btn btn-primary px-4"
      >
        수정하기
      </button>
      <button 
        @click="changeConfirm(false)" 
        class="btn btn-secondary px-4"
      >
        취소
      </button>
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
</style>