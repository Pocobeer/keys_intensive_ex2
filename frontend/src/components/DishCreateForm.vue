<template>
  <div>
    <form class="x-form" @submit.prevent="createDish">
      <h1>Добавить блюдо</h1>
      <x-input v-model="dish.dish_name" placeholder="Название"></x-input>
      <x-input v-model="dish.dish_price" type="number" placeholder="Цена" ></x-input>
      <x-input v-model="dish.dish_rating" type="number" placeholder="Рейтинг" ></x-input>
      <x-input v-model="dish.dish_ingredients" placeholder="Ингредиенты (через запятую)"></x-input>
      <x-input v-model="dish.dish_povars" placeholder="Повар (ID)" ></x-input>
      <x-button type="submit" style="width: max-content; align-self: flex-end;" class="success">Добавить блюдо</x-button>
      <x-button @click="hello" type = "button">Миксин</x-button>
    </form>
  </div>
</template>

<script>
import XMixin from '@/mixins/XMixin';
import XButton from './UI/XButton.vue';

export default {
  components: {
    XButton
  },
  mixins: [XMixin],
  name: "DishCreateForm",
  data() {
    return {
      dish: {
        dish_name: '',
        dish_price: '',
        dish_rating: '',
        dish_ingredients: '', // Это должен быть список или строка
        dish_povars: '' // Это должен быть ID повара
      }
    }
  },
  mounted(){
    console.log('aaaaa')
  },
  methods: {
    createDish() {
      const payload = {
        dish_name: this.dish.dish_name,
        dish_price: parseFloat(this.dish.dish_price),
        dish_rating: parseFloat(this.dish.dish_rating),
        dish_ingredients: this.dish.dish_ingredients.split(',').map(ingredient => ingredient.trim()), // Преобразуем строку в массив
        dish_povars: parseInt(this.dish.dish_povars) // Преобразуем в число
      };

      this.$ajax.post('api/dishes/', payload).then(response => {
        const { data } = response;
        this.$emit('create', data);
      }).catch(error => {
        console.error('Error creating dish:', error.response ? error.response.data : error.message);
      });

      // Очистка полей после отправки формы
      this.dish.dish_name = '';
      this.dish.dish_price = '';
      this.dish.dish_rating = '';
      this.dish.dish_ingredients = '';
      this.dish.dish_povars = '';
    }
  }
}
</script>

<style scoped>
.x-form {
  background: white;
  padding: 10px;
  margin-top: 15px;
  display: flex;
  flex-direction: column;
}
</style>