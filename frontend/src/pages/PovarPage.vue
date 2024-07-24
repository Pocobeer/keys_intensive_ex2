<script>
import AppHeader from "@/components/AppHeader.vue";
import AppContent from "@/components/AppContent.vue";

export default {
  name: "PovarPage",
  components: {AppContent, AppHeader}
}
</script>

<template>
  <div class="main-block">
    <app-header></app-header>
    <app-content></app-content>
  </div>
</template>

<style scoped>

</style>
