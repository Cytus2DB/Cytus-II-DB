<template>
  <div class="reply">
    <div class="avatar">
      <img :src="`./images/imavatars/${avatar}.png`" :alt="avatar" />
      {{name}}
    </div>
    <div class="content">
      <div class="text" v-html="text"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostReply",
  props: ["avatar", "name", "text"]
}
</script>

<style lang="scss" scoped>

</style>
