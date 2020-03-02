<template>
  <div class="view" :class="{full: $route.query.hide=='true'}">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>
    <template v-if="!loading&&$route.params.folder">
      <div class="info">
        {{$t('db.filename')}}: {{current().name}}<br>
        <a target="_blank" :href="filepath()">{{$t('db.download')}}</a>
      </div>
      <div class="content">
        <div class="video" v-if="current().type==1||current().type==5">
          <VideoPlayer :options="{
            video: {
              url: filepath()
            },
            subtitle: {
              url: current().type==1?`./data/subtitles/${$route.params.id}_${$i18n.locale}.vtt`:null
            }
          }"/>
        </div>
        <div class="audio" v-if="current().type==2||current().type==4">
          <AudioPlayer theme="#2d303a" :music="{
            pic: '@/assets/empty.png',
            src: filepath(),
            title: current().name,
            artist: $route.params.id,
          }" preload/>
        </div>
        <div class="image" v-if="current().type==3">
          <img :alt="$route.params.id" :src="`./images/gallery/${$route.params.id}.jpg`"
            @click="viewImage(`./images/gallery/${$route.params.id}.jpg`)">
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import Error from '../Error';
import Loading from '../Loading';

import 'vue-dplayer/dist/vue-dplayer.css';

import VideoPlayer from 'vue-dplayer';
import AudioPlayer from 'vue-aplayer';

export default {
  name: 'QueryDB',
  data() {
    return {
      error: null,
      loading: null,
      dblist: null,
    };
  },
  components: {
    Error,
    Loading,
    VideoPlayer,
    AudioPlayer,
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    viewImage(url) {
      window.open(url);
    },
    current() {
      if (!this.dblist) return {};
      return this.dblist[this.$route.params.folder].files[this.$route.params.id];
    },
    filepath() {
      switch (this.current().type) {
        case 1:
          return `./videos/${this.$route.params.id}.mp4`;
        case 2:
          return `./audios/story/${this.$route.params.id}.mp3`;
        case 3:
          return ``;
        case 4:
          return `${this.current().location}/${this.$route.params.id}.mp3`;
        case 5:
          return `${this.current().location}/${this.$route.params.id}.mp4`;
        default:
          return 0;
      }
    },
    fetchData() {
      if (!this.$route.params.folder) return;
      this.error = this.dblist = null;
      this.loading = true;
      fetch("./data/dblist.json").then(res => {
        this.loading = false;
        if (res.ok) res.json().then(data=>{
          this.dblist = data;
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
    width: calc(100vw);
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
      width: calc(100vw);
    }
  }
  .aplayer {
    color: #fff;
    background: #fff1;
    aplyer-icon:hover {
      opacity: .2;
    }
  }
  .image img {
    max-width: 100%;
  }
}
</style>
