<script>
export default {
  props: {
    dishes: {
      type: Array,
      required: true
    }
  },
  name: "DishesList",
  data(){
    return {
      isActive:0,
    }
  }
}
</script>

<template>
  <div>
    <div v-show="dishes.length > 0">
      <transition-group name = "dishes-list">
        <div class="dish" v-for="dish in dishes" :key="`dish-${dish.id}`">
          <div>
            <div :class="[{'x-active': isActive === dish.id}, 'x-item']" @click="isActive = dish.id">
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
      </transition-group>
    </div>
    <transition-group name="fade">
      <div v-show="dishes.length === 0" style="color: orangered">
        <p>Список блюд пуст</p>
      </div>
    </transition-group>
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

.dishes-list-enter-active, dishes-list-leave-active {
  transition: all 1s;
}

.dishes-list-enter, dishes-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.dishes-list-move {
  transition: transform 1s;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.x-active {
  background-color: orange !important;
}
</style>