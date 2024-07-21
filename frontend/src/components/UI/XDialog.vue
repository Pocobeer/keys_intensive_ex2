<script>
export default {
  name: "XDialog",
  props: {
    value: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<template>
<div class="x-dialog" v-if="value===true" @click="$emit('input', false)">
  <div class="x-dialog--content" @click.stop>
    <slot></slot>
  </div>
</div>
</template>

<style scoped>
.x-dialog {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgba(0,0,0,0.5);
  position: fixed;
  display: flex;
}

.x-dialog--content {
  margin: auto;
  background: white;
  border-radius: 10px;
  min-height: 50px;
  min-width: 300px;
  padding: 20px;
}
</style>
