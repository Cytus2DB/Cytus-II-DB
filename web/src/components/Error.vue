<template>
  <div class="error">
    {{ error }}
  </div>
</template>

<script>
export default {
  name: 'Error',
  props: ["error"]
}
</script>

<style lang="scss" scoped>
.error {
  margin: 20px;
  color: red;
}
</style>
