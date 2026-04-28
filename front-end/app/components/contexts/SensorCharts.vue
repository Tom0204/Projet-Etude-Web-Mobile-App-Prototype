<template>
  <div class="sensor-charts">
    <!-- Grid capteurs -->
    <DailySumary :liste="sensorCard"/>

    <!-- Graphique température -->
    <Canva :dataGraph="tempData" :labels="label" title="Température" :colors="['#FF8C00','#0072FF']" ></Canva>

    <Canva :dataGraph="humidData" :labels="label" title="Humidité" :colors="['#2ECC71','#E91E63']"></Canva>

  </div>
</template>

<script setup lang="ts">
import {ref, onMounted, onUnmounted, watch , computed} from 'vue'
import { useSensorData } from '../../composables/useSensorData'
import Canva from "../core/sensor/Canva.vue";
import DailySumary from "../core/home/DailySumary.vue";
import {useFetch} from "nuxt/app";

const { sensors } = useSensorData()


interface Sensor {
  timestamp: string
  sensor_id: string
  temperature_c: string  // ← string !
  humidity_pct: string   // ← string !
  soil_moisture_pct: string
  soil_ph: string
}


const api = '10.111.1.37:8080' //! ICI API
const { data: ListLastSensor, pending, error, refresh } = useFetch<Array<Sensor>>(
    `http://${api}/sensors/?limit=24`,
    {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    }

)


const label = ["Air","Sol"]
const badgeC = ["Froid","Optimal","Chaud","Élevé !"]
const badgeH = ["Sec","Optimal","Saturation","Élevé !"]
const badgeN = ["Carence","Optimal","Surdosage","Élevé !"]

const cI = [15,22,30]
const cSI = [10,15,20]
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


const sensorCard = ref([{}])
const tempData = ref({})
const humidData = ref({})


const listpred = ref([
  12.45, 87.12, 34.09, 56.78, 91.23, 4.56,
  67.89, 23.45, 8.91, 45.67, 78.12, 10.34,
  55.21, 99.04, 32.18, 14.76, 62.33, 41.50,
  7.29, 88.65, 19.82, 53.47, 71.11,50
])
const listpred2 = ref([
  12.45, 87.12, 34.09, 56.78, 91.23, 4.56,
  67.89, 23.45, 8.91, 45.67, 78.12, 10.34,
  55.21, 99.04, 32.18, 14.76, 62.33, 41.50,
  7.29, 88.65, 19.82, 53.47, 71.11 , 50
])


watch(ListLastSensor, (val) => {
  if (!val) return
  const len = val.length
  tempData.value = {
    graph1: val.map(({ temperature_c }) => parseFloat(temperature_c)).reverse(),
    graph1pred: [
            ...Array(len - 1).fill(null),
      parseFloat(val[0]?.temperature_c ?? '0'), ...listpred.value
    ],
    // graph2: [15.8, 15.2, 14.5, 13.8, 12.1, 10.4, 8.2, 7.1, 6.8, 6.5],
    // graph2pred: [...Array(15).fill(null),
    //   6.5,
    //   5.2, 4.1, 7.4, 3.2, 5.8, 12.4, 25.6, 29.3, 23.0
    // ],
  }

  humidData.value = {
    graph1: val.map(({ humidity_pct }) => parseFloat(humidity_pct)).reverse(),
    graph1pred: [...Array(len - 1).fill(null),
      parseFloat(val[0]?.humidity_pct ?? '0'),
      ...listpred2.value
    ],
    // graph2: [26.5, 26.7, 26.4, 26.8, 27.2, 27.5, 27.9, 28.1],
    // graph2pred: [
    //   ...Array(15).fill(null),
    //   26.4, 22.4, 23.1, 24.5, 27.8, 30.2, 32.5
    // ],
  }


  sensorCard.value= [{
      label: 'Température air',
      value: ListLastSensor.value?.[0]?.temperature_c,
      unit :'°C' ,
      badgeText: returnLevel(  parseFloat(ListLastSensor.value?.[0]?.temperature_c ?? '0'),cI,badgeC)[1],
      badgeLevel: returnLevel(  parseFloat(ListLastSensor.value?.[0]?.temperature_c ?? '0'),cI,badgeC)[0]
    },
    { label: 'Température sol', value: sensors.value.soilTemp ,unit :'°C', badgeText: returnLevel(sensors.value.soilTemp,cSI,badgeC)[1],bageLevel: returnLevel(sensors.value.soilTemp,cSI,badgeC)[0] },
    { label: 'Humidité air', value:   ListLastSensor.value?.[0]?.humidity_pct ,unit : '%', badgeText: returnLevel( parseFloat(ListLastSensor.value?.[0]?.humidity_pct ?? '0'),hI,badgeH)[1] ,badgeLevel: returnLevel( parseFloat(ListLastSensor.value?.[0]?.humidity_pct ?? '0'),hI,badgeH)[0] },
    { label: 'Humidité sol', value: sensors.value.soilHumidity,unit :'%', badgeText: returnLevel(sensors.value.soilHumidity,hI,badgeH)[1],badgeLevel: returnLevel(sensors.value.soilHumidity,hI,badgeH)[0]},
    { label: 'Nutriments', value: sensors.value.nutrition ,unit : '%', badgeText: returnLevel(sensors.value.nutrition,nI,badgeN)[1] ,badgeLevel: returnLevel(sensors.value.nutrition,nI,badgeN)[0] },

  ]
  console.log(tempData.value)
  console.log(sensorCard.value)
})








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
