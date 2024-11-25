<template>
  <div class="mb-3">
    <div class="small text-dark mb-1">{{ data.key }}</div>
    <div class="form-control bg-white text-secondary border">
      {{ data.value }}
    </div>
  </div>
</template>

<script setup>
defineProps({
  data: Object,
})
</script>

<style scoped>
.form-control {
  height: auto;
  min-height: 44px;
  font-size: 0.875rem;
  padding: 0.75rem;
  cursor: default;
}

.form-control:focus {
  box-shadow: none;
  border-color: #dee2e6;
}
</style>