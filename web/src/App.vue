<template>
  <div id="app">
    <div id="main">
      <Header/>
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/views/App/Header';
import Footer from '@/views/App/Footer';

export default {
  name: 'App',
  components: {
    Header, Footer
  }
}
</script>

<style lang="scss">
@font-face {
  font-family: Rajdhani;
  src: local("Rajdhani"), url("fonts/Rajdhani-SemiBold.ttf");
}

*::-webkit-scrollbar-track {
  background-color: #0a0a0c;
}

*::-webkit-scrollbar {
  width: 6px;
  background-color: #0a0a0c;
}

*::-webkit-scrollbar-thumb {
  background-color: #fff;
}

html, body {
  margin: 0;
  background: #0a0a0c;
  font-family: Rajdhani, "Noto Sans CJK SC", "Noto Sans SC", "Microsoft Yahei", -apple-system, sans-serif;
}

a {
  color: #00b0ff;
  text-decoration: none;
}

button {
  color: white;
  background: none;
  border: none;
  padding: inherit;
  font-size: 16px;
  outline: none;
  cursor: pointer;
  font-family: inherit;
}

.new {
  color: yellow;
}

#app {
  position: absolute;
  height: 80vh;
  width: 80vw;
  left: 10vw;
  top: 10vh;
  @media screen and (max-width: 767px) {
    height: 100vh;
    width: 100vw;
    left: 0;
    top: 0;
  }
  color: #fff;
}
#main {
  height: 75vh;
  @media screen and (max-width: 767px) {
    height: 95vh;
  }

  display: flex;
  flex-direction: column;

  background: #131418;
  border-radius: 5px;
}
</style>
