<script setup lang="ts">

import CardInfoValue from "../card/CardInfoValue.vue";
const props = defineProps({
  liste: { type: Array<Record<string, any>>, required: true },
});
console.log(props.liste);
</script>

<template>
  <div>
    <p class="section-label">Résumé du jour</p>
    <div class="grid-2">
      <div v-for="(l,index) in liste" :key="`capt-list-`+ index">
        <CardInfoValue :ele-value="l" />

      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">

</style>