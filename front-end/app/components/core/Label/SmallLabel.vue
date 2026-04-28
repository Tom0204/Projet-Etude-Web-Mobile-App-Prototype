<script setup lang="ts">
const props = defineProps({
  text: { type: String, required: true },
});
</script>

<template>
  <p class="summary-label">{{ text }}</p>
</template>

<style scoped lang="scss">
.summary-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}
</style>