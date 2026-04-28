// plugins/chartjs.client.ts
// Client-only plugin: registers Chart.js globally
// Used by SensorCharts.vue and any other chart components

import {
  Chart,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
  Filler,
} from 'chart.js'
import { defineNuxtPlugin } from "nuxt/app"

export default defineNuxtPlugin(() => {
  Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    BarElement,
    ArcElement,
    Title,
    Tooltip,
    Legend,
    Filler,
  )

  // Global chart defaults — dark theme
  Chart.defaults.color = '#9a9590'
  Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.06)'
  Chart.defaults.font.family = "'DM Sans', sans-serif"
  Chart.defaults.plugins.tooltip.backgroundColor = '#242424'
  Chart.defaults.plugins.tooltip.titleColor = '#9a9590'
  Chart.defaults.plugins.tooltip.bodyColor = '#f0ede8'
  Chart.defaults.plugins.tooltip.borderColor = 'rgba(255,255,255,0.08)'
  Chart.defaults.plugins.tooltip.borderWidth = 1
  Chart.defaults.plugins.tooltip.padding = 10
  Chart.defaults.plugins.tooltip.cornerRadius = 10
  Chart.defaults.plugins.legend.display = false
})
