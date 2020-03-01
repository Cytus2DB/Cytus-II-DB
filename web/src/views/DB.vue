<template>
  <div class="db">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <div class="sidebar" :class="{ hidden:($route.query.hide==='true') }">
      <Folder v-for="(info, uuid) in dblist"
        :key="uuid"
        :uuid="uuid"
        :name="info.name"
        :files="info.files"/>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Error from '@/components/Error';
import Loading from '@/components/Loading';

import Folder from '@/components/System/Folder';

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
    Folder,
  },
  created () {
    this.fetchData()
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
.db {
  .sidebar {
    width: 12em;
    height: 100%;
    font-size: 1.2em;
    overflow-y: scroll;
    background: #ffffff08;
    @media screen and (max-width: 767px) {
      width: 100%;
    }
  }
}
</style>
