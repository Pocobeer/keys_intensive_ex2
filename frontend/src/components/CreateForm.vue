<template>
  <div>
    <form class="x-form" @submit.prevent="createPovar">
      <h1>Добавить повара</h1>
      <input v-model="povar.name" placeholder="Имя" class="x-input">
      <input v-model="povar.experience" placeholder="Опыт" class="x-input">
      <input v-model="povar.rating" placeholder="Рейтинг" class="x-input">
      <input v-model="povar.age" placeholder="Возраст" class="x-input">
      <button @create="createPovar" style="width: max-content; align-self: flex-end;" class="success">Добавить повара</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "CreateForm",
  data() {
    return {
      povar: {
        name: '',
        experience: '',
        rating: '',
        age: ''
      }
    }
  },
  methods: {
    createPovar() {
      this.$emit('create', { 
        id: Date.now(),
        ...this.povar });
      // Очистка полей после отправки формы
      this.povar.name = '';
      this.povar.experience = '';
      this.povar.rating = '';
      this.povar.age = '';
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
