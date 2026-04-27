<template>
  <div class="app-layout">
    <AppHeader
      :title="currentPage.title"
      :subtitle="currentPage.subtitle"
      :show-notif="currentPage.showNotif"
      @notif="store.toggleAlertPanel"
    />

    <main class="layout-main">
      <slot />
    </main>

    <AppNavBottom />
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { useAppStore } from '../store/app'
import { computed, ref } from 'vue'
import AppHeader from "../components/core/AppHeader.vue";
import AppNavBottom from "../components/core/AppNavBottom.vue";

const route = useRoute()
const store = useAppStore()

const pages: Record<string, { title: string; subtitle?: string; showNotif?: boolean }> = {
  '/':         { title: 'Bonjour, Julien 👋', showNotif: true },
  '/meteo':    { title: 'Météo', subtitle: 'Yvetot — Normandie' },
  '/capteurs': { title: 'Capteurs & données', subtitle: 'Parcelle A — dernières 24h' },
  '/parametre':    { title: 'Paramètre & Comptes ', subtitle: 'Données personnelles et configuration' },
}


const currentPage = computed(() => pages[route.path] ?? { title: 'AgriSense' })
</script>

<style lang="scss">
.app-layout {
  min-height: 100vh;
  background: var(--bg-primary);
  position: relative;
}

.layout-main {
  // Content sits under fixed header + status bar + nav
}
</style>
