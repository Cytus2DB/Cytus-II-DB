<template>
  <div class="im">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'iM'
}
</script>

<style lang="scss">
.im {
  overflow-x: hidden;
  overflow-y: scroll;
}
</style>