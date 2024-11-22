<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-4">
        <MapSearch
          @selected="handleSearchSelected"
        />
      </div>
      <div class="col-8">
        <MapObject
          :searchData="searchData"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
  import MapObject from '@/components/map/MapObject.vue';
  import MapSearch from '@/components/map/MapSearch.vue';
  import { ref } from 'vue';

  const searchData = ref({
    province: '',
    city: '',
    bank: ''
  })

  const handleSearchSelected = (data) => {
    searchData.value = data
  }

</script>

<style scoped>

</style>