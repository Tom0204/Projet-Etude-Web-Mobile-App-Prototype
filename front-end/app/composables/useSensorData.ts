import { ref, readonly } from 'vue'


export interface SensorData {
  airTemp: number
  soilTemp: number
  airHumidity: number
  soilHumidity: number
  nutrition: number
  lastUpdate: Date
}

const sensors = ref<SensorData>({
  airTemp: 16.4,
  soilTemp: 13.1,
  airHumidity: 78,
  soilHumidity: 62,
  nutrition: 91,
  lastUpdate: new Date(),
})

// Simulate slight real-time variation
let intervalId: ReturnType<typeof setInterval> | null = null

function startSimulation() {
  if (intervalId) return
  intervalId = setInterval(() => {
    const jitter = (range: number) => (Math.random() - 0.5) * range

    sensors.value = {
      airTemp:       parseFloat((sensors.value.airTemp + jitter(0.4)).toFixed(1)),
      soilTemp:      parseFloat((sensors.value.soilTemp + jitter(0.2)).toFixed(1)),
      airHumidity:   Math.min(100, Math.max(0, Math.round(sensors.value.airHumidity + jitter(2)))),
      soilHumidity:  Math.min(100, Math.max(0, Math.round(sensors.value.soilHumidity + jitter(1)))),
      nutrition:  Math.min(100, Math.max(0, Math.round(sensors.value.nutrition + jitter(2)))),
      lastUpdate: new Date(),
    }
  }, 5000)
}

function stopSimulation() {
  if (intervalId) {
    clearInterval(intervalId)
    intervalId = null
  }
}

export function useSensorData() {
  startSimulation()

  // Historical temperature data for chart (24h, hourly)
  const tempHistory = ref<number[]>([
    6.8, 6.5, 6.2, 6.0, 6.4, 7.2, 8.8, 10.5,
    12.3, 13.9, 15.1, 15.8, 16.2, 16.4, 15.9, 14.8,
    13.5, 12.1, 11.0, 10.2, 9.4, 8.8, 8.1, 7.6,
  ])

  const humidityHistory = ref({
    air:    [82, 80, 79, 81, 83, 84, 82, 80, 77, 75, 74, 76, 78, 78, 77, 76, 75, 74, 75, 76, 77, 78, 79, 78],
    soil:   [63, 63, 62, 62, 62, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62],
    leaves: [95, 94, 93, 92, 91, 90, 89, 88, 88, 89, 90, 91, 91, 91, 90, 90, 90, 91, 91, 92, 92, 92, 91, 91],
  })

  return {
    sensors: readonly(sensors),
    tempHistory: readonly(tempHistory),
    humidityHistory: readonly(humidityHistory),
    stopSimulation,
  }
}
