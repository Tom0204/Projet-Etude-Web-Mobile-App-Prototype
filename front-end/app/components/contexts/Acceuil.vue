<script setup lang="ts">
import { Cloud, Activity, MapPin, ShieldAlert } from 'lucide-vue-next'
import { useAppStore } from '../../store/app'
import { useSensorData } from '../../composables/useSensorData'
import {definePageMeta} from "../../../.nuxt/imports";
import {ref, watch} from 'vue'
import DailySumary from "../core/home/DailySumary.vue";
import NavGrid from "../core/home/NavGrid.vue";
import ClassicAlerte from "../core/home/ClassicAlerte.vue";
import {useFetch} from "nuxt/app";

definePageMeta({ layout: 'default' })

const store = useAppStore()
const { sensors } = useSensorData()

const navItems = [
  { to: '/meteo',    label: 'Météo',    sub: 'Prévisions 7j',    icon: Cloud,       color: '#2563eb' },
  { to: '/capteurs', label: 'Capteurs', sub: 'Temp / Humidité',   icon: Activity,    color: '#0d9488' },
  { to: '/',         label: 'Alertes',  sub: `${store.unreadCount} notifications`, icon: MapPin, color: '#dc2626' },
]


//*-----------------------------------------------Sensor // temp / hum --------------------------------------------------

interface Sensor {
  timestamp: string
  sensor_id: string
  temperature_c: string  // ← string !
  humidity_pct: string   // ← string !
  soil_moisture_pct: string
  soil_ph: string
}
const api = '10.111.1.37:8080' //! ICI API
const { data: lastSensor, pending, error, refresh } = useFetch<Sensor>(
    `http://${api}/sensors/latest`,
    {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    }
)

const DailyStat = ref([{}])



watch(lastSensor, (val) => {
  if (!val) return

  console.log(val)

  DailyStat.value = [
    { label: 'Température', value: val.temperature_c ,unit :'°C', status: 'Normal', badgeText: 'neutral',badgeLevel: 2 },
    { label: 'Humidité sol', value: val.humidity_pct,unit :'%', status: 'Modéré', badgeText: 'medium',badgeLevel: 3 },
    { label: 'Humidité air', value: sensors.value.airHumidity ,unit : '%', status: 'Élevé', badgeText: 'high',badgeLevel: 4 },
    { label: 'Nutriments', value: sensors.value.nutrition, unit :'%', status: 'Bon état', badgeText: 'fine',badgeLevel: 0 },
  ]

})



</script>

<template>
  <div class="pages animate-fade-up">

    <div></div>

    <ClassicAlerte/>

    <NavGrid :items="navItems"/>

    <DailySumary :liste="DailyStat"/>


  </div>
</template>

<style scoped lang="scss">

</style>