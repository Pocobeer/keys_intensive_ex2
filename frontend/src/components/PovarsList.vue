<script>
export default {
  props: {
    povars: {
      type: Array,
      required: true
    }
  },
  name: "PovarsList"
}
</script>

<template>
  <div>
    <div v-if="povars.length > 0">
      <div class="povar" v-for="povar in povars" :key="povar.id">
        <div class="x-item">
          <div>
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
    </div>
    <div v-else><p>Повара отсутствуют</p></div>
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
