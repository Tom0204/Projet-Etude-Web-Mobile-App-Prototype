<template>
  <div class="page-content">
    <!-- Parcelle selector -->
    <div class="parcelle-tabs animate-fade-up">
      <button
        v-for="p in store.parcelles"
        :key="p"
        class="parcelle-tab"
        :class="{ 'parcelle-tab--active': store.parcelleActive === p }"
        @click="store.setParcelleActive(p)"
      >
        {{ p }}
      </button>
    </div>

    <SensorCharts />
  </div>
</template>

<script setup lang="ts">
import { useAppStore } from '../store/app'

import {definePageMeta} from "../../.nuxt/imports";
import SensorCharts from "../components/contexts/SensorCharts.vue";


definePageMeta({ layout: 'default' })
const store = useAppStore()
</script>

<style scoped lang="scss">
.parcelle-tabs {
  display: flex;
  gap: 8px;
}

.parcelle-tab {
  flex: 1;
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  color: var(--text-secondary);
  font-size: 0.85rem;
  font-weight: 600;
  font-family: var(--font-body);
  cursor: pointer;
  transition: all 0.2s ease;

  &--active {
    background: var(--accent-blue);
    color: #fff;
    border-color: var(--accent-blue);
  }
}
</style>
