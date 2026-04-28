<script setup lang="ts">
const props = defineProps({
  level: { type: Number, required: true },
  text: { type: String , default: "null" },
});
  const levelGrade = ["badge--low", "badge--stable", "badge--neutral", "badge--medium","badge--high"];

</script>

<template>
  <span class="badge "  :class="levelGrade[level]">{{ text }}</span>
</template>

<style scoped lang="scss">

</style>