<template>
  <header class="app-header">
    <div class="status-bar">
      <span class="status-time">{{ time }}</span>
      <div class="status-icons">
        <svg width="15" height="12" viewBox="0 0 15 12" fill="none">
          <path d="M7.5 2.5C9.8 2.5 11.8 3.5 13.2 5.1L14.5 3.8C12.7 1.8 10.2 0.5 7.5 0.5C4.8 0.5 2.3 1.8 0.5 3.8L1.8 5.1C3.2 3.5 5.2 2.5 7.5 2.5Z" fill="currentColor" opacity="0.4"/>
          <path d="M7.5 5.5C9 5.5 10.3 6.1 11.3 7.1L12.6 5.8C11.2 4.4 9.4 3.5 7.5 3.5C5.6 3.5 3.8 4.4 2.4 5.8L3.7 7.1C4.7 6.1 6 5.5 7.5 5.5Z" fill="currentColor" opacity="0.7"/>
          <circle cx="7.5" cy="10" r="1.5" fill="currentColor"/>
        </svg>
        <div class="battery">
          <div class="battery-body">
            <div class="battery-fill" style="width: 72%"></div>
          </div>
          <div class="battery-cap"></div>
        </div>
      </div>
    </div>
    <div class="header-content">
      <div class="header-text">
        <p v-if="subtitle" class="header-subtitle">{{ subtitle }}</p>
        <h1 class="header-title">{{ title }}</h1>
      </div>

      <div class="header-actions">
        <button  class="btn">
          i
        </button>

        <button v-if="showNotif" class="btn" @click="$emit('notif')">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
          </svg>
          <span v-if="alertCount > 0" class="notif-badge">{{ alertCount }}</span>
        </button>
      </div>

    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useAppStore } from '../../store/app'

defineProps<{
  title: string
  subtitle?: string
  showNotif?: boolean
}>()

defineEmits(['notif'])

const store = useAppStore()
const alertCount = computed(() => store.alerts.length)

const time = ref('')
let timer: ReturnType<typeof setInterval>

function updateTime() {
  const now = new Date()
  time.value = now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' })
}

onMounted(() => {
  updateTime()
  timer = setInterval(updateTime, 10000)
})
onUnmounted(() => clearInterval(timer))
</script>

<style scoped lang="scss">
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: var(--bg-primary);
  border-bottom: 1px solid var(--border-subtle);
}

.status-bar {
  height: 44px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;

  .status-time {
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: -0.01em;
  }

  .status-icons {
    display: flex;
    align-items: center;
    gap: 6px;
    color: var(--text-primary);
  }
}

.battery {
  display: flex;
  align-items: center;
  gap: 1px;

  &-body {
    width: 22px;
    height: 12px;
    border: 1.5px solid currentColor;
    border-radius: 3px;
    padding: 2px;
    opacity: 0.9;
  }

  &-fill {
    height: 100%;
    background: currentColor;
    border-radius: 1.5px;
  }

  &-cap {
    width: 2px;
    height: 5px;
    background: currentColor;
    border-radius: 0 1px 1px 0;
    opacity: 0.6;
  }
}

.header-content {
  height: 64px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-subtitle {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin-bottom: 1px;
}

.header-title {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text-primary);
}
.header-actions {
  display: flex;
  gap: 7px;
}

.btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  color: var(--text-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;

  &:active {
    background: var(--bg-elevated);
  }
}

.notif-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  width: 18px;
  height: 18px;
  background: var(--accent-orange);
  color: #000;
  border-radius: 50%;
  font-size: 0.65rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
