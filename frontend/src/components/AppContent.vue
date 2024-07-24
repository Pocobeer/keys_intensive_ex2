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
      selectSort: '',
      sortOptions: [
        {value: 'name', name: 'По имени'},
        {value: 'experience', name: 'По опыту'},
      ]
    }
  },
  mounted(){
    this.$ajax.get('api/povars/')
      .then(response => {
        console.log('API Response:', response.data);

        // Извлекаем массив данных из свойства `results`
        const results = response.data.results;
        console.log('Extracted Results:', results);

        if (Array.isArray(results)) {
          // Преобразуем данные в формат, ожидаемый компонентом
          this.povars = results.map(povar => ({
            id: povar.id,
            name: povar.Povar_name,
            experience: povar.Povar_experience,
            rating: povar.Povar_rating,
            age: povar.Povar_age
          }));
          
          console.log('Transformed Povars:', this.povars);
        } else {
          console.error('Expected array but got:', results);
          this.povars = [];
        }
      })
      .catch(error => {
        console.error('Error fetching povars:', error);
        this.povars = [];
      });
  },
  methods: {
    createPovar(data) {
      console.log(data)
      this.povars.push(data)
    },
    removePovar(povar){
      const url = `api/povars/${povar.id}`;
      console.log('Deleting Povar URL:', url);

      this.$ajax.delete(url)
        .then(() => {
          this.povars = this.povars.filter(elem => elem.id !== povar.id);
        })
        .catch(error => {
          console.error('Error removing povar:', error.response ? error.response.data : error.message);
        });
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