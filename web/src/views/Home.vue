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
      <router-link to="/im">
        <div class="button">
          <img src="@/assets/home-im.png" alt="iM" />iM
        </div>
      </router-link>
      <router-link to="/os">
        <div class="button">
          <img src="@/assets/home-os.png" alt="OS" />OS
        </div>
      </router-link>
      <router-link to="/db">
        <div class="button">
          <img src="@/assets/home-db.png" alt="DB" />DB
        </div>
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
  height: 100%;
  padding: 24px 24px;
  display: flex;
  overflow-y: scroll;
  flex-direction: column;
  font-size: 1.2em;

  .body {
    padding-top: 18px;
    p {
      margin-top: 8px;
    }
  }
  .header {
    color: gray;
    font-style: italic;
  }
  .buttons {
    margin-bottom: 8px;
    display: flex;
    width: 100%;
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
    margin-top: 12px;
    margin-right: 18px;
    background: #2d303a;
    img {
      margin-bottom: 0.4em;
      width: 64px;
    }
    &:hover {
      background: #2d303a44;
      transition: 0.2s ease;
    }
  }
}
</style>
