<script>
import DishCreateForm from "@/components/DishCreateForm.vue";
import DishesList from "@/components/DishesList.vue";

export default {
  name: "DishAppContent",
  components: { DishCreateForm, DishesList },
  data() {
    return {
      dishes: [],
      showCreateForm: false,
      selectSort: '',
      sortOptions: [
        { value: 'dish_name', name: 'По имени' },
        { value: 'dish_price', name: 'По цене' },
      ],
      searchText:''
    }
  },
  mounted() {
    this.fetchDishes();
  },
  methods: {
    async fetchDishes() {
      try {
        const response = await this.$ajax.get('api/dishes/');
        console.log('API Response:', response.data);

        if (Array.isArray(response.data)) {
          this.dishes = response.data.map(dish => ({
            id: dish.id,
            dish_name: dish.dish_name,
            dish_price: dish.dish_price,
            dish_rating: dish.dish_rating
          }));
          console.log('Transformed Dishes:', this.dishes);
        } else {
          console.error('Expected array but got:', response.data);
          this.dishes = [];
        }
      } catch (error) {
        console.error('Error fetching dishes:', error);
        this.dishes = [];
      }
    },
    createDish(data) {
      console.log('New Dish:', data);
      this.dishes.push(data);
    },
    async removeDish(dish) {
      const url = `api/dishes/${dish.id}/`;
      console.log('Deleting Dish URL:', url);

      try {
        await this.$ajax.delete(url);
        this.dishes = this.dishes.filter(elem => elem.id !== dish.id);
      } catch (error) {
        console.error('Error removing dish:', error.response ? error.response.data : error.message);
      }
    }
  },
  computed: {
    sortedDishes() {
      return [...this.dishes].sort((pov1, pov2) => {
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
      return this.sortedDishes.filter(dish=>{
        const dishName = dish.dish_name || '';
        return dishName.toLowerCase().includes(this.searchText.toLowerCase())
      })
    }
  }
}
</script>

<template>
  <div>
    <div class="x-content">
      <x-dialog v-model="showCreateForm">
        <dish-create-form @create="createDish"></dish-create-form>
      </x-dialog>
      <div class="x-actions">
        <x-select :options="sortOptions" v-model="selectSort"></x-select>
        <x-input v-model="searchText" style = "margin-left: 10px; width: 100%; margin-right: 10px;" placeholder = "Поиск"></x-input>
        <x-button @click="showCreateForm = true" style="margin-left: auto; margin-right: 10px">
          Добавить блюдо
        </x-button>
      </div>
      <dishes-list :dishes="sortedAndSearched" @remove="removeDish"></dishes-list>
    </div>
  </div>
</template>

<style scoped>
.x-actions {
  display: flex;
  margin-top: 15px;
}
</style>