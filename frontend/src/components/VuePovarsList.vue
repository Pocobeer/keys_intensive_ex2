<template>
    <v-list>
        <v-list-item-group>
            <v-list-item v-for="povar in povars" :key="povar.id">
                <v-list-item-content>
                    <v-list-item-title>{{ povar.name }}</v-list-item-title>
                    <v-list-item-subtitle>Возраст: {{ povar.age }}</v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-actions>
                    <v-btn @click="$emit('remove', povar)" color="red">Удалить</v-btn>
                </v-list-item-actions>
            </v-list-item>
        </v-list-item-group>
    </v-list>
</template>

<script>
export default {
    name: "PovarsList",
    props: {
        povars: Array
    }
};
</script>

<style scoped>
/* Стили для списка поваров */
</style>