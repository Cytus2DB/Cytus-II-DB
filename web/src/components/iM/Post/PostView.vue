<template>
  <div class="view">
    <div class="avatar">
      <img :src="`./images/imavatars/${avatar}.png`" :alt="avatar" />
      {{name}}
    </div>
    <div class="content">
      <div class="title">
        {{title}}
      </div>
      <div class="text" v-html="text"/>
      <div v-for="item in attachments" :key="`${pid}-attach-${item}`">
        <img
          :src="`./images/imfiles/${item.toLowerCase()}.jpg`"
          :alt="item"
          @click="viewImage(item.toLowerCase())">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostView",
  props: ["avatar", "name", "pid", "title", "text", "attachments"],
  methods: {
    viewImage(id) {
      window.open(`./images/imfiles/${id}.jpg`);
    }
  }
}
</script>

<style lang="scss" scoped>
.view {
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
    .image {
      margin-top: 20px;
      img {
        height: 8em;
        cursor: pointer;
      }
    }
  }
}
</style>
