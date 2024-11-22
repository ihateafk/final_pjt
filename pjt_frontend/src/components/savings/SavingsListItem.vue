<template>
  <RouterLink
    :to="{ name: 'savingsDetail', params : {id : savings.fin_co_no} }"
    @click="savingsItemchange"
  >
    <div>
      <div>
        <div>
          <h2>{{ savings.kor_co_nm }}</h2>
          <p>{{ savings.fin_prdt_nm }}</p>
        </div>
        <div>
          <div>
            <span>6개월</span>
            <span>{{ getInterestRate(6) }}%</span>
          </div>
          <div>
            <span>12개월</span>
            <span>{{ getInterestRate(12) }}%</span>
          </div>
          <div>
            <span>24개월</span>
            <span>{{ getInterestRate(24) }}%</span>
          </div>
        </div>
      </div>
    </div>
  </RouterLink>
</template>

<script setup>
  import { useSavingsStore } from '@/stores/savings';
  import { defineProps } from 'vue';
  import { RouterLink } from 'vue-router';

  const store = useSavingsStore()

  const props = defineProps({
    savings: {
      type: Object
    },
    optionList: {
      type: Array
    }
  })

  const savingsItemchange = function () {
    store.savingsItem = props.savings
    const options = props.optionList.filter(opt => props.savings.fin_prdt_cd === opt.fin_prdt_cd)
    store.savingsOptionList = options
  }

  const getInterestRate = (month) => {
    const option = props.optionList?.find(opt => 
      opt.save_trm === month.toString() &&
      opt.fin_prdt_cd === props.savings.fin_prdt_cd
    )
    return option ? option.intr_rate : '-'
  }
</script>

<style scoped>

</style>