<script setup lang="ts">
import { useAppStore } from '../../../store/app'
import SmallLabel from "../Label/SmallLabel.vue";
import BoldTitleLabel from "../Label/BoldTitleLabel.vue";
const store = useAppStore()

</script>

<template>
  <div class="alert-banner animate-fade-up" v-if="store.unreadAlerts.length">
    <span class="alert-icon">⚠️</span>
    <div>
      <BoldTitleLabel class="alert-title" :text="store.unreadAlerts[0].title"/>
      <SmallLabel class="alert-msg" :text="store.unreadAlerts[0].message"/>
    </div>
  </div>
</template>

<style scoped lang="scss">
.alert-icon {
  font-size: 1rem;
  margin-top: 1px;
  flex-shrink: 0;

}
.alert-title {
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--alert-warning-text);
}
.alert-msg {
  color: var(--alert-warning-text);
  margin-top: 2px;
  opacity: 0.85;
}


</style>