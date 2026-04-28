<script setup lang="ts">
const props = defineProps({
  ele: { type: Object, required: true },
});
</script>

<template>
  <span class="temp-value">{{ ele.temp }}°</span>
  <div class="weather-meta">
    <p class="weather-desc text-more-blue">{{ ele.desc }}</p>
    <p class="weather-detail text-secondary">
      <span>Vent {{ ele.wind }}km/h</span>
    </p>
    <p class="weather-detail text-more-blue">
      Humidité {{ ele.humidity }}%
    </p>
  </div>
</template>

<style scoped lang="scss">

.temp-value {
  font-size: 3.5rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  color: #1a2a4a;
  line-height: 1;
}

.weather-desc {
  font-size: 1rem;
  font-weight: 600;
}

.weather-detail {
  font-size: 0.875rem;
  font-weight: 500;
  color: #4f6895;
}


</style>