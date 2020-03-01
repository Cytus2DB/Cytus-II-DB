<template>
  <div class="folder">
    <div class="title" @click="()=>{folded = !folded;}">
      {{title}}
    </div>
    <router-link :class="{hidden: folded}" v-for="file in files" :key="file.id" :to="{
      path: (location?location+'/':'')+file.id,
      query: $route.query
    }" append>
      {{file.title}}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Folder',
  props: ['location', 'title', 'files'],
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
