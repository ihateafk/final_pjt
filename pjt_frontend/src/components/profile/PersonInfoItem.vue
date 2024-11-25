<template>
  <div class="d-flex justify-content-between align-items-center py-2">
    <div id="fieldname">
      <span id="name" class="fw-bold">{{ data.key }}</span>
    </div>
    <div id="fieldvalue">
      <span id="value">{{ data.value }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  data: Object,
})
</script>

<style lang="css" scoped>
#fieldname {
  flex-basis: 30%;
  text-align: right;
  padding-right: 1rem;
}

#fieldvalue {
  flex-basis: 70%;
  font-weight: normal;
}
</style>