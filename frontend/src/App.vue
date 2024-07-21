<script>
import AppContent from "@/components/AppContent.vue";
import AppHeader from "@/components/AppHeader.vue";

export default {
  components: {
    AppHeader, AppContent
  },
  name: "App",
  data() {
    return {
      name: '',
      experience: '',
      rating: '',
      age: ''
    }
  },
}
</script>

<template>
  <div class="main-block">
    <app-header></app-header>
    <app-content></app-content>
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
