<template>
    <div>
      <form class="x-form" @submit.prevent="createIngredient">
        <h1>Добавить ингредиент</h1>
        <input v-model="ingredient.name" placeholder="Имя" class="x-input">
        <input v-model="ingredient.price" placeholder="Цена" class="x-input">
        <input v-model="ingredient.type" placeholder="Тип (от 1 до 3)" class="x-input">
        <button @create="createIngredient" style="width: max-content; align-self: flex-end;" class="success">Добавить ингредиент</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "IngredientCreateForm",
    data() {
      return {
        ingredient: {
          name: '',
          price: '',
          type: ''
        }
      }
    },
    methods: {
      createIngredient() {
        const payload = {
          ingredient_name: this.ingredient.name,
          ingredient_price: parseFloat(this.ingredient.price),
          ingredient_type: this.ingredient.type
        };
  
        this.$ajax.post('api/ingredients/', payload).then(response => {
          const {data} = response
          this.$emit('create', data)
        })
  
        // Очистка полей после отправки формы
        this.ingredient.name = '';
        this.ingredient.price = '';
        this.ingredient.type = '';
      }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .x-form {
    background: white;
    padding: 1px 10px 10px 10px;
    margin-top: 15px;
    display: flex;
    flex-direction: column;
  }
  </style>
  