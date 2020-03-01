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

@font-face {
  font-family: NotoSansCJK;
  src: local("Noto Sans CJK"), url("fonts/NotoSansCJK-Regular.otf");
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

body {
  margin: 0;
  overflow: hidden;
  background: #0a0a0c;
  font-family: Rajdhani, NotoSansCJK, "Microsoft Yahei", -apple-system, sans-serif;
}

a {
  color: #00b0ff;
  text-decoration: none;
}

button {
  border: none;
  outline: none;
  cursor: pointer;
  padding: inherit;
  font-size: 1.8em;
  font-family: inherit;
  color: white;
  background: none;
}

.im, .os, .db, .home {
  height: calc(75vh - 2em);
  @media screen and (max-width: 767px) {
    height: calc(95vh - 2em);
  }
}

.new {
  color: lame;
}

.hidden {
  display: none;
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

  overflow-y: hidden;
}
</style>
