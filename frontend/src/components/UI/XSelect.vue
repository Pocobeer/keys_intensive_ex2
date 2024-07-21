<script>
export default {
  name: "XSelect",
  props: {
    value: {
      type: String,
    },
    options: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<template>
  <select :value="value" @change="$emit('input', $event.target.value)">
    <option disabled value="">Выберите из списка</option>
    <option v-for="option in options"
            :key="option.value"
            :value="option.value"
    >
      {{ option.name }}
    </option>
  </select>
</template>

<style scoped>

</style>
