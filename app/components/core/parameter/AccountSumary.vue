<script setup lang="ts">

import SmallLabel from "../Label/SmallLabel.vue";
import ClassicCard from "../containers/ClassicCard.vue";
import BoldTitleLabel from "../Label/BoldTitleLabel.vue";
import ElevatedCard from "../containers/ElevatedCard.vue";
</script>

<template>
  <ClassicCard title="Compte" class="account-container">
    <ElevatedCard  class="profile-row">
      <div class="avatar">U</div>
      <div class="profile-info">
        <BoldTitleLabel  text="User"/>
        <SmallLabel class="profile-email" text="user.user@sfrmail.fr"/>
        <span class="badge-plan">Plan Classic</span>
      </div>
      <button class="btn-modifier">Modifier</button>
    </ElevatedCard>

    <ElevatedCard class="stats-row">
      <div class="stat-item">
        <span class="stat-value">4</span>
        <SmallLabel text="Capteurs"/>
      </div>
      <div class="stat-item">
        <span class="stat-value">3</span>
        <SmallLabel text="Parcelles"/>
      </div>
      <div class="stat-item">
        <span class="stat-value">247</span>
        <SmallLabel text="Jours actif"/>
      </div>
    </ElevatedCard>

  </ClassicCard>
</template>

<style scoped lang="scss">



.account-container{
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* ── Profile ── */
.profile-row {
  display: flex;
  align-items: center;
  gap: 14px;
  //padding: 18px 16px 16px;
}

.avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #3a5a8a;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.profile-info {
  flex: 1;
  min-width: 0;
}

.profile-name {
  font-size: 17px;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.2;
}

.profile-email {

  color: var(--text-secondary);
}

.badge-plan {
  display: inline-block;
  margin-top: 6px;
  font-size: 11px;
  font-weight: 600;
  color: var(--blue);
  border: 1px solid rgba(79, 160, 247, 0.4);
  border-radius: 6px;
  padding: 1px 8px;
}

.btn-modifier {
  border: none;
  border-radius: 10px;
  color: var(--text-primary);
  font-size: 15px;
  font-weight: 600;
  padding: 9px 18px;
  cursor: pointer;
  flex-shrink: 0;
  transition: background 0.15s;

  &:hover{
    background: #585654;

  }
}

.btn-modifier:active {
  background: #3a3a3c;
}



.stats-row {
  display: flex;
  align-items: center;
  padding: 14px 0;
}

.stat-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.stat-value {
  font-size: 20px;
  font-weight: 700;
  color: var(--text-primary);
}




</style>