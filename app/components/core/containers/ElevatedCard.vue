<script setup lang="ts">
const props = defineProps({
  text: { type: String, default: "" },
});
</script>

<template>
  <div class="card-elevated  animate-fade-up">
    <p class="section-label">{{ text }}</p>
    <slot></slot>
  </div>

</template>

<style scoped lang="scss">

</style>