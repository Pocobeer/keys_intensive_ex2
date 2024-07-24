<script>
import AppContent from "@/components/AppContent.vue";
import AppHeader from "@/components/AppHeader.vue";
import IngredientAppContent from "@/components/IngredientAppContent.vue";

export default {
  components: {
    AppHeader, AppContent, IngredientAppContent
  },
  name: "App",
}
</script>

<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<style>
body {
  background-color: #f6f6f6;
}

.main-block {
  width: 60%;
  margin: 0 auto;
}

.warning {
  background-color: orangered !important;
  border-color: orangered !important;
}

.success {
  background-color: green !important;
  border-color: green !important;
}
</style>