<template>
  <header>
    <div class="header-l">
      <router-link
        :to="{
          path: '/im',
          hash: `#${$route.params.id}`,
          query: $route.query
        }"
        v-if="$route.matched[0]&&$route.matched[0].path=='/im'&&$route.params.id">
        <img src="@/assets/btn-back.svg" alt="Back">
      </router-link>
      <router-link
        :to="{
          hash: $route.hash,
          query: {
            ...$route.query,
            hide: reverse(this.$route.query.hide)
          }
        }"
        v-if="
          $route.matched[0] && (
          $route.matched[0].path=='/db' ||
          $route.matched[0].path=='/os'
        )">
        <img src="@/assets/btn-list.svg" alt="List">
      </router-link>
      <div class="title">{{$route.name}}</div>
    </div>
    <div class="header-r">
      <Options :title="$t('header.language')"
        :items="[{
          id: 'header.language.en',
          title: 'English',
          onclick: ()=>setLocale('en')
        }, {
          id: 'header.language.ja',
          title: '日本語',
          onclick: ()=>setLocale('ja')
        }, {
          id: 'header.language.zh',
          title: '中文<國際>',
          onclick: ()=>setLocale('zh')
        }, {
          id: 'header.language.ko',
          title: '한국',
          onclick: ()=>setLocale('ko')
        }, {
          id: 'header.language.zh-TW',
          title: '中文<繁體>',
          onclick: ()=>setLocale('zh-TW')
        }, {
          id: 'header.language.zh-CN',
          title: '中文<简体>',
          onclick: ()=>setLocale('zh-CN')
        }]" />
      <Options v-if="$route.name=='OS'"
        :title="$t('header.display.title')"
        :items="[{
          id: 'header.display.character',
          title: $t('header.display.character'),
          onclick: ()=>{this.$router.push({
            hash: this.$route.hash,
            query: {
              ...this.$route.query,
              view: 'character',
            }
          })}
        }, {
          id: 'header.display.timeline',
          title: $t('header.display.timeline'),
          onclick: ()=>{this.$router.push({
            hash: this.$route.hash,
            query: {
              ...this.$route.query,
              view: 'timeline',
            }
          })}
        }]" />
      <Options v-if="
          $route.matched[0] && (
          $route.matched[0].path=='/db' ||
          $route.matched[0].path=='/os' ||
          $route.matched[0].path=='/im'
        )"
        :title="$t('header.version')"
        :items="versions" />
    </div>
  </header>
</template>

<script>
import Options from '@/components/Options';

export default {
  name: 'Header',
  components: {
    Options
  },
  created () {
    this.fetchData()
  },
  data() {
    return {
      versions: []
    };
  },
  methods: {
    setLocale(locale) {
      localStorage.setItem('locale', locale);
      this.$i18n.locale = locale;
    },
    reverse(val) {
      return ( val==null || val==='false' ).toString()
    },
    fetchData() {
      fetch('./data/versions.json').then(res=>{
        res.json().then(data=>{
          data.forEach(item => {
            let versionItem = {
              id: item,
              title: item,
              onclick: ()=>{
                if (this.$route.query.v != item) this.$router.push({
                  hash: this.$route.hash,
                  query: {...this.$route.query, v: item}
                });
              }
            }
            this.versions.push(versionItem);
          });
        })
      })
    }
  }
}
</script>

<style lang="scss" scoped>
header {
  height: 2em;
  display: flex;
  box-sizing: border-box;
  
  font-size: 1em;
  background: #1e1f26;
  border-radius: 5px 5px 0px 0px;
  @media screen and (max-width: 767px) {
    border-radius: 0;
  }

  .header-l {
    left: 12px;
    height: 2em;
    display: flex;
    position: absolute;
    align-items: center;
    a {
      display: flex;
      margin-right: 6px;
      img {
        height: 1em;
      }
    }
    .title {
      font-size: 1.2em;
      user-select: none;
    }
  }
  .header-r {
    right: 8px;
    height: 2em;
    display: flex;
    position: absolute;
  }
}
</style>