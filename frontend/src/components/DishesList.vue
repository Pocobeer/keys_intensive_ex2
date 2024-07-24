<script>
export default {
  props: {
    dishes: {
      type: Array,
      required: true
    }
  },
  name: "DishesList"
}
</script>

<template>
  <div>
    <div v-if="dishes.length > 0">
      <div class="dish" v-for="dish in dishes" :key="dish.id">
        <div class="x-item">
          <div>
            <p><strong>id: </strong> {{ dish.id }}</p>
            <p><strong>Название: </strong> {{ dish.dish_name }}</p>
            <p><strong>Цена: </strong> {{ dish.dish_price }}</p>
            <p><strong>Рейтинг: </strong> {{ dish.dish_rating }}</p>
          </div>
          <div class = "x-item__actions">
            <x-button class = "warning" @click="$emit('remove', dish)">Удалить</x-button>
          </div>
        </div>
      </div>
    </div>
    <div v-else><p>Блюда отсутствуют</p></div>
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
