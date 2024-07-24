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
  <select :value="value" class="x-select" @change="$emit('input', $event.target.value)">
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
.x-select {
  font-size: 16px;
  padding: 14px;
  border: 1px solid #bdbdbd;
  border-radius: 5px;
}

.x-select:focus {
  border-color: #bdbdbd;
  box-shadow: 0 0 0 0.1rem rgba(158,158,158,0.25);
}

</style>
