<script setup lang="ts">

</script>

<template>
<div class="sep-main">
  <div class="sep-col">
    <slot name="col1"></slot>
  </div>
  <div class="sep-col">
    <slot name="col2"></slot>
  </div>
</div>
</template>

<style scoped lang="scss">
.sep-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sep-col {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
</style>