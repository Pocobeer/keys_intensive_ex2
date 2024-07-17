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
    <div class="povar" v-for="povar in povars">
      <div class="x-item">
        <p><strong>id: </strong> {{ povar.id }}</p>
        <p><strong>Имя: </strong> {{ povar.name }}</p>
        <p><strong>Опыт: </strong> {{ povar.experience }}</p>
        <p><strong>Рейтинг: </strong> {{ povar.rating }}</p>
        <p><strong>Возраст: </strong> {{ povar.age }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.x-item {
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 10px;
  margin-top: 15px;
  border-radius: 5px;
  background: white;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.2);
}

.x-item p {
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>
