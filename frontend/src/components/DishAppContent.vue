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
      ]
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
      return [...this.dishes].sort((a, b) => {
        const key = this.selectSort;
        if (key === 'dish_name') {
          return a[key].localeCompare(b[key]);
        }
        return a[key] - b[key];
      });
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
        <x-button @click="showCreateForm = true" style="margin-left: auto; margin-right: 10px">
          Добавить блюдо
        </x-button>
      </div>
      <dishes-list :dishes="sortedDishes" @remove="removeDish"></dishes-list>
    </div>
  </div>
</template>

<style scoped>
.x-actions {
  display: flex;
  margin-top: 15px;
}
</style>