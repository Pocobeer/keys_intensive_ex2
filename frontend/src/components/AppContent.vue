<script>
import CreateForm from "@/components/CreateForm.vue";
import PovarsList from "@/components/PovarsList.vue";

export default {
  name: "AppContent",
  components: {CreateForm, PovarsList},
  data() {
    return {
      povars: [],
      showCreateForm: false,
      selectSort: '',
      sortOptions: [
        {value: 'name', name: 'По имени'},
        {value: 'experience', name: 'По опыту'},
      ],
      searchText:''
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
      return [...this.povars].sort((pov1, pov2) => {
        const value1 = pov1[this.selectSort];
        const value2 = pov2[this.selectSort];

        // Проверка, что значения являются строками
        if (typeof value1 === 'string' && typeof value2 === 'string') {
          return value1.localeCompare(value2);
        }
        
        // Если значения не строки, просто сравниваем их напрямую
        return (value1 > value2) ? 1 : (value1 < value2) ? -1 : 0;
      });
    },
    sortedAndSearched(){
      return this.sortedPovars.filter(povar => povar.name.toLowerCase().includes(this.searchText.toLowerCase()))
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
        <x-input v-model="searchText" style = "margin-left: 10px; width: 100%; margin-right: 10px;" placeholder = "Поиск"></x-input>
        <x-button @click="showCreateForm = true" 
        style="margin-left: auto; margin-right: 10px">Добавить повара
      </x-button>
      </div>
      <povars-list :povars="sortedAndSearched" @remove="removePovar"></povars-list>
    </div>
  </div>
</template>

<style scoped>
.x-actions {
  display: flex;
  margin-top: 15px;
}
</style>