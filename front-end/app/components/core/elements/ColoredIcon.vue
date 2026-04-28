<script setup lang="ts">
import * as vue from "vue";
import {LucideProps} from "lucide-vue-next";

const props = defineProps({
  icon: { type: Object, required: true },
  color: { type: String, default: "", required: true },

});
</script>

<template>
  <div class="colored-icon" :style="{ background: color }">
    <component :is="icon" :size="22" color="#fff" :stroke-width="2" />
  </div>
</template>

<style scoped lang="scss">
.colored-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.9;
}
</style>