<template>
    <v-app-bar app>
        <v-toolbar-title>Иванов Владимир</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn @click="logout">Выход</v-btn>
        <v-btn @click="navigateTo('/PovarPage')">Поварs</v-btn>
        <v-btn @click="navigateTo('/DishPage')">Блюда</v-btn>
        <v-btn @click="navigateTo('/IngredientPage')">Ингредиенты</v-btn>
        <v-btn @click="navigateTo('/BeautifulPage')">vuetify</v-btn>
    </v-app-bar>
</template>

<script>
export default {
    name: "VueAppHeader",
    methods: {
        logout() {
            this.$store.commit('auth/removeToken');
            this.$router.push('/login');
        },
        navigateTo(route) {
            this.$router.push(route);
        }
    }
};
</script>

<style scoped>
/* Стили для заголовка */
</style>