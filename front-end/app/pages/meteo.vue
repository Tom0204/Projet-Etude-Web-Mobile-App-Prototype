<template>
  <div class="page-content">
    <MeteoWidget />
  </div>
</template>

<script setup lang="ts">

import MeteoWidget from "../components/contexts/MeteoWidget.vue";
import {definePageMeta} from "../../.nuxt/imports";


definePageMeta({ layout: 'default' })
</script>
