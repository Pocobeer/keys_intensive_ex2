<script>
export default {
  name: "XInput",
  props: {
    modelValue: [String, Number],
  },
  methods: {
    updateInput(event) {
      this.$emit('input', event.target.value)
    }
  }
}
</script>

<template>
  <input :value="modelValue" @input="updateInput" type="text" placeholder="Имя" class="x-input">
</template>

<style scoped>
.x-input {
  height: 25px;
  padding: 5px;
  margin-bottom: 10px;
  border: 1px solid #bdbdbd;
  font-size: 16px;
  border-radius: 0.25rem;
  outline: 0;
}

.x-input:focus {
  border-color: #bdbdbd;
  box-shadow: 0 0 0 0.1rem rgba(158, 158, 158, 0.25);
}
