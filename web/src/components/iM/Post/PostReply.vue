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
  name: 'PostReply',
  props: ['avatar', 'name', 'text']
}
</script>

<style lang="scss" scoped>
.reply {
  display: flex;
  margin: 1em;
  padding: 1em;
  background: #ffffff08;
  border-radius: 5px;
  .avatar {
    width: 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
    word-break: break-all;
    text-align: center;
    img {
      width: 64px;
    }
  }
  .content {
    white-space: pre-line;
    padding: 0em 1em 1em 1em;
    .title {
      margin-bottom: 1em;
      font-size: 1.2em;
      color: #00b0ff;
    }
  }
}
</style>
