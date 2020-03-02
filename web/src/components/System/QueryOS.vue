<template>
  <div class="view" :class="{full: $route.query.hide=='true'}">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <div class="content" v-if="!loading&&$route.params.folder">
      <div class="video" v-if="osfile.res">
        <VideoPlayer :options="{
          video: {
            url: `./videos/${osfile.res.toLowerCase()}`
          },
          subtitle: {
            url: `./data/subtitles/${osfile.res.split('.')[0].toLowerCase()}_${$i18n.locale}.vtt`
          },
          autoplay: false
        }" />
      </div>
      <div v-for="(content, index) in osfile.contents[parseInt($t('code'))]"
        :key="`${$route.params.id}_${$i18n.locale}_${index}`">
        <div class="audio" v-if="content.type=='bgm'">
          <AudioPlayer theme="#2d303a" :music="{
            pic: '@/assets/empty.png',
            src: `./audios/bgms/${content.attrs[0].toLowerCase()}.mp3`,
            title: $t('os.bgm'),
            artist: content.attrs[0],
          }" preload />
        </div>
        <div class="image" v-if="content.type=='bgm'">

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Error from '../Error';
import Loading from '../Loading';

import 'vue-dplayer/dist/vue-dplayer.css';

import VideoPlayer from 'vue-dplayer';
import AudioPlayer from 'vue-aplayer';

export default {
  name: 'QueryOS',
  data() {
    return {
      error: null,
      loading: null,
      osfile: {
        contents: []
      },
    };
  },
  components: {
    Error,
    Loading,
    AudioPlayer,
    VideoPlayer,
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
      this.osfile = {
        contents: []
      };
      this.error = null;
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
}
</style>
