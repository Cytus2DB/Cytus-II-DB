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
        <img :src="`./images/imfiles/${item.toLowerCase()}.jpg`" :alt="item" @click="()=>{
          window.open(`./images/imfiles/${item.toLowerCase()}.jpg`);
        }">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostView",
  props: ["avatar", "name", "pid", "title", "text", "attachments"]
}
</script>

<style lang="scss" scoped>

</style>
