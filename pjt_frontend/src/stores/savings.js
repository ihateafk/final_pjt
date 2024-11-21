import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useSavingsStore = defineStore('savings', () => {
  const savingsItem = ref(null)
  const savingsOptionList = ref([])
  return {
    savingsItem,
    savingsOptionList
  }
}, {persist : true},)
