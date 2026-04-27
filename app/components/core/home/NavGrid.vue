<script setup lang="ts">

import NavCard from "../card/NavCard.vue";
const props = defineProps({
  items : { type: Array<Object>, required: true },
})
</script>

<template>
  <div>
    <p class="section-label">Navigation</p>
    <div class="nav-grid">
      <NavCard  v-for="(nav ,index) in items"
                :key="`nav-${index}`"
                class="nav-tile card"
                :nav="nav"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.nav-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

</style>