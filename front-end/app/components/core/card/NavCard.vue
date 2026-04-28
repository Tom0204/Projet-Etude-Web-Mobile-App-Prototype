<script setup lang="ts">
import SmallLabel from "../Label/SmallLabel.vue";
import BoldTitleLabel from "../Label/BoldTitleLabel.vue";
import ColoredIcon from "../elements/ColoredIcon.vue";

const props = defineProps({
  nav: { type: Object, required: true },
});
</script>

<template>
  <NuxtLink :to="nav.link">
    <ColoredIcon :color="nav.color" :icon="nav.icon"/>
    <div>
      <BoldTitleLabel :text="nav.label" />
      <SmallLabel :text="nav.sub" />
    </div>
  </NuxtLink>
</template>

<style scoped lang="scss">

.nav-tile {
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
  transition: transform 0.15s ease, background 0.2s;

  &:active {
    transform: scale(0.97);
  }
}





</style>