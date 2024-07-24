<script>
export default {
  props: {
    ingredients: {
      type: Array,
      required: true
    }
  },
  name: "IngredientsList",
  data(){
    return {
      isActive:0,
    }
  }
}
</script>

<template>
  <div>
    <div v-show="ingredients.length > 0">
      <transition-group name = "students-list">
        <div class="ingredient" v-for="ingredient in ingredients" :key="`ingredient-${ingredient.id}`">
          <div>
            <div :class="[{'x-active': isActive === ingredient.id}, 'x-item']" @click="isActive = ingredient.id">
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
      </transition-group>
    </div>
    <transition name="fade">
      <div v-show="ingredients.length === 0" style="color: orangered">
        <p>Список ингредиентов пуст</p>
      </div>
    </transition>
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

.students-list-enter-active, students-list-leave-active {
  transition: all 1s;
}

.students-list-enter, students-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.students-list-move {
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