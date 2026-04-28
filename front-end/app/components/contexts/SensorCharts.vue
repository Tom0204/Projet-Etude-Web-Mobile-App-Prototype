<template>
  <div class="sensor-charts">
    <!-- Grid capteurs -->
    <DailySumary :liste="ActualStatA"/>

    <!-- Graphique température -->
    <Canva :dataGraph="tempData" :labels="label" title="Température" :colors="['#FF8C00','#0072FF']" ></Canva>

    <Canva :dataGraph="humidData" :labels="label" title="Humidité" :colors="['#2ECC71','#E91E63']"></Canva>

    <!-- Humidité comparée -->
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useSensorData } from '../../composables/useSensorData'
import Canva from "../core/sensor/Canva.vue";
import DailySumary from "../core/home/DailySumary.vue";

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
const humidData = {
  graph1: [24.1, 23.8, 23.5, 24.2, 26.4, 28.1, 30.5, 31.8, 31.2, 29.5, 27.8, 26.2, 25.4, 24.9, 24.5, 24.2],
  graph1pred: [
    ...Array(15).fill(null),
    24.2,
    32.5, 31.9, 31.2, 30.4, 28.7, 26.5, 24.2, 22.8, 21.5, 20.9, 20.1, 19.4, 18.8, 18.5, 18.2, 18.0
  ],
  graph2: [26.5, 26.7, 26.4, 26.8, 27.2, 27.5, 27.9, 28.1, 28.0, 27.8, 27.5, 27.2, 26.9, 26.7, 26.5, 26.4],
  graph2pred: [
    ...Array(15).fill(null),
    26.4,
    22.4, 23.1, 24.5, 27.8, 30.2, 32.5, 34.1, 35.2, 34.8, 33.1, 30.5, 28.2, 26.4, 25.1, 24.2, 23.5
  ],
}


const label = ["Air","Sol"]
const badgeC = ["Froid","Optimal","Chaud","Élevé !"]
const badgeH = ["Sec","Optimal","Saturation","Élevé !"]
const badgeN = ["Carence","Optimal","Surdosage","Élevé !"]

const cI = [15,22,30]
const hI = [15,30,40]
const nI = [40,90,100]

const returnLevel = (value: number ,interval:Array<number>, badge :Array<string>) => {
  switch (true) {
    case value < interval[0]:
      return [1,badge[0]]
    case value < interval[1]:
      return [0,badge[1]]
    case value < interval[2]:
      return [3,badge[2]]
    default:
      return [4,badge[3]]
  }
}





const ActualStatA = ref([
  { label: 'Température sol', value: sensors.value.soilTemp ,unit :'°C' , badgeText: returnLevel(sensors.value.soilTemp,cI,badgeC)[1],badgeLevel: returnLevel(sensors.value.soilTemp,cI,badgeC)[0] },
  { label: 'Température air', value: sensors.value.airTemp ,unit :'°C', badgeText: returnLevel(sensors.value.airTemp,cI,badgeC)[1],badgeLevel: returnLevel(sensors.value.airTemp,cI,badgeC)[0] },
  { label: 'Humidité sol', value: sensors.value.soilHumidity,unit :'%', badgeText: returnLevel(sensors.value.soilHumidity,hI,badgeH)[1],badgeLevel: returnLevel(sensors.value.soilHumidity,hI,badgeH)[0]},
  { label: 'Humidité air', value: sensors.value.airHumidity ,unit : '%', badgeText: returnLevel(sensors.value.airHumidity,hI,badgeH)[1] ,badgeLevel: returnLevel(sensors.value.airHumidity,hI,badgeH)[0] },
  { label: 'Nutriments', value: sensors.value.nutrition ,unit : '%', badgeText: returnLevel(sensors.value.nutrition,nI,badgeN)[1] ,badgeLevel: returnLevel(sensors.value.nutrition,nI,badgeN)[0] },

])

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
