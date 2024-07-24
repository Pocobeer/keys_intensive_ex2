<template>
    <v-form>
        <v-text-field v-model="name" label="Имя" required></v-text-field>
        <v-text-field v-model="age" label="Возраст" required></v-text-field>
        <v-text-field v-model="experience" label="Опыт" required></v-text-field>
        <v-text-field v-model="rating" label="Рейтинг" required></v-text-field>
        <v-btn @click="submit">Создать</v-btn>
        <v-btn @click="$emit('close')">Отменить</v-btn>
    </v-form>
</template>

<script>
export default {
    name: "CreateForm",
    data() {
        return {
            name: '',
            age: '',
            experience: '',
            rating: ''
        };
    },
    methods: {
        submit() {
            const newPovar = {
                name: this.name,
                age: this.age,
                experience: this.experience,
                rating: this.rating
            };
            this.$emit('create', newPovar);
            this.name = '';
            this.age = '';
            this.experience = '';
            this.rating = '';
        }
    }
};
</script>

<style scoped>
/* Стили для формы создания */
</style>