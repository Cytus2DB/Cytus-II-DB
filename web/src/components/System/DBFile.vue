<template>
  <div class="db">
    <div class="content">
      <Error v-if="error" :error="error"/>
      <Loading v-if="loading"/>
      <!-- TODO -->
    </div>
  </div>
</template>

<script>
import Error from '../Error';
import Loading from '../Loading';

export default {
  name: 'DBFile',
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
