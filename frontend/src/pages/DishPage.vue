<script>
import AppHeader from "@/components/AppHeader.vue";
import DishAppContent from "@/components/DishAppContent.vue";

export default {
  name: "DishPage",
  components: {AppHeader, DishAppContent}
}
</script>

<template>
  <div class="main-block">
    <app-header></app-header>
    <dish-app-content></dish-app-content>
  </div>
</template>

<style scoped>

</style>
