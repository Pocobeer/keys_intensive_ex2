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
      showCreateForm: false,
      selectSort: ' ',
      sortOptions: [
        {value: 'name', name: 'По имени'},
        {value: 'experience', name: 'По опыту'},
        {value: 'rating', name: 'По рейтингу'},
      ]
    }
  },
  methods: {
    createPovar(data) {
      console.log(data)
      this.povars.push(data)
    },
    removePovar(povar){
      this.povars = this.povars.filter(elem => elem.id !== povar.id)
    }
  },
  computed: {
    sortedPovars(){
      return [...this.povars].sort(
        (pov1, pov2) => pov1[this.selectSort]?.localeCompare(pov2[this.selectSort])
      )
    }
  }
}
</script>

<template>
  <div>
    <div class="x-content">
      <x-dialog v-model="showCreateForm">
        <create-form @create="createPovar"></create-form>
      </x-dialog>
      <div class = "x-actions">
        <x-select :options="sortOptions" v-model="selectSort"></x-select>
        <x-button @click="showCreateForm = true" 
        style="margin-left: auto; margin-right: 10px">Добавить повара
      </x-button>
      </div>
      <povars-list :povars="sortedPovars" @remove="removePovar"></povars-list>
    </div>
  </div>
</template>

<style scoped>
.x-actions {
  display: flex;
  margin-top: 15px;
}
</style>
