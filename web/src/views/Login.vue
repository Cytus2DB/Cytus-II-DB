<template>
  <div class="login">
      <div class="label">{{$t("login.username")}}</div>
      <input type="text" value="Ivy" disabled>
      <div class="label">{{$t("login.uuid")}}</div>
      <input type="text" v-model="uuid" :style="{color: color}">
      <button @click="login">{{$t("login.login")}}</button>
      <audio ref="success" src="@/audios/Password_Pass.mp3" preload></audio>
      <audio ref="failed"  src="@/audios/Password_Fail.mp3" preload></audio>
  </div>
</template>

<script>
import auth from '@/auth'

export default {
  name: 'Login',
  data() {
    return {
      uuid: localStorage['auth'],
      color: 'white'
    }
  },
  methods: {
    login() {
      localStorage.setItem('auth', this.uuid);
      if (auth()) {
        this.color = 'lawngreen';
        this.$refs.success.onended = ()=>this.$router.push('/');
        this.$refs.success.play();
      } else {
        this.color = 'red';
        this.$refs.failed.play();
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 15vh;

  .label {
    margin-top: 18px;
    font-size: 1.2em;
  }
  input {
    margin-top: 8px;
    border: none;

    color: white;
    text-align: center;
    font-size: 1.2em;
    font-family: inherit;

    background: #2d303a;
  }
  button {
    display: block;
    margin-top: 48px;
    padding: 0.4em 0.8em;

    font-size: 1.2em;
    font-family: inherit;

    background: #2d303a;
  }
}
</style>