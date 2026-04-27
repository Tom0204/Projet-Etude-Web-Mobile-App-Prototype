<template>
  <div class="sensor-charts">
    <!-- Grid capteurs -->
    <div class="grid-2 animate-fade-up">
      <div class="card sensor-card">
        <p class="sensor-label">Temp. air</p>
        <p class="sensor-value">{{ sensors.airTemp }}<span class="sensor-unit">°C</span></p>
        <span class="badge badge--low">↑ +0.8°</span>
      </div>
      <div class="card sensor-card">
        <p class="sensor-label">Temp. sol</p>
        <p class="sensor-value">{{ sensors.soilTemp }}<span class="sensor-unit">°C</span></p>
        <span class="badge badge--stable">Stable</span>
      </div>
      <div class="card sensor-card delay-1 animate-fade-up">
        <p class="sensor-label">Hum. air</p>
        <p class="sensor-value">{{ sensors.airHumidity }}<span class="sensor-unit">%</span></p>
        <span class="badge badge--high">↑ Élevé</span>
      </div>
      <div class="card sensor-card delay-1 animate-fade-up">
        <p class="sensor-label">Hum. sol</p>
        <p class="sensor-value">{{ sensors.soilHumidity }}<span class="sensor-unit">%</span></p>
        <span class="badge badge--low">Optimal</span>
      </div>
    </div>

    <!-- Graphique température -->
    <Canva :dataGraph="tempData" :labels="label"></Canva>

    <!-- Humidité comparée -->
    <div class="card delay-3 animate-fade-up">
      <p class="section-label">Humidité comparée</p>
      <div class="humidity-bars">
        <div class="hum-row">
          <span class="hum-label">Air</span>
          <div class="progress-bar flex-1">
            <div class="progress-fill progress-fill--blue" :style="{ width: sensors.airHumidity + '%' }"></div>
          </div>
          <span class="hum-value">{{ sensors.airHumidity }}%</span>
        </div>
        <div class="hum-row">
          <span class="hum-label">Sol</span>
          <div class="progress-bar flex-1">
            <div class="progress-fill progress-fill--green" :style="{ width: sensors.soilHumidity + '%' }"></div>
          </div>
          <span class="hum-value">{{ sensors.soilHumidity }}%</span>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useSensorData } from '../../composables/useSensorData'
import Canva from "../core/sensor/Canva.vue";

const { sensors } = useSensorData()


const tempData = {
  graph1: [7.2, 6.8, 6.4, 7.5, 10.1, 13.5, 16.2, 17.1, 16.5, 14.8, 12.7, 10.9, 9.4, 8.7, 8.1, 7.6],
  graph1pred: [
    ...Array(15).fill(null),
    7.6,
    21.4, 20.9, 20.1, 21.5, 17.8, 15.2, 28.9, 30.2, 29.7, 27.5, 25.4, 23.8, 22.1, 21.8, 21.5, 21.2
  ],
  graph2: [15.8, 15.2, 14.5, 13.8, 12.1, 10.4, 8.2, 7.1, 6.8, 6.5, 6.2, 5.9, 5.7, 5.5, 5.4, 5.2],
  graph2pred: [
    ...Array(15).fill(null),
    5.2,
    4.1, 7.4, 3.2, 5.8, 12.4, 25.6, 29.3, 23.0, 30, 25.1, 28.1, 15.3, 10.1, 8.4, 6.1, 6.5
  ],
}
const label = ["Air","Sol"]

</script>

<style scoped lang="scss">
.sensor-charts {
  display: flex;
  flex-direction: column;
  gap: 12px;

}

.sensor-card {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sensor-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}

.sensor-value {
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1;
  color: var(--text-primary);
}

.sensor-unit {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-secondary);
  margin-left: 2px;
}



.humidity-bars {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.hum-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.hum-label {
  width: 52px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.flex-1 { flex: 1; }

.hum-value {
  width: 36px;
  text-align: right;
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--text-primary);
}
</style>
