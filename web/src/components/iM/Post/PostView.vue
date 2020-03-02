<template>
  <div class="view">
    <div class="avatar">
      <img :src="`./images/imavatars/${avatar}.png`" :alt="avatar"/>
      <div class="name">{{name}}</div>
    </div>
    <div class="content">
      <div class="title">
        {{title}}
      </div>
      <div class="text" v-html="text"/>
      <div class="image" v-for="item in attachments" :key="`${pid}-attach-${item}`">
        <img
          :src="`./images/imfiles/${item.toLowerCase()}.jpg`"
          :alt="item"
          @click="viewImage(`./images/imfiles/${item.toLowerCase()}.jpg`)">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostView',
  props: ['avatar', 'name', 'pid', 'title', 'text', 'attachments'],
  methods: {
    viewImage(url) {
      window.open(url);
    }
  }
}
</script>

<style lang="scss" scoped>
.view {
  margin: 12px;
  padding: 12px;
  display: flex;
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
    white-space: pre-line;
    padding: 0 16px;
    .title {
      margin-bottom: 1em;
      font-size: 1.2em;
      color: #00b0ff;
    }
    .image {
      margin-top: 20px;
      img {
        width: 12em;
        max-width: 100%;
        cursor: pointer;
      }
    }
  }
}
</style>
