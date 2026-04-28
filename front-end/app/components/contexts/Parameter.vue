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
import Settings from "../core/parameter/Settings.vue";

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
      <Settings />


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
  gap: 14px;
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
