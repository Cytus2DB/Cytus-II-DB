<template>
  <div class="folder">
    <div class="title" @click="()=>{folded = !folded;}">
      {{name}}
    </div>
    <router-link v-for="file in files" :key="file.id"
      :class="{
        hidden: folded,
        new: file.version==$route.query.v
      }"
      :to="{
        path: `${uuid}/${file.id}`,
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
      folded: true
    };
  }
}
</script>

<style lang="scss" scoped>
.folder {

}
</style>
