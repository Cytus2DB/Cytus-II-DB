<template>
  <footer>
    <div class="footer-l">
      <router-link to="/im">iM</router-link>
      &nbsp;&middot;&nbsp;
      <router-link to="/os">OS</router-link>
      &nbsp;&middot;&nbsp;
      <router-link to="/db">DB</router-link>
    </div>
    <div class="footer-r">
      <router-link to="/">Cytus II DB</router-link>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style lang="scss" scoped>
footer {
  top: 5px;
  position: relative;
  user-select: none;
  cursor: default;

  &, a {
    color: white;
    font-size: 16px;
  }
  .footer-l {
    display: inline-block;
  }
  .footer-r {
    display: inline-block;
    position: absolute;
    right: 0;
  }
}
</style>