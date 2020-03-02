<template>
  <div class="home">
    <div class="header">
      {{$t("header.version")}}: {{version}}<br>
      {{$t("login.username")}}: Ivy<br>
      {{$t("home.header.line3")}}: Constructor<br>
      {{$t("home.header.line4")}}<br>
    </div>
    <div class="body">
      <p>{{$t("home.text.line1")}}</p>
      <p>{{$t("home.text.line2")}}</p>
      <p>{{$t("home.text.line3")}}:</p>
      <p>
        <a href="https://afdian.net/@dtsdao">afdian</a>
        &nbsp; / &nbsp;
        <a href="https://www.patreon.com/dtsdao">Patreon</a>
      </p>
      <p>{{$t("home.text.line4")}}</p>
    </div>
    <div class="buttons">
      <router-link class="button" to="/im">
        <img src="@/assets/home-im.png" alt="iM" />iM
      </router-link>
      <router-link class="button" to="/os">
        <img src="@/assets/home-os.png" alt="OS" />OS
      </router-link>
      <router-link class="button" to="/db">
        <img src="@/assets/home-db.png" alt="DB" />DB
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      version: process.env.VUE_APP_VERSION
    }
  }
}
</script>

<style lang="scss" scoped>
.home {
  padding: 0 24px;
  font-size: 1.2em;
  overflow-x: hidden;
  overflow-y: scroll;

  .header {
    color: gray;
    font-style: italic;
    padding-top: 12px;
  }
  .body p {
    margin: 12px 0px;
  }
  .buttons {
    width: 100%;
    display: flex;
    flex-flow: wrap;
    a {
      color: #fff;
    }
  }
  .button {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 1.2em;
    padding: 16px 28px;
    cursor: pointer;
    margin-bottom: 18px;
    margin-right: 18px;
    background: #2d303a;
    img {
      margin-bottom: 0.4em;
      width: 56px;
    }
    &:hover {
      background: #2d303a44;
      transition: 0.2s ease;
    }
  }
}
</style>
