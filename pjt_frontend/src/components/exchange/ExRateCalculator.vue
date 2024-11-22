<template>
  <div class="exchange-container">
    <div class="exchange-input">
      <p>
        <label>변환 전:</label>
        <select v-model="originCountry">
          <option v-for="code in countryCodes" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
      </p>
      <p>
        <label>가격 : </label>
        <input type="number" v-model="originValue">
      </p>
      <p>
        <label>변환 후: </label>
        <select v-model="changeCountry">
          <option v-for="code in countryCodes" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
      </p>
    </div>
    
    <div class="exchange-result">
      <p>{{ exchangeResult }} {{ changeCountry }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import axios from 'axios';

const originCountry = ref('KRW')
const changeCountry = ref('USD')
const originValue = ref(0)
const exchangeResult = ref(0)
const changeRate = ref(0)
const countryCodes = ref([])

// API에서 지원하는 모든 통화 코드 가져오기
const getCountryCodes = async () => {
  try {
    const response = await axios.get(
      `https://cors-anywhere.herokuapp.com/https://v6.exchangerate-api.com/v6/${import.meta.env.VITE_APP_EXCHANGERATE_API_KEY}/latest/USD`
    )
    // conversion_rates 객체의 키들을 countryCodes 배열에 저장
    countryCodes.value = Object.keys(response.data.conversion_rates).sort()
  } catch (err) {
    console.error('통화 코드 가져오기 실패:', err)
  }
}

const getRates = async () => {
  try {
    const response = await axios.get(
      `https://cors-anywhere.herokuapp.com/https://v6.exchangerate-api.com/v6/${import.meta.env.VITE_APP_EXCHANGERATE_API_KEY}/latest/${originCountry.value}`
    )
    changeRate.value = response.data.conversion_rates[changeCountry.value]
    calculateResult()
  } catch (err) {
    console.error('환율 가져오기 실패:', err)
  }
}

const calculateResult = () => {
  if (changeRate.value) {
    exchangeResult.value = (originValue.value * changeRate.value).toFixed(2)
  }
}

// 나라 코드나 금액이 변경될 때마다 자동 계산
watch([originCountry, changeCountry], () => {
  getRates()
})

watch(originValue, () => {
  calculateResult()
})

onMounted(() => {
  getCountryCodes()
  getRates()
})
</script>

<style scoped>
.exchange-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.exchange-input {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.exchange-input p {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0;
}

label {
  margin-right: 10px;
  width: 60px;
}

select, input {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
  width: 200px;
}

input[type="number"] {
  width: 200px;
}

.exchange-result {
  margin-top: 20px;
  padding: 15px;
  background-color: #f5f5f5;
  border-radius: 4px;
  text-align: center;
}
</style>