<template>
  <router-link tag="div" class="item" :to="{path:`/im/${item.id}`, query:$route.query}">
    <div class="avatar">
      <img :src="`./images/imavatars/${item.avatar}.png`" :alt="item.avatar"/>
      <div class="name">{{item.name}}</div>
    </div>
    <div class="header">
      <div class="title" :class="{ new: item.version==$route.query.v }">
        {{item.titles[parseInt($t('code'))]}}
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
  name: 'Item',
  props: ['item'],
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
  margin: 12px;
  padding: 12px;
  display: flex;
  user-select: none;
  border-radius: 5px;
  background: #ffffff08;
  .avatar {
    min-width: 108px;
    max-width: 108px;
    text-align: center;
    img {
      width: 64px;
    }
    .name {
      word-break: break-all;
    }
  }
  .header {
    width: 100%;
    display: flex;
    flex-direction: column;
    .title {
      min-height: 58px;
      word-break: break-word;
    }
    .info {
      display: flex;
      justify-content: flex-end;
      .likes {
        min-width: 72px;
      }
      .replies {
        min-width: 36px;
      }
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