<template>
  <div class="os">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <div class="sidebar" :class="{ hidden:($route.query.hide==='true') }">
      <template v-if="$route.query.view!='timeline'">
        <Folder v-for="(info, uuid) in oslist"
          :key="uuid"
          :uuid="uuid"
          :name="info.name"
          :files="info.files"/>
      </template>
      <template v-if="$route.query.view=='timeline'">
        <Folder key="timeline" uuid="timeline"
          :name="$t('header.display.timeline')"
          :files="ostime"
          :opened="true"/>
      </template>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Error from '@/components/Error';
import Loading from '@/components/Loading';

import Folder from '@/components/System/Folder';

export default {
  name: 'OS',
  data() {
    return {
      error: null,
      loading: null,
      oslist: null,
      ostime: null
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
      this.error = this.oslist = this.ostime = null;
      this.loading = true;
      fetch("./data/ostime.json").then(res => {
        this.loading = false;
        if (res.ok) res.json().then(data=>{
          this.ostime = data;
        }); else {
          this.error = res.status+' '+res.statusText;
        }
      });
      fetch("./data/oslist.json").then(res => {
        this.loading = false;
        if (res.ok) res.json().then(data=>{
          this.oslist = data;
        }); else {
          this.error = res.status+' '+res.statusText;
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.os {
  .sidebar {
    width: 300px;
    height: 100%;
    font-size: 1.2em;
    overflow-x: hidden;
    overflow-y: scroll;
    display: inline-block;
    background: #ffffff08;
    @media screen and (max-width: 767px) {
      width: 100%;
    }
  }
}
</style>
