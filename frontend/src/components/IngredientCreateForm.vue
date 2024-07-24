<template>
  <div>
    <form class="x-form" @submit.prevent="createIngredient">
      <h1>Добавить ингредиент</h1>
      <x-input v-model="ingredient.name" placeholder="Имя"></x-input>
      <x-input v-model="ingredient.price" placeholder="Цена"></x-input>
      <x-input v-model="ingredient.type" placeholder="Тип (от 1 до 3)"></x-input>
      <x-button @create="createIngredient" style="width: max-content; align-self: flex-end;" class="success">Добавить ингредиент</x-button>
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
