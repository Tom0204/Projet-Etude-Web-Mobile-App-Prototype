<script setup lang="ts">
import { Cloud, Activity, MapPin, ShieldAlert } from 'lucide-vue-next'
import { useAppStore } from '../../store/app'
import { useSensorData } from '../../composables/useSensorData'
import {definePageMeta} from "../../../.nuxt/imports";
import { ref } from 'vue'
import DailySumary from "../core/home/DailySumary.vue";
import NavGrid from "../core/home/NavGrid.vue";
import ClassicAlerte from "../core/home/ClassicAlerte.vue";

definePageMeta({ layout: 'default' })

const store = useAppStore()
const { sensors } = useSensorData()

const navItems = [
  { to: '/meteo',    label: 'Météo',    sub: 'Prévisions 7j',    icon: Cloud,       color: '#2563eb' },
  { to: '/capteurs', label: 'Capteurs', sub: 'Temp / Humidité',   icon: Activity,    color: '#0d9488' },
  { to: '/sante',    label: 'Santé',    sub: 'Analyse & risques', icon: ShieldAlert, color: '#7c3aed' },
  { to: '/',         label: 'Alertes',  sub: `${store.unreadCount} notifications`, icon: MapPin, color: '#dc2626' },
]

const activity = [
  { title: 'Capteur air mis à jour',        time: 'Il y a 2 min',   type: 'green'  },
  { title: 'Prévision mildiou — Élevé',     time: 'Il y a 18 min',  type: 'orange' },
  { title: 'Analyse sol Parcelle A',        time: 'Il y a 1h',      type: 'blue'   },
  { title: 'Rapport journalier généré',     time: 'Ce matin 07:00', type: 'green'  },
]


const DailyStat = ref([
  { label: 'Température', value: sensors.value.airTemp ,unit :'°C', status: 'Normal', badgeText: 'neutral',badgeLevel: 2 },
  { label: 'Humidité sol', value: sensors.value.soilHumidity,unit :'%', status: 'Modéré', badgeText: 'medium',badgeLevel: 3 },
  { label: 'Humidité air', value: sensors.value.airHumidity ,unit : '%', status: 'Élevé', badgeText: 'high',badgeLevel: 4 },
  { label: 'Santé globale', value: `74`, unit :'/100', status: 'Bon état', badgeText: 'low',badgeLevel: 0 },
])
</script>

<template>
  <!-- Alerte mildiou -->
  <div class="pages animate-fade-up">
    <ClassicAlerte/>

    <!-- Navigation grid -->
    <NavGrid :items="navItems"/>

    <!-- Résumé du jour -->
    <DailySumary :list="DailyStat"/>


  </div>
</template>

<style scoped lang="scss">

</style>