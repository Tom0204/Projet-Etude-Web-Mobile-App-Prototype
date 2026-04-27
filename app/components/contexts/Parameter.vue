<script setup lang="ts">
import { ref, onMounted, onUnmounted, h } from 'vue'
import {definePageMeta} from "../../../.nuxt/imports";
import ClassicCard from "../core/containers/ClassicCard.vue";
import ElevatedCard from "../core/containers/ElevatedCard.vue";
import SmallLabel from "../core/Label/SmallLabel.vue";
import BoldTitleLabel from "../core/Label/BoldTitleLabel.vue";
import AccountSumary from "../core/parameter/AccountSumary.vue";
import SensorCharts from "./SensorCharts.vue";
import SensorParameter from "../core/parameter/SensorParameter.vue";

definePageMeta({ layout: 'default' })

// --- Heure mise à jour ---
const currentTime = ref('')
let timer : any = null

function updateTime() {
  const now = new Date()
  currentTime.value = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`
}

onMounted(() => {
  updateTime()
  timer = setInterval(updateTime, 60000)
})

onUnmounted(() => clearInterval(timer))

// --- Icônes SVG inline (composants fonctionnels) ---

const IconBell = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('path', { d: 'M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9' }),
    h('path', { d: 'M13.73 21a2 2 0 0 1-3.46 0' }),
  ])
}
const IconSliders = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('line', { x1: 4, y1: 21, x2: 4, y2: 14 }),
    h('line', { x1: 4, y1: 10, x2: 4, y2: 3 }),
    h('line', { x1: 12, y1: 21, x2: 12, y2: 12 }),
    h('line', { x1: 12, y1: 8, x2: 12, y2: 3 }),
    h('line', { x1: 20, y1: 21, x2: 20, y2: 16 }),
    h('line', { x1: 20, y1: 12, x2: 20, y2: 3 }),
    h('line', { x1: 1, y1: 14, x2: 7, y2: 14 }),
    h('line', { x1: 9, y1: 8, x2: 15, y2: 8 }),
    h('line', { x1: 17, y1: 16, x2: 23, y2: 16 }),
  ])
}
const IconAlertTriangle = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('path', { d: 'M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z' }),
    h('line', { x1: 12, y1: 9, x2: 12, y2: 13 }),
    h('line', { x1: 12, y1: 17, x2: 12.01, y2: 17 }),
  ])
}
const IconUser = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('path', { d: 'M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2' }),
    h('circle', { cx: 12, cy: 7, r: 4 }),
  ])
}



// --- Préférences ---
const preferences = ref([
  { id: 1, name: 'Notifications', sub: 'Alertes temps réel', route: '/notifications', icon: IconBell, iconBg: 'rgba(100,160,240,0.18)', iconColor: '#64A0F0' },
  { id: 2, name: 'Unités & affichage', sub: '°C, %, mm/j', route: '/unites', icon: IconSliders, iconBg: 'rgba(120,200,120,0.18)', iconColor: '#7BC67E' },
  { id: 3, name: "Seuils d'alerte", sub: 'Humidité, température', route: '/seuils', icon: IconAlertTriangle, iconBg: 'rgba(220,100,80,0.18)', iconColor: '#E07070' },
  { id: 4, name: 'Mon compte', sub: 'Abonnement, sécurité', route: '/compte', icon: IconUser, iconBg: 'rgba(160,160,180,0.18)', iconColor: '#A0A0B8' },
])

function navigateTo(route : string) {
  // Navigation Nuxt
  // useRouter().push(route)
  console.log('Navigating to', route)
}
</script>

<template>

    <div class="update-bar">
      <span class="update-dot" />
      <span class="update-label">Mis à jour</span>
      <span class="update-time">{{ currentTime }}</span>
    </div>


      <!-- COMPTE -->
      <AccountSumary />

      <!-- CAPTEURS LIÉS -->
      <SensorParameter />

      <!-- PRÉFÉRENCES -->
      <section>
        <p class="section-label">PRÉFÉRENCES</p>
        <div class="card card--list">
          <div
              v-for="(pref, index) in preferences"
              :key="pref.id"
              class="pref-row"
              :class="{ 'pref-row--last': index === preferences.length - 1 }"
              @click="navigateTo(pref.route)"
          >
            <div class="pref-icon" :style="{ background: pref.iconBg }">
              <component :is="pref.icon" class="icon-svg" :style="{ color: pref.iconColor }" />
            </div>
            <div class="pref-info">
              <p class="pref-name">{{ pref.name }}</p>
              <p class="pref-sub">{{ pref.sub }}</p>
            </div>
            <svg class="chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
        </div>
      </section>

</template>

<style scoped lang="scss">
/* ── Tokens ── */
:root {

  --text-primary: #f5f5f5;
  --text-secondary: #8e8e93;
  --text-tertiary: #48484a;
  --green: #34c759;
  --red: #ff453a;
  --blue: #4fa0f7;
  --radius-card: 16px;
  --radius-icon: 10px;
}


/* ── Update bar ── */
.update-bar {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 6px;
  padding: 10px 20px 4px;
  font-size: 12px;
  color: var(--text-secondary);
}

.update-dot {
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 6px var(--green);
  flex-shrink: 0;
}

.update-label {
  color: var(--text-secondary);
}

.update-time {
  color: var(--text-primary);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.5px;
  padding: 2px 8px;
  border-radius: 6px;
}




/* ── Cards ── */


.card--list {
  display: flex;
  flex-direction: column;
}

.card--action {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  border: none;
  cursor: pointer;
  text-align: left;
  padding: 14px 16px;
  margin-top: 10px;
  transition: opacity 0.15s;
}

.card--action:active {
  opacity: 0.7;
}



/* ── Sensors ── */


/* ── Preferences ── */
.pref-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border-bottom: 1px solid;
  cursor: pointer;
  transition: background 0.15s;
}

.pref-row--last {
  border-bottom: none;
}

.pref-row:active {
  background: rgba(255, 255, 255, 0.03);
}

.pref-icon {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-icon);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.pref-info {
  flex: 1;
}

.pref-name {
  font-size: 15px;
  font-weight: 500;
  color: var(--text-primary);
}

.pref-sub {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 1px;
}
</style>
