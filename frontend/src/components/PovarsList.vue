<script>
export default {
  props: {
    povars: {
      type: Array,
      required: true
    }
  },
  name: "PovarsList",
  data(){
    return{
      isActive: 0,
    }
  }
}
</script>

<template>
  <div>
    <div v-show="povars.length > 0">
      <transition-group name="povars-list">
        <div class="povar" v-for="povar in povars" :key="povar.id">
          <div>
            <div :class = "[{'x-active': isActive === povar.id}, 'x-item']" @click="isActive = povar.id">
              <p><strong>id: </strong> {{ povar.id }}</p>
              <p><strong>Имя: </strong> {{ povar.name }}</p>
              <p><strong>Опыт: </strong> {{ povar.experience }}</p>
              <p><strong>Рейтинг: </strong> {{ povar.rating }}</p>
              <p><strong>Возраст: </strong> {{ povar.age }}</p>
            </div>
            <div class = "x-item__actions">
              <x-button class = "warning" @click="$emit('remove', povar)">Удалить</x-button>
            </div>
          </div>
        </div>
      </transition-group>
    </div>
    <transition name="fade">
      <div v-show="povars.length === 0" style="color: orangered">
        <p>Список поваров пуст</p>
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

.povars-list-enter-active, povars-list-leave-active {
  transition: all 1s;
}

.povars-list-enter, povars-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.povars-list-move {
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