<script setup lang="ts">
const props = defineProps({
  text: { type: String, required: true },
});
</script>

<template>
  <p class="tile-name">{{ text }}</p>

</template>

<style scoped lang="scss">
.tile-name {
  font-size: 0.95rem;
  font-weight: 700;
}
</style>