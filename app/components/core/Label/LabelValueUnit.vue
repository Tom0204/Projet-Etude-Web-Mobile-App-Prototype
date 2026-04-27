<script setup lang="ts">
const props = defineProps({
  value: { type: Number, required: true },
  unit: { type: String, default: "" },
});
</script>

<template>
  <p class="summary-value">{{ value }}<span class="summary-unit">{{ unit }}</span></p>
</template>

<style scoped lang="scss">
.summary-value {
  font-size: 1.8rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1;
}

.summary-unit {
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-secondary);
  margin-left: 2px;
}
</style>