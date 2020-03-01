<template>
  <div class="reply">
    <div class="avatar">
      <img :src="`./images/imavatars/${avatar}.png`" :alt="avatar" />
      <div class="name">{{name}}</div>
    </div>
    <div class="content">
      <div class="text" v-html="text"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostReply',
  props: ['avatar', 'name', 'text']
}
</script>

<style lang="scss" scoped>
.reply {
  display: flex;
  margin: 12px;
  padding: 12px;
  border-radius: 5px;
  background: #ffffff08;
  .avatar {
    min-width: 108px;
    max-width: 108px;
    user-select: none;
    text-align: center;
    img {
      width: 64px;
    }
    .name {
      word-break: break-all;
    }
  }
  .content {
    padding: 0 12px;
    white-space: pre-line;
  }
}
</style>
