<script setup lang="ts">

import CardInfoValue from "../card/CardInfoValue.vue";
const props = defineProps({
  list: { type: Array<Record<string, any>>, required: true },
});
</script>

<template>
  <div>
    <p class="section-label">Résumé du jour</p>
    <div class="grid-2">
      <CardInfoValue :ele-value="list[0]"/>
      <CardInfoValue :ele-value="list[1]"/>
      <CardInfoValue :ele-value="list[2]"/>
      <CardInfoValue :ele-value="list[3]"/>
    </div>
  </div>
</template>

<style scoped lang="scss">

</style>