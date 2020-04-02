<template>
  <div class="view" :class="{full: $route.query.hide=='true'}">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <div class="content" v-if="!loading&&$route.params.folder">
      <div class="video" v-if="osfile.res">
        <VideoPlayer :options="{
          video: {
            url: `./videos/${osfile.res}`
          },
          subtitle: {
            url: `./data/subtitles/${osfile.res.split('.')[0].toLowerCase()}_${$i18n.locale}.vtt`
          },
          autoplay: false
        }"/>
      </div>
      <div v-for="(item, index) in osfile.contents[parseInt($t('code'))]"
        :key="`${$route.params.id}_${$i18n.locale}_${index}`">
        <div class="hint" v-if="item.type=='text'" v-html="item.content"/>
        <div class="video" v-if="item.type=='movie'">
          <VideoPlayer :options="{
            video: {
              url: `./videos/${item.attrs[0]}.mp4`
            },
            subtitle: {
              url: `./data/subtitles/${item.attrs[0].toLowerCase()}_${$i18n.locale}.vtt`
            },
            autoplay: false
          }"/>
        </div>
        <div class="audio" v-if="item.type=='bgm'">
          <AudioPlayer theme="#2d303a" :music="{
            pic: './empty.png',
            src: `./audios/bgms/${item.attrs[0].toLowerCase()}.mp3`,
            loop: 'one',
            mutex: false,
            title: $t('os.bgm'),
            artist: item.attrs[0],
          }" preload/>
        </div>
        <div class="audio" v-if="item.type=='sound'">
          <AudioPlayer theme="#2d303a" :music="{
            pic: './empty.png',
            src: `./audios/sounds/${item.attrs[0].toLowerCase()}.mp3`,
            loop: 'none',
            mutex: false,
            title: item.attrs[1],
            artist: item.attrs[0],
          }" preload/>
        </div>
        <div class="image" v-if="item.type=='image'">
          <img :alt="item.attrs[0]" :src="`./images/osfiles/${item.attrs[0].toLowerCase()}.jpg`"
            @click="()=>viewImage(`./images/osfiles/${item.attrs[0].toLowerCase()}.jpg`)">
        </div>
        <JsonObject v-if="item.type=='json'" :raw="item"/>
        <MailObject v-if="item.type=='mail'"
          :title="item.attrs[0]"
          :from="item.attrs[1]"
          :to="item.attrs[2]"
          :content="item.content"/>
        <TextObject v-if="item.type=='conversation'"
          :name="item.attrs[0]"
          :content="item.content"/>
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

import JsonObject from './Objects/JsonObject';
import MailObject from './Objects/MailObject';
import TextObject from './Objects/TextObject';

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
    JsonObject,
    MailObject,
    TextObject,
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
          // delete duplicated cutscene
          let firstItem = data.contents?data.contents[0]:{};
          if (firstItem.type=="movie"&&firstItem.attrs[0]==data.res){
            data.res = null;
          }

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
  .audio, .video, .image, .hint {
    margin-bottom: 16px;
  }
  .hint {
    white-space: pre-line;
  }
  .image img {
    max-width: 100%;
  }
}
</style>
