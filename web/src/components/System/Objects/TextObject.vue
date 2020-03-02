<template>
  <div class="text">
    <div class="name">{{name}}</div>
    <div class="content" v-html="content"/>
  </div>
</template>

<script>
export default {
  name: 'TextObject',
  props: ['name', 'content']
}
</script>

<style lang="scss" scoped>
.text {
  padding: 16px;
  border-radius: 5px;
  margin-bottom: 16px;
  background: #ffffff08;
}
</style>