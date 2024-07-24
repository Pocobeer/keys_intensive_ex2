<script>

import {mapActions} from "vuex";

export default {
  name: "LoginForm",
  data() {
    return {
      username: '',
      password: '',
      showDialog: true,
    }
  },
  methods: {
    ...mapActions(['auth/login']),
    loginUser() {
      this['auth/login']({username: this.username, password: this.password, router: this.$router})
    }
  }
}
</script>

<template>
  <x-dialog v-model="showDialog">
    <form @submit.prevent="loginUser" class="x-login-form">
      <x-input type="text" v-model="username" placeholder="Username" required></x-input>
      <x-input type="text" v-model="password" placeholder="Пароль" required></x-input>
      <x-button type="submit">Войти</x-button>
    </form>
  </x-dialog>
</template>

<style scoped>
.x-login-form {
  display: flex;
  flex-direction: column;
}
</style>