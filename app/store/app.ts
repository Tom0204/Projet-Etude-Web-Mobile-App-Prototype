import { defineStore } from 'pinia'

export interface Alert {
  id: string
  type: 'warning' | 'info' | 'danger'
  title: string
  message: string
  timestamp: Date
  read: boolean
}

export const useAppStore = defineStore('app', {
  state: () => ({
    activePage: '/' as string,
    alertPanelOpen: false,
    alerts: [
      {
        id: 'alert-2',
        type: 'info' as const,
        title: 'Pluie prévue vendredi',
        message: '14mm attendus — report des traitements recommandé',
        timestamp: new Date(Date.now() - 3600_000),
        read: false,
      },
      {
        id: 'alert-3',
        type: 'info' as const,
        title: 'Capteur sol Parcelle B',
        message: 'Humidité stable à 62% — niveau optimal maintenu',
        timestamp: new Date(Date.now() - 7200_000),
        read: true,
      },
    ] as Alert[],

    // App settings
    parcelleActive: 'Parcelle A',
    parcelles: ['Parcelle A', 'Parcelle B', 'Parcelle C'],
  }),

  getters: {
    unreadCount: (state) => state.alerts.filter((a) => !a.read).length,
    unreadAlerts: (state) => state.alerts.filter((a) => !a.read),
  },

  actions: {
    setActivePage(path: string) {
      this.activePage = path
    },

    toggleAlertPanel() {
      this.alertPanelOpen = !this.alertPanelOpen
    },

    markAlertRead(id: string) {
      const alert = this.alerts.find((a) => a.id === id)
      if (alert) alert.read = true
    },

    markAllRead() {
      this.alerts.forEach((a) => (a.read = true))
    },

    dismissAlert(id: string) {
      this.alerts = this.alerts.filter((a) => a.id !== id)
    },

    setParcelleActive(name: string) {
      this.parcelleActive = name
    },
  },
})
