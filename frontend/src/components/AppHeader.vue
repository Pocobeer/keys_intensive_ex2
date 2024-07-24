<script>
export default {
    name: "AppHeader",
    methods:{
        logout(){
            this.$store.commit('auth/removeToken')
            this.$router.push('/login')
        },
        povarpage(){
            this.$router.push('/PovarPage')
        },
        dishpage(){
            this.$router.push('/DishPage')
        },
        ingredientpage(){
            this.$router.push('/IngredientPage')
        }
    }
}
</script>

<template>
    <div class ="x-header">
        <strong>Иванов Владимир</strong>
        <x-button @click="povarpage">Поварs</x-button>
        <x-button @click="dishpage">Блюда</x-button>
        <x-button @click="ingredientpage">Ингредиенты</x-button>
        <x-button @click="logout">Выход</x-button>
    </div>
</template>

<style scoped>
.x-header {
    padding: 10px;
    display: flex;
    justify-content: space-between;
    border-radius: 5px;
    background: white;
    box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.2);

}
</style>