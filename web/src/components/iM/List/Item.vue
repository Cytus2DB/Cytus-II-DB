<template>
  <router-link tag="div" class="item" :to="item.id" append>
    <div class="avatar">
      <img :src="`./images/imavatars/${item.avatar}.png`" :alt="item.avatar" />
      {{item.name}}
    </div>
    <div class="header">
      <div :class="{ title:true, new: item.version==$route.query.v }">
        {{item.title[parseInt($t('code'))]}}
      </div>
      <div class="info">
        <div class="likes">
          <img src="@/assets/im-likes.svg" alt="likes">
          {{item.likes}}
        </div>
        <div class="replies">
          <img src="@/assets/im-replies.svg" alt="reply">
          {{item.replies}}
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "Item",
  props: ["item"],
  mounted() {
    if (this.$route.hash==`#${this.item.id}`){
      this.$el.scrollIntoView();
    }
  }
}
</script>

<style lang="scss" scoped>
.list .item {
  cursor: pointer;
}
.item {
  display: flex;
  margin: 1em;
  padding: 1em;
  background: #ffffff08;
  border-radius: 5px;
  .avatar {
    width: 120px;
    display: flex;
    flex-direction: column;
    align-items: center;
    word-break: break-all;
    text-align: center;
    img {
      width: 64px;
    }
  }
  .header {
    width: 100%;
    display: flex;
    flex-direction: column;
    .title {
      margin: 0em 1.2em 3em 1.2em;
      word-break: break-word;
    }
    .info {
      display: flex;
      justify-content: flex-end;
      .likes, .replies {
        padding: 10px;
        font-size: 1.1em;
        img {
          height: 0.8em;
        }
      }
    }
  }
}
</style>