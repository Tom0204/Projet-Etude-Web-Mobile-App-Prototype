<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useSensorData } from '../../../composables/useSensorData'

const props = defineProps({
  dataGraph: { type: Object , required: true},
  labels: { type: Array<string>, required: true },
  title: { type: String, required: true },
  colors: { type: Array<string>, required: true },
})


const { sensors } = useSensorData()

const tempChartRef = ref(null)

let chartInstance: any = null

watch(() => props.dataGraph, (newData) => {
  if (!chartInstance || !newData) return

  chartInstance.data.datasets[0].data = newData.graph1
  chartInstance.data.datasets[1].data = newData.graph1pred
  chartInstance.data.datasets[2].data = newData.graph2
  chartInstance.data.datasets[3].data = newData.graph2pred

  chartInstance.update()
}, { deep: true })

const xLabels = ['00', '03', '06', '09', '12', '15', '18', '21', '24', '27', '30', '33', '36', '39', '42', '45', '48']


const allLabels = Array.from({ length: 48 }, (_, i) => `${i}h`)
onMounted(async () => {
  if (!tempChartRef.value) return
  try {
    const { Chart, registerables } = await import('chart.js')
    Chart.register(...registerables)

    chartInstance = new Chart(tempChartRef.value, {
      type: 'line',
      data: {
        labels: allLabels,
        datasets: [
          {
            label: props.labels[0],
            data: props.dataGraph.graph1,
            borderColor: props.colors[0],
            backgroundColor: 'rgba(96, 165, 250, 0.07)',
            borderWidth: 2,
            pointRadius: 3,
            pointBackgroundColor: props.colors[0],
            pointBorderColor: '#1a1a1a',
            pointBorderWidth: 1.5,
            tension: 0.4,
            fill: true,
          },
          {
            label: props.labels[0] + '_Forecast',
            data: props.dataGraph.graph1pred,
            borderColor: props.colors[0]+'99',
            backgroundColor: 'rgba(96, 165, 250, 0.03)',
            borderWidth: 1.5,
            borderDash: [4, 4],
            pointRadius: 0,
            pointHoverRadius: 2,
            tension: 0.4,
            fill: true,
          },

          {
            label: props.labels[1],
            data: props.dataGraph.graph2,
            borderColor: props.colors[1],
            backgroundColor: 'rgba(249, 115, 22, 0.07)',
            borderWidth: 2,
            pointRadius: 3,
            pointBackgroundColor: props.colors[1],
            pointBorderColor: '#1a1a1a',
            pointBorderWidth: 1.5,
            tension: 0.4,
            fill: true,
          },

          {
            label: props.labels[1] + '_Forecast',
            data: props.dataGraph.graph2pred,
            borderColor:  props.colors[1]+'99',
            backgroundColor: 'rgba(249, 115, 22, 0.03)',
            borderWidth: 1.5,
            borderDash: [4, 4],
            pointRadius: 0,
            pointHoverRadius: 2,
            tension: 0.4,
            fill: true,
          },
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#242424',
            titleColor: '#9a9590',
            bodyColor: '#f0ede8',
            borderColor: 'rgba(255,255,255,0.08)',
            borderWidth: 1,
            padding: 8,
            filter: (item) => !item.dataset.label?.endsWith('_Forecast'),
            callbacks: {
              label: (ctx) => ` ${ctx.dataset.label}  ${ctx.parsed.y}°C`
            }
          }
        },
        scales: {
          x: { display: false },
          y: {
            display: true,
            grid: { color: 'rgba(255,255,255,0.04)' },
            border: { display: false },
            ticks: {
              color: '#6b6760',
              font: { size: 10 },
              maxTicksLimit: 4,
              callback: (v) => `${v}°`
            }
          }
        }
      }
    })
  } catch (e) {
    console.error('Chart.js not available', e)
  }
})

onUnmounted(() => {
  chartInstance?.destroy()
})
</script>

<template>
  <div class="card delay-2 animate-fade-up">
    <div class="card-header">
      <p class="section-label">{{ title }} — 24H</p>
      <div class="legend">
        <span class="legend-item">
          <span class="legend-dot" :style="`background: ${colors[0]} `"></span>
          {{ props.labels[0] }}
        </span>
        <span class="legend-item">
          <span class="legend-dot" :style="`background: ${colors[1]} `"></span>
          {{ props.labels[1] }}
        </span>
        <span class="legend-forecast">
          <span class="legend-dash"></span>
          Prévision
        </span>
      </div>
    </div>
    <div class="chart-container">
      <canvas ref="tempChartRef" height="110"></canvas>
    </div>
    <div class="chart-axis">
      <span v-for="h in xLabels" :key="h" class="chart-tick">{{ h }}</span>
    </div>
  </div>
</template>

<style scoped lang="scss">
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}

.legend {
  display: flex;
  align-items: center;
  gap: 12px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 0.65rem;
  color: var(--text-muted);
  font-family: var(--font-mono);
  letter-spacing: 0.03em;
}

.legend-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}

.legend-forecast {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 0.65rem;
  color: var(--text-muted);
  font-family: var(--font-mono);
  opacity: 0.6;
}

.legend-dash {
  width: 14px;
  height: 1.5px;
  background: repeating-linear-gradient(
      90deg,
      var(--text-muted) 0px,
      var(--text-muted) 4px,
      transparent 4px,
      transparent 8px
  );
  flex-shrink: 0;
}

.chart-container {
  height: 110px;
  position: relative;
}

.chart-axis {
  display: flex;
  justify-content: space-between;
  margin-top: 6px;

  .chart-tick {
    font-size: 0.65rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }
}
</style>