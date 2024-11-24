<template>
  <div>
    <h5 class="mb-4">지역 검색</h5>

    <div class="mb-3">
      <label class="form-label">광역시/도</label>
      <select 
        v-model="selectedProvince" 
        class="form-select"
      >
        <option value="" disabled>선택하세요</option>
        <option 
          v-for="province in mapStore.mapInfo" 
          :key="province.id" 
          :value="province.prov"
        >
          {{ province.prov }}
        </option>
      </select>
    </div>

    <div class="mb-3">
      <label class="form-label">시/군/구</label>
      <select 
        v-model="selectedCity"
        class="form-select"
        :disabled="!selectedProvince"
      >
        <option value="" disabled>선택하세요</option>
        <option 
          v-for="city in cityList" 
          :key="city" 
          :value="city"
        >
          {{ city }}
        </option>
      </select>
    </div>

    <div class="mb-4">
      <label class="form-label">은행명</label>
      <select 
        v-model="selectedBank" 
        class="form-select"
      >
        <option value="" disabled>선택하세요</option>
        <option 
          v-for="bank in mapStore.bankInfo" 
          :key="bank" 
          :value="bank"
        >
          {{ bank }}
        </option>
      </select>
    </div>

    <button class="btn btn-primary w-100 text-center" @click="handleSearch">
      검색
    </button>
  </div>
</template>

<script setup>
import { useMapStore } from '@/stores/map';
import { ref, computed, watch } from 'vue';

const mapStore = useMapStore();

const selectedProvince = ref('');
const selectedCity = ref('');
const selectedBank = ref('');

const cityList = computed(() => {
  if (!selectedProvince.value) return [];
  
  const province = mapStore.mapInfo.find(
    item => item.prov === selectedProvince.value
  );
  return province ? province.city : [];
});

// 광역시/도가 변경되면 선택된 시/군/구를 초기화
watch(selectedProvince, () => {
  selectedCity.value = '';
});

const emit = defineEmits(['selected']);

// 검색 버튼 클릭 핸들러
const handleSearch = () => {
  emit('selected', {
    province: selectedProvince.value,
    city: selectedCity.value,
    bank: selectedBank.value
  });
};
</script>