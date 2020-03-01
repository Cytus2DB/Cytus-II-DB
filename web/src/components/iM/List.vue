<template>
  <div class="list">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <Item v-for="item in items" :key="item.id" :item="item"/>
  </div>
</template>

<script>
import Error from '../Error';
import Loading from '../Loading';

import Item from './List/Item';

export default {
  name: 'List',
  data() {
    return {
      error: null,
      loading: null,

      items: null,
    };
  },
  components: {
    Error,
    Loading,

    Item,
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData() {
      this.error = this.items = null;
      this.loading = true;
      fetch("./data/imlist.json").then(res => {
        this.loading = false;
        if (res.ok) res.json().then(data=>{
          this.items = data;
        }); else {
          this.error = res.status+' '+res.statusText;
        }
      });
    }
  }
}
</script>
