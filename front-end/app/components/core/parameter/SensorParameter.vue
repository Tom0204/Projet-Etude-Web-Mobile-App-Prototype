<script setup lang="ts">
import {h, ref} from 'vue'
import ClassicCard from "../containers/ClassicCard.vue";
import ElevatedCard from "../containers/ElevatedCard.vue";
import BoldTitleLabel from "../Label/BoldTitleLabel.vue";
import SmallLabel from "../Label/SmallLabel.vue";


const IconSoil = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('path', { d: 'M12 2a10 10 0 0 0-7.35 16.83C6.18 20.85 9 22 12 22s5.82-1.15 7.35-3.17A10 10 0 0 0 12 2z' }),
    h('path', { d: 'M12 8v8' }),
    h('path', { d: 'M8 12h8' }),
  ])
}
const IconAir = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('circle', { cx: 12, cy: 12, r: 5 }),
    h('line', { x1: 12, y1: 1, x2: 12, y2: 3 }),
    h('line', { x1: 12, y1: 21, x2: 12, y2: 23 }),
    h('line', { x1: 4.22, y1: 4.22, x2: 5.64, y2: 5.64 }),
    h('line', { x1: 18.36, y1: 18.36, x2: 19.78, y2: 19.78 }),
    h('line', { x1: 1, y1: 12, x2: 3, y2: 12 }),
    h('line', { x1: 21, y1: 12, x2: 23, y2: 12 }),
  ])
}
const IconRain = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('line', { x1: 8, y1: 19, x2: 8, y2: 21 }),
    h('line', { x1: 8, y1: 13, x2: 8, y2: 15 }),
    h('line', { x1: 16, y1: 19, x2: 16, y2: 21 }),
    h('line', { x1: 16, y1: 13, x2: 16, y2: 15 }),
    h('line', { x1: 12, y1: 21, x2: 12, y2: 23 }),
    h('line', { x1: 12, y1: 15, x2: 12, y2: 17 }),
    h('path', { d: 'M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25' }),
  ])
}
const IconLeaf = {
  render: () => h('svg', { width: 20, height: 20, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
    h('path', { d: 'M2 22c1.25-1.25 2.5-2.5 3.75-3.75M12 2C6.5 7.5 2 12 2 17c0 2.76 2.24 5 5 5s5-2.24 5-5c0-1.93 1.57-3.5 3.5-3.5h1C19.43 13.5 22 10.93 22 7.5 22 4.46 19.54 2 16.5 2H12z' }),
  ])
}

const sensors = ref([
  { id: 1, name: 'Capteur Sol A1', type: 'Temp + humidité sol', online: true, value: '13.1°C', icon: IconSoil, iconBg: 'rgba(120,200,120,0.15)', iconColor: '#7BC67E' },
  { id: 2, name: 'Station Air B2', type: 'Temp + humidité air', online: true, value: '16.4°C', icon: IconAir, iconBg: 'rgba(100,160,240,0.15)', iconColor: '#64A0F0' },
  { id: 3, name: 'Pluviomètre C1', type: 'Précipitations', online: true, value: '0 mm', icon: IconRain, iconBg: 'rgba(180,140,80,0.15)', iconColor: '#C8A050' },
  { id: 4, name: 'Capteur H D1', type: 'Humidité ', online: false, value: '—', icon: IconLeaf, iconBg: 'rgba(220,80,80,0.15)', iconColor: '#E07070' },
])
</script>

<template>
  <ClassicCard class="list-container" title="CAPTEURS LIÉS">


    <ElevatedCard>
      <div
          v-for="(sensor, index) in sensors"
          :key="sensor.id"
          class="sensor-row"
          :class="{ 'sensor-row--last': index === sensors.length - 1 }"
      >
        <div class="sensor-icon" :style="{ background: sensor.iconBg }">
          <component :is="sensor.icon" class="icon-svg" :style="{ color: sensor.iconColor }" />
        </div>
        <div class="sensor-info">
          <BoldTitleLabel :text=" sensor.name"/>
          <SmallLabel :text="sensor.type"/>
        </div>
        <div class="sensor-status">
              <span class="status-pill" :class="sensor.online ? 'status-online' : 'status-offline'">
                <span class="status-dot" />
                {{ sensor.online ? 'En ligne' : 'Hors ligne' }}
              </span>
          <BoldTitleLabel :text="sensor.value" :class="{ 'sensor-value--offline': !sensor.online }"/>
        </div>
      </div>
    </ElevatedCard>

    <ClassicCard class="btn-hover" >
      <button class="link-btn">
        <div class="link-icon">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        </div>
        <div class="link-text">
          <p class="link-title">Lier un nouveau capteur</p>
          <p class="link-sub">Bluetooth, NFC ou LoRa</p>
        </div>
      </button>
    </ClassicCard>
  </ClassicCard>
</template>

<style scoped lang="scss">

.list-container{
  display: flex;
  flex-direction: column;
  gap: 14px;
}


.sensor-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  transition: background 0.15s;
}

.sensor-row--last {
  border-bottom: none;
}

.sensor-row:active {
  background: rgba(255, 255, 255, 0.03);
}

.sensor-icon {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-icon);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.icon-svg {
  width: 20px;
  height: 20px;
}

.sensor-info {
  flex: 1;
  min-width: 0;
}

.sensor-name {
  font-size: 15px;
  font-weight: 500;
  color: var(--text-primary);
}

.sensor-type {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 1px;
}

.sensor-status {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.status-pill {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 11px;
  font-weight: 500;
}

.status-online {
  color: limegreen;
}

.status-offline {
  color: red;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}


.sensor-value {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
}

.sensor-value--offline {
  color: var(--text-tertiary);
}

/* ── Link button ── */
.link-btn {
  display: flex;
  gap : 14px;
  align-items: center;
}
.btn-hover:hover{
  background: #544b4b;
}
.link-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: rgba(79, 160, 247, 0.18);
  color: var(--blue);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.link-text {
  flex: 1;
}

.link-title {
  font-size: 15px;
  font-weight: 500;
  color: var(--blue);
}

.link-sub {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 1px;
}

.chevron {
  color: var(--text-tertiary);
  flex-shrink: 0;

}
</style>