import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useDepositStore = defineStore('deposit', () => {
  const depositItem = ref(null)
  const depositOptionList = ref([])
  return {
    depositItem,
    depositOptionList
  }
}, {persist : true},)
