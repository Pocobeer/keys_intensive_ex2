<script>
export default {
  props: {
    ingredients: {
      type: Array,
      required: true
    }
  },
  name: "IngredientsList"
}
</script>

<template>
  <div>
    <div v-if="ingredients.length > 0">
      <div class="ingredient" v-for="ingredient in ingredients" :key="ingredient.id">
        <div class="x-item">
          <div>
            <p><strong>id: </strong> {{ ingredient.id }}</p>
            <p><strong>Название: </strong> {{ ingredient.name }}</p>
            <p><strong>Цена: </strong> {{ ingredient.price }}</p>
            <p><strong>Тип: </strong> {{ ingredient.type }}</p>
          </div>
          <div class = "x-item__actions">
            <x-button class = "warning" @click="$emit('remove', ingredient)">Удалить</x-button>
          </div>
        </div>
      </div>
    </div>
    <div v-else><p>Ингридиенты отсутствуют</p></div>
  </div>
</template>

<style scoped>
.x-item {
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 10px;
  padding-right: 10px;
  margin-top: 15px;
  border-radius: 5px;
  background: white;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.x-item__actions {
  display: flex;
  align-self: end;
}

.x-item p {
  margin-top: 5px;
  margin-bottom: 5px;
}


</style>
