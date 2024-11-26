<template>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-12 col-md-8 col-lg-6">
        <div class="exchange-container p-4">
          <div class="exchange-header mb-4">
            <h4 class="text-center">환율 계산기</h4>
          </div>
          <div class="exchange-input">
            <div class="form-group row">
              <label for="originCountry" class="col-3 col-form-label">변환 전</label>
              <div class="col-9">
                <select class="form-control" v-model="originCountry">
                  <option v-for="code in countryCodes" :key="code" :value="code">
                    {{ code }}
                  </option>
                </select>
              </div>
            </div>
            <div class="form-group row">
              <label for="originValue" class="col-3 col-form-label">가격</label>
              <div class="col-9">
                <input 
                  type="number" 
                  class="form-control" 
                  v-model="originValue"
                  min="0" 
                  step="1" 
                  @input="validateInput"
                  @keypress="preventNonNumber"
                >
              </div>
            </div>
            <div class="form-group row">
              <label for="changeCountry" class="col-3 col-form-label">변환 후</label>
              <div class="col-9">
                <select class="form-control" v-model="changeCountry">
                  <option v-for="code in countryCodes" :key="code" :value="code">
                    {{ code }}
                  </option>
                </select>
              </div>
            </div>
          </div>
          
          <div class="exchange-result text-center display-5 bg-light p-3 rounded">
            {{ exchangeResult }} {{ changeCountry }}
          </div>
        </div>
      </div>
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
const originVlue = ref('')

const getCountryCodes = async () => {
  try {
    const response = await axios.get(
      `https://cors-anywhere.herokuapp.com/https://v6.exchangerate-api.com/v6/${import.meta.env.VITE_APP_EXCHANGERATE_API_KEY}/latest/USD`
    )
    countryCodes.value = Object.keys(response.data.conversion_rates).sort()
  } catch (err) {
    console.error('통화 코드 가져오기 실패:', err)
  }
}

const validateInput = (event) => {
  let value = event.target.value
  
  if (value < 0) {
    originValue.value = ''
    return
  }
  
  if (value.includes('.')) {
    originValue.value = Math.floor(value)
    return
  }
  
  if (isNaN(value)) {
    originValue.value = ''
    return
  }
  
  originValue.value = Math.floor(Number(value))
}

const preventNonNumber = (event) => {
  if (!/^\d*$/.test(event.key)) {
    event.preventDefault()
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

input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0; 
}

input[type=number] {
  -moz-appearance: textfield;
}
</style>