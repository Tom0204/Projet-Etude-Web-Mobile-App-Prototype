<script setup lang="ts">
const props = defineProps({
  icon: { type: String, required: true },
});
</script>

<template>
  <div class="weather-icon">
    <span class="weather-emoji">{{ icon }}</span>
  </div>
</template>

<style scoped lang="scss">
.weather-icon {
  .weather-emoji {
    font-size: 4rem;
    line-height: 1;
    filter: drop-shadow(0 4px 12px rgba(0,0,0,0.15));
  }
}
</style>