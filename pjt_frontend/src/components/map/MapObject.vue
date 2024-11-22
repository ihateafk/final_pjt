<template>
  <div class="container-fluid p-0">
    <div class="position-relative" style="height: 500px;">
      <!-- 지도를 담을 영역 -->
      <div id="map" style="width: 100%; height: 100%; position: absolute; left: 0px; top: 0px;"></div>
      <!-- 검색 결과 목록 -->
      <div v-if="searchData.province && places.length > 0" 
           style="position: absolute; top: 0; right: 0; width: 350px; max-height: calc(100% - 20px); overflow-y: auto; margin: 10px; background: white; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); z-index: 2;">
        <div class="p-3">
          <ul class="list-unstyled mb-0">
            <li v-for="(place, index) in places" 
                :key="index"
                class="border-bottom p-2 cursor-pointer"
                @click="moveToPlace(place, markers[index])"
                style="cursor: pointer;">
              <h6 class="fw-bold mb-1">{{ place.place_name }}</h6>
              <p class="small text-muted mb-1">{{ place.address_name }}</p>
              <p class="small text-muted mb-0">{{ place.phone }}</p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'

const props = defineProps({
  searchData: {
    type: Object,
    required: true,
    default: () => ({
      province: '',
      city: '',
      bank: ''
    })
  }
});

const map = ref(null)
const markers = ref([])
const infowindow = ref(null)
const places = ref([])
const ps = ref(null)

// 마커를 생성하고 지도 위에 마커를 표시하는 함수
const addMarker = (position, idx, place) => {
  const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png'
  const imageSize = new window.kakao.maps.Size(36, 37)
  const imgOptions = {
    spriteSize: new window.kakao.maps.Size(36, 691),
    spriteOrigin: new window.kakao.maps.Point(0, (idx * 46) + 10),
    offset: new window.kakao.maps.Point(13, 37)
  }
  const markerImage = new window.kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions)
  const marker = new window.kakao.maps.Marker({
    position: position,
    image: markerImage
  })
  
  // 마커 클릭 이벤트 추가
  window.kakao.maps.event.addListener(marker, 'click', () => {
    moveToPlace(place, marker)
  })
  
  marker.setMap(map.value)
  markers.value.push(marker)
}

// 검색결과 항목을 Element로 반환하는 함수
const displayInfowindow = (marker, title) => {
  const content = '<div class="p-2">' + title + '</div>'
  infowindow.value.setContent(content)
  infowindow.value.open(map.value, marker)
}

// 특정 장소로 지도 이동
const moveToPlace = (place, marker) => {
  // 지도 중심을 해당 위치로 이동
  const moveLatLng = new window.kakao.maps.LatLng(place.y, place.x)
  map.value.setLevel(3) // 지도 확대 레벨 설정
  map.value.panTo(moveLatLng)
  
  // 인포윈도우 표시
  displayInfowindow(marker, place.place_name)
}

// 지도 위에 표시되고 있는 마커를 모두 제거합니다
const removeMarker = () => {
  for (let i = 0; i < markers.value.length; i++) {
    markers.value[i].setMap(null)
  }
  markers.value = []
}

// 검색결과 목록과 마커를 표출하는 함수
const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds()
    
    removeMarker()
    places.value = data

    for (let i = 0; i < data.length; i++) {
      const placePosition = new kakao.maps.LatLng(data[i].y, data[i].x)
      addMarker(placePosition, i, data[i])
      bounds.extend(placePosition)
    }

    map.value.setBounds(bounds)
  } else {
    places.value = []
    removeMarker()
  }
}

const initMap = () => {
  const container = document.getElementById('map')
  const options = {
    center: new window.kakao.maps.LatLng(37.566826, 126.9786567), // 서울 시청
    level: 3
  }

  map.value = new window.kakao.maps.Map(container, options)
  ps.value = new kakao.maps.services.Places()
  infowindow.value = new kakao.maps.InfoWindow({ zIndex: 1 })
}

const searchPlaces = () => {
  if (!props.searchData.province) return
  const keyword = `${props.searchData.province} ${props.searchData.city} ${props.searchData.bank}`.trim()
  ps.value?.keywordSearch(keyword, placesSearchCB)
}

// searchData가 변경될 때마다 검색 실행
watch(() => props.searchData, () => {
  searchPlaces()
}, { deep: true })

onMounted(() => {
  const script = document.createElement('script')
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${import.meta.env.VITE_APP_MAP_API_KEY}&autoload=false&libraries=services`
  script.onload = () => {
    window.kakao.maps.load(() => {
      initMap()
      if (props.searchData.province) {
        searchPlaces()
      }
    })
  }
  document.head.appendChild(script)
})
</script>

<style>
.cursor-pointer {
  cursor: pointer;
}

.cursor-pointer:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

#map {
  z-index: 1;
}
</style>