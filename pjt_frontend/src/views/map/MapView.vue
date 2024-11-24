<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-3">
        <div class="sidebar">
          <h4>은행 지도</h4>
          <MapSearch @selected="handleSearchSelected" />
        </div>
      </div>
      <div class="col-md-9">
        <MapObject :searchData="searchData" />
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
.container {
  margin-top: 20px;
}

.sidebar {
  padding: 20px;
}

.sidebar h4 {
  margin-bottom: 20px;
}

@media (max-width: 767px) {
  .col-md-3 {
    margin-bottom: 20px;
  }
}
</style>