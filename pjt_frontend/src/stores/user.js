import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const URL = ref('http://127.0.0.1:8000')
  const token = ref(null)

  return {
    URL,
    token,
  }
}, {persist : true},)