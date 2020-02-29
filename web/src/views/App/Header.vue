<template>
  <header>
    <div class="header-l">
      <router-link :to="`/im#${$route.params.id}`" v-if="$route.params.id">
        <img src="@/assets/btn-back.svg" alt="Back">
      </router-link>
      <router-link
        :to="{
          query: {
            ...$route.query,
            hide: (
              this.$route.query.hide==null || this.$route.query.hide==='false'
            ).toString()
          }
        }"
        v-if="$route.path.match(/(os|db)/)">
        <img src="@/assets/btn-list.svg" alt="List">
      </router-link>
    </div>
    <div class="header-t">{{$route.name}}</div>
    <div class="header-r">
      <Options v-if="$route.name=='OS'"
        :title="$t('header.display.title')"
        :items="[{
          id: 'header.display.character',
          title: $t('header.display.character'),
          onclick: ()=>{this.$router.push('/os/c')}
        }, {
          id: 'header.display.timeline',
          title: $t('header.display.timeline'),
          onclick: ()=>{this.$router.push('/os/t')}
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
    fetchData() {
      fetch('./data/versions.json').then(res=>{
        res.json().then(data=>{
          data.forEach(item => {
            this.versions.push({
              id: item,
              title: item,
              onclick: ()=>this.$router.push({
                query: {...this.$route.query, v: item}
              })
            });
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
    img {
      height: 1.2em;
    }
  }
  .header-t {
    font-size: 1.2em;
    text-align: center;
    padding: 5px 0;
    user-select: none;
  }
  .header-r {
    right: 0;
    padding: 3px 6px;
    position: absolute;
    display: inline-flex;
  }
}
</style>