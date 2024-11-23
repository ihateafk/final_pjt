<template>
  <div>
    <div id="fieldname">
      <span id="name">{{ data.key }}</span>
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

</style>