<template>
  <div class="view">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <div class="content" v-if="!loading&&$route.params.folder">
      <!--
      <div class="video" v-if="current().type==1||current().type==5">
        <VideoPlayer :options="{
          video: {
            url: filepath()
          },
          subtitle: {
            url: current().type==1?`./data/subtitles/${$route.params.id}_${$i18n.locale}.vtt`:null
          },
          autoplay: false
        }" />
      </div>
      <div class="audio" v-if="current().type==2||current().type==4">
        <AudioPlayer theme="#2d303a" preload :music="{
          pic: '@/assets/empty.png',
          src: filepath(),
          title: current().name,
          artist: this.$route.params.id,
        }" />
      </div>
      <div class="image" v-if="current().type==3">

      </div>
      -->
    </div>
  </div>
</template>

<script>
import Error from '../Error';
import Loading from '../Loading';

import 'vue-dplayer/dist/vue-dplayer.css';

//import AudioPlayer from 'vue-aplayer';
//import VideoPlayer from 'vue-dplayer';

export default {
  name: 'OSFile',
  data() {
    return {
      error: null,
      loading: null,
      osfile: null,
    };
  },
  components: {
    Error,
    Loading,
    //AudioPlayer,
    //VideoPlayer,
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData() {
      if (!this.$route.params.folder) return;
      this.error = this.osfile = null;
      this.loading = true;
      fetch(`./data/osfiles/${this.$route.params.folder}/${this.$route.params.id}.json`).then(res => {
        this.loading = false;
        if (res.ok) res.json().then(data=>{
          this.osfile = data;
        }); else {
          this.error = res.status+' '+res.statusText;
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.view {
  width: calc(80vw - 300px);
  @media screen and (max-width: 767px) {
    width: calc(100vw - 300px);
  }
  height: 100%;
  padding: 16px;
  overflow-x: hidden;
  overflow-y: scroll;
  display: inline-block;
  box-sizing: border-box;
  .info {
    margin-bottom: 16px;
  }
  .loading {
    width: calc(80vw - 332px);
    @media screen and (max-width: 767px) {
      width: calc(100vw - 332px);
    }
  }
  .aplayer {
    color: #fff;
    background: #fff1;
    aplyer-icon:hover {
      opacity: .2;
    }
  }
}
</style>
