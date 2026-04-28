<script setup lang="ts">
import ClassicLabel from "../Label/ClassicLabel.vue";
import ClassicBadge from "../Label/ClassicBadge.vue";

const props = defineProps({
  ele_content: { type: Object, required: true },
});
</script>

<template>
    <ClassicLabel :text="ele_content.label" />
    <span class="forecast-icon">{{ ele_content.emoji }}</span>
    <span class="forecast-temps">{{ ele_content.max }}° / {{ ele_content.min }}°</span>
    <ClassicBadge class="forecast-rain" :text="`${ele_content.rain}mm`" :level="ele_content.rain > 0 ? 3 : 2"></ClassicBadge>
</template>

<style scoped lang="scss">



.forecast-icon {
  font-size: 1.1rem;
  width: 24px;
  text-align: center;
}

.forecast-temps {
  flex: 1;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
}

.forecast-rain {
  min-width: 48px;
  text-align: center;
  justify-content: center;
}
</style>