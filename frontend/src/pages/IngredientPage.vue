<script>
import AppHeader from "@/components/AppHeader.vue";
import IngredientAppContent from "@/components/IngredientAppContent.vue";

export default {
  name: "IngredientPage",
  components: {AppHeader, IngredientAppContent},
}
</script>

<template>
  <div class="main-block">
    <app-header></app-header>
    <ingredient-app-content></ingredient-app-content>
  </div>
</template>

<style scoped>

</style>
