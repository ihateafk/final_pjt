<template>
  <div>
    <h2 class="text-xl mb-4">지역 검색</h2>

    <div class="space-y-4">
      <div class="flex items-center gap-4">
        <label class="min-w-24">광역시/도:</label>
        <select 
          v-model="selectedProvince" 
          class="border p-2 rounded min-w-48"
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

      <div class="flex items-center gap-4">
        <label class="min-w-24">시/군/구:</label>
        <select 
          v-model="selectedCity"
          class="border p-2 rounded min-w-48"
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

      <div class="flex items-center gap-4">
        <label class="min-w-24">은행명:</label>
        <select 
          v-model="selectedBank" 
          class="border p-2 rounded min-w-48"
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
    </div>
    <button @click="handleSearch">
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