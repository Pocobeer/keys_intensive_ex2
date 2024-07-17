<script>
import AppContent from "@/components/AppContent.vue";

export default {
  components: {
    AppContent
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
    <app-content></app-content>
  </div>

</template>

<style scoped>
body {
  background-color: #f6f6f6;
}

.main-block {
  width: 60%;
  margin: 0 auto;
}
</style>
