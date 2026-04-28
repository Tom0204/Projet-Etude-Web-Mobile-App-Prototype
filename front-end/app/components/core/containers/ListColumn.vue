<template>
  <div class="forecast-list">
    <div
        v-for="(ele, i) in elements"
        :key="i"
        class="forecast-row"
        :class="{ 'forecast-row--selected': i === selected && selected != -2 }"
    >
      <slot :ele_cont="ele" :index="i"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  elements: { type: Array, required: true },
  selected: { type: Number, default: -2 },
});
</script>

<style scoped lang="scss">
.forecast-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.forecast-row {
  display: flex;
  align-items: center;
  padding: 10px 4px;
  gap: 12px;
  border-radius: 8px;
  transition: background 0.2s;

  &--selected {
    background: rgba(255,255,255,0.04);
  }
}
</style>