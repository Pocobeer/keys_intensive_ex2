<script>
import IngredientCreateForm from "@/components/IngredientCreateForm.vue";
import IngredientsList from "@/components/IngredientsList.vue";

export default {
  name: "IngredientAppContent",
  components: {IngredientCreateForm, IngredientsList},
  data() {
    return {
      ingredients: [],
      showCreateForm: false,
      selectSort: '',
      sortOptions: [
        {value: 'name', name: 'По имени'},
        {value: 'experience', name: 'По цене'},
      ],
      searchText: ''
    }
  },
  mounted(){
    this.$ajax.get('api/ingredients/')
      .then(response => {
        console.log('API Response:', response.data);

        // Извлекаем массив данных из свойства `results`
        const results = response.data.results;
        console.log('Extracted Results:', results);

        if (Array.isArray(results)) {
          // Преобразуем данные в формат, ожидаемый компонентом
          this.ingredients = results.map(ingredient => ({
            id: ingredient.id,
            name: ingredient.ingredient_name,
            price: ingredient.ingredient_price,
            type: ingredient.ingredient_type
          }));
          
          console.log('Transformed Ingredients:', this.ingredients);
        } else {
          console.error('Expected array but got:', results);
          this.ingredients = [];
        }
      })
      .catch(error => {
        console.error('Error fetching ingredients:', error);
        this.ingredients = [];
      });
  },
  methods: {
    createIngredient(data) {
      console.log(data)
      this.ingredients.push(data)
    },
    removeIngredient(ingredient  ){
      const url = `api/ingredients/${ingredient.id}/`;
      console.log('Deleting Ingredient URL:', url);

      this.$ajax.delete(url)
        .then(() => {
          this.ingredients = this.ingredients.filter(elem => elem.id !== ingredient.id);
        })
        .catch(error => {
          console.error('Error removing ingredient:', error.response ? error.response.data : error.message);
        });
    }
  },
  computed: {
    sortedIngredients() {
      return [...this.ingredients].sort((pov1, pov2) => {
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
      return this.sortedIngredients.filter(dish => dish.name.toLowerCase().includes(this.searchText.toLowerCase()))
    }
  }
}
</script>

<template>
  <div>
    <div class="x-content">
      <x-dialog v-model="showCreateForm">
        <ingredient-create-form @create="createIngredient"></ingredient-create-form>
      </x-dialog>
      <div class = "x-actions">
        <x-select :options="sortOptions" v-model="selectSort"></x-select>
        <x-input v-model="searchText" style = "margin-left: 10px; width: 100%; margin-right: 10px;" placeholder = "Поиск"></x-input>
        <x-button @click="showCreateForm = true" 
        style="margin-left: auto; margin-right: 10px">Добавить ингредиент
      </x-button>
      </div>
      <ingredients-list :ingredients="sortedAndSearched" @remove="removeIngredient"></ingredients-list>
    </div>
  </div>
</template>

<style scoped>
.x-actions {
  display: flex;
  margin-top: 15px;
}
</style>