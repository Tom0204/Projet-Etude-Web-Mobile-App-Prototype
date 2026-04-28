<template>
  <div class="pages animate-fade-up">
    <!-- Hero météo actuelle -->
    <ElevatedCard text="" class="weather-hero">
      <SeparatedRowColumnContainer  >
        <template #col1>
          <ActualTopInfo :ele="current"/>
        </template>
        <template #col2>
          <IconWeather :icon="current.emoji"/>
        </template>
      </SeparatedRowColumnContainer>
    </ElevatedCard>

    <!-- Prévisions 5 jours -->
   <ClassicCard title="Prévisions 5 jours">
      <ListColumn :elements="forecast" >
        <template #default="{ ele_cont }">
          <DayLineInfo :ele_content="ele_cont as Record<string, any>"></DayLineInfo>
        </template>
      </ListColumn>
    </ClassicCard>

    <!-- Conditions agricoles -->
    <ClassicCard title="Conditions agricoles">
     <GridContainer>
        <SubCard text="Gel prévu">
          <p class="agri-value">{{ agri.frost }}</p>
          <ClassicBadge :level="agri.frostBadge" :text="agri.frostStatus"/>
        </SubCard>
       <SubCard text="ETP">
          <p class="agri-value">{{ agri.etp }}</p>
         <ClassicBadge :level="agri.etpBadge" :text="agri.etpStatus"/>
        </SubCard>
     </GridContainer>
    </ClassicCard>
  </div>
</template>

<script setup lang="ts">
import ClassicCard from "../core/containers/ClassicCard.vue";
import ListColumn from "../core/containers/ListColumn.vue";
import DayLineInfo from "../core/meteo/DayLineInfo.vue";
import GridContainer from "../core/containers/GridContainer.vue";
import SubCard from "../core/containers/SubCard.vue";
import ClassicBadge from "../core/Label/ClassicBadge.vue";
import ElevatedCard from "../core/containers/ElevatedCard.vue";
import SeparatedRowColumnContainer from "../core/containers/SeparatedRowColumnContainer.vue";
import ActualTopInfo from "../core/meteo/ActualTopInfo.vue";
import IconWeather from "../core/meteo/IconWeather.vue";


const current = {
  temp: 17,
  desc: 'Partiellement nuageux',
  wind: 12,
  humidity: 78,
  emoji: '⛅',
}

const forecast = [
  { label: 'Auj.', emoji: '⛅', max: 17, min: 11, rain: 0 },
  { label: 'Jeu.',  emoji: '🌧️', max: 13, min: 8,  rain: 6 },
  { label: 'Ven.', emoji: '🌧️', max: 11, min: 7,  rain: 14 },
  { label: 'Sam.', emoji: '⛅', max: 16, min: 9,  rain: 1 },
  { label: 'Dim.', emoji: '☀️', max: 19, min: 10, rain: 0 },
]

const agri = {
  frost: 'Non',
  frostStatus: 'Sûr',
  frostBadge: 0,
  etp: '2.4 mm/j',
  etpStatus: 'Modérée',
  etpBadge: 3,
}
</script>

<style scoped lang="scss">

.weather-hero {
  background: linear-gradient(135deg, #e8f0fe 0%, #f0e6ff 50%, #e6f7ff 100%);
  border: none;
}






.agri-card {
  background: var(--bg-elevated);
  border-radius: var(--radius-sm);
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.agri-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}

.agri-value {
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}
</style>
