<template>
  <nav class="app-nav">
    <NuxtLink
      v-for="tab in tabs"
      :key="tab.to"
      :to="tab.to"
      class="nav-item"
      :class="{ 'nav-item--active': route.path === tab.to }"
    >
      <div class="nav-icon">
        <component :is="tab.icon" :size="22" :stroke-width="route.path === tab.to ? 2.5 : 1.8" />
      </div>
      <span class="nav-label">{{ tab.label }}</span>
    </NuxtLink>
  </nav>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { BarChart2, Cloud, Activity, AlignJustify   } from 'lucide-vue-next'

const route = useRoute()

const tabs = [
  { to: '/',         label: 'Accueil',  icon: BarChart2 },
  { to: '/meteo',    label: 'Météo',    icon: Cloud },
  { to: '/capteurs', label: 'Capteurs', icon: Activity },
  { to: '/parametre',    label: 'Paramètre',    icon: AlignJustify  },
]
</script>

<style scoped lang="scss">
.app-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 100;
  height: var(--nav-height);
  background: rgba(26, 26, 26, 0.92);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid var(--border-subtle);
  display: flex;
  align-items: stretch;
  padding-bottom: env(safe-area-inset-bottom, 0px);
}

.nav-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  text-decoration: none;
  color: var(--text-muted);
  transition: color 0.2s ease;
  -webkit-tap-highlight-color: transparent;

  &--active {
    color: var(--accent-blue);

    .nav-icon {
      background: rgba(96, 165, 250, 0.12);
    }
  }

  &:active {
    opacity: 0.7;
  }
}

.nav-icon {
  width: 40px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 14px;
  transition: background 0.2s ease;
}

.nav-label {
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}
</style>
