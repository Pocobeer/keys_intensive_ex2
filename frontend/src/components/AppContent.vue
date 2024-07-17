<script>
import CreateForm from "@/components/CreateForm.vue";
import PovarsList from "@/components/PovarsList.vue";

export default {
  name: "AppContent",
  components: {CreateForm, PovarsList},
  data() {
    return {
      povars: [
        {id: 1, name: "Владимир", experience: 5, rating: "5", age: 19},
      ],
    }
  },
  methods: {
    createPovar(data) {
      console.log(data)
      this.povars.push(data)
    }
  }
}
</script>

<template>
  <div>
    <div class="x-content">
      <create-form @create="createPovar"></create-form>
      <povars-list :povars="povars"></povars-list>
    </div>
  </div>
</template>

<style scoped>

</style>
