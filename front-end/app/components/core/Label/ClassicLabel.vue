<script setup lang="ts">
const props = defineProps({
  text: { type: String, required: true },
});
</script>

<template>
  <span class="c-label">
    {{ text }}
  </span>
</template>

<style scoped lang="scss">
.c-label {
  width: 36px;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-secondary);
}
</style>