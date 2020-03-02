<template>
  <div class="folder">
    <div class="title" @click="()=>{hidden = !hidden;}">
      <div class="icon">
        <img src="@/assets/btn-drop.svg" alt="dropdown">
      </div>
      <div class="name">
        {{name}}
      </div>
    </div>
    <router-link tag="div" class="item" v-for="(file, id) in files" :key="id"
      :class="{
        hidden,
        new: file.version==$route.query.v,
      }"
      :to="{
        path: `${$route.matched[0].path}/${file.folder||uuid}/${file.folder?file.id:id}`,
        query: {
          ...$route.query,
          hide: isMobile()?'true':$route.query.hide
        }
      }" append>
      <div class="icon" v-if="file.folder">
        <img :src="`./images/characters/${file.folder}_s.png`" :alt="file.folder">
      </div>
      <div class="name">
        {{file.name}}
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Folder',
  props: ['uuid', 'name', 'files'],
  data() {
    return {
      hidden: true
    };
  },
  methods: {
    isMobile() {
      return window.outerWidth<767;
    }
  }
}
</script>

<style lang="scss" scoped>
.folder {
  margin: 6.4px;
  cursor: pointer;
  user-select: none;
  word-break: break-all;
  .icon {
    width: 26px;
    display: flex;
    justify-content: center;
  }
  .title {
    display: flex;
    padding: 3.2px 6.4px;
    align-items: center;
    background: #ffffff08;
    .icon img {
      height: .8em;
    }
  }
  .item {
    display: flex;
    margin-bottom: 1px;
    padding: 3.2px 6.4px;
    background: #ffffff10;
    .icon img {
      height: 1em;
    }
  }
  .router-link-active {
    color: yellow;
  }
}
</style>
