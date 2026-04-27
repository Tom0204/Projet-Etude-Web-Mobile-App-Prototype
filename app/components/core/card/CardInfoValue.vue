<script setup lang="ts">
import LabelValueUnit from "../Label/LabelValueUnit.vue";
import ClassicBadge from "../Label/ClassicBadge.vue";
import SmallLabel from "../Label/SmallLabel.vue";

const props = defineProps({
  eleValue: { type: Object, required: true },
});
</script>

<template>
  <div class="card summary-card animate-fade-up delay-1">
    <SmallLabel :text="eleValue.label"/>
    <LabelValueUnit :value="eleValue.value" :unit="eleValue.unit"/>
    <ClassicBadge :level="eleValue.badgeLevel" :text="eleValue.badgeText"/>
  </div>
</template>

<style scoped lang="scss">
.summary-card {
  display: flex;
  flex-direction: column;
  gap: 6px;
}



</style>