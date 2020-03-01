<template>
  <div class="db">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <div :class="{sidebar:true, hidden:$route.query.hide}">
      <Folder v-for="(info, uuid) in dblist"
        :key="info.name"
        :uuid="uuid"
        :title="info.title||info.name"
        :files="info.files"/>
    </div>
    <div class="content" v-if="$route.params.id">
      <!-- TODO -->
    </div>
  </div>
</template>

<script>
import Error from '@/components/Error';
import Loading from '@/components/Loading';

export default {
  name: 'DB',
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
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData() {
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

</style>
