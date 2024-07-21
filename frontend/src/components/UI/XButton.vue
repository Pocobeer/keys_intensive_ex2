<script>
export default {
  name: "XButton"
}
</script>

<template>
  <button class="x-btn" v-on="$listeners">
    <slot></slot>
  </button>
</template>

<style scoped>
.x-btn {
  border: 1px solid #3d6fef;
  background-color: transparent;
  color: #3d6fef;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}
</style>
