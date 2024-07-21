<script>
export default {
    name: "AppHeader"
}
</script>

<template>
    <div class ="x-header">
        <strong>Иванов Владимир</strong>
        <x-button>Выход</x-button>
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