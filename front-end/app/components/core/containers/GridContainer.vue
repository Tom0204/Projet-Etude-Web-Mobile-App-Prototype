<script setup lang="ts">

</script>

<template>
  <div class="grid">
    <slot></slot>
  </div>
</template>

<style scoped lang="scss">
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
</style>