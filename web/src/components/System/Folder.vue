<template>
  <div class="folder">
    <div class="title" @click="()=>{hidden = !hidden;}">
      <img src="@/assets/btn-drop.svg" alt="dropdown">
      {{name}}
    </div>
    <router-link tag="div" class="item" v-for="(file, id) in files" :key="id"
      :class="{
        hidden,
        new: file.version==$route.query.v,
      }"
      :to="{
        path: `${$route.matched[0].path}/${uuid}/${id}`,
        query: {
          ...$route.query,
          hide: isMobile()?'true':$route.query.hide
        }
      }" append>
      {{file.name}}
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
  .title {
    display: flex;
    padding: 3.2px 6.4px;
    align-items: center;
    background: #ffffff08;
    img {
      height: .8em;
      padding-right: 6.4px;
    }
  }
  .item {
    padding: 3.2px 6.4px;
    margin-bottom: 1px;
    background: #ffffff10;
  }
  .router-link-active {
    color: yellow;
  }
}
</style>
