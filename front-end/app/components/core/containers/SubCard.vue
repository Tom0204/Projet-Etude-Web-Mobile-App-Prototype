<script setup lang="ts">
const props = defineProps({
  text: { type: String, required: true },
});
</script>

<template>
  <div class="sub-card">
    <p class="sub-label">{{ text }}</p>
    <slot/>
  </div>
</template>

<style scoped lang="scss">
.sub-card {
  background: var(--bg-elevated);
  border-radius: var(--radius-sm);
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sub-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}
</style>