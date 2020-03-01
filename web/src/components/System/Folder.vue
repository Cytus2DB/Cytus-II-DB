<template>
  <div class="folder">
    <div class="title" @click="()=>{hidden = !hidden;}">
      <img src="@/assets/os-open.svg" alt="dropdown">
      {{name}}
    </div>
    <router-link tag="div" class="item" v-for="file in files" :key="file.id"
      :class="{
        hidden,
        new: file.version==$route.query.v
      }"
      :to="{
        path: `${$route.matched[0].path}/${uuid}/${file.name}`,
        query: $route.query
      }" append>
      {{file.title}}
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
  }
}
</script>

<style lang="scss" scoped>
.folder {
  margin: .4em;
  cursor: pointer;
  user-select: none;
  .title {
    display: flex;
    padding: .2em .4em;
    align-items: center;
    background: #ffffff08;
    img {
      height: .8em;
      padding-right: .4em;
    }
  }
  .item {
    padding: .2em .4em;
    margin-bottom: 1px;
    background: #ffffff10;
  }
}
</style>
