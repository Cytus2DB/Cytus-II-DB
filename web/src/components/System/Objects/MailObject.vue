<template>
  <div class="mail">
    <div class="info">
      {{$t('os.title')}}: {{title}}<br>
      {{$t('os.from')}}: {{from}}<br>
      {{$t('os.to')}}: {{to}}
    </div>
    <div class="text" v-html="content"/>
  </div>
</template>

<script>
export default {
  name: 'JsonObject',
  props: ['title', 'from', 'to', 'content']
}
</script>

<style lang="scss" scoped>
.mail .info {
  color: gray;
  margin-bottom: 8px;
}
</style>