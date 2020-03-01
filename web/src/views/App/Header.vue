<template>
  <header>
    <div class="header-l">
      <router-link
        :to="{
          path: '/im',
          hash: `#${$route.params.id}`,
          query: $route.query
        }"
        v-if="$route.params.id">
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
        v-if="$route.path.match(/(os|db)/)">
        <img src="@/assets/btn-list.svg" alt="List">
      </router-link>
      <div class="title">{{$route.name}}</div>
    </div>
    <div class="header-r">
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
      <Options v-if="$route.path.match(/(im|os|db)/)"
        :title="$t('header.version')"
        :items="versions" />
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
  justify-content: center;
  
  background: #1e1f26;
  border-radius: 5px 5px 0px 0px;
  @media screen and (max-width: 767px) {
    border-radius: 0;
  }

  .header-l {
    left: 0;
    padding: 6px 12px;
    position: absolute;
    display: inline-flex;
    justify-content: center;
    .title {
      text-align: center;
      font-size: 1em;
      user-select: none;
    }
    a {
      margin-right: 6px;
    }
    img {
      height: 1.2em;
    }
  }
  .header-r {
    right: 0;
    padding: 3px 6px;
    position: absolute;
    display: inline-flex;
  }
}
</style>