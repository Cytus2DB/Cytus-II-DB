<template>
  <div class="post">
    <Error v-if="error" :error="error"/>
    <Loading v-if="loading"/>

    <PostView v-if="post"
      :avatar="post.avatar"
      :name="post.name"
      :pid="post.id"
      :title="post.title[parseInt($t('code'))]"
      :text="post.contents[parseInt($t('code'))]"
      :attachments="post.attachments"/>
    <PostReply v-for="reply in replies" :key="reply.id"
      :avatar="post.avatar"
      :name="post.name"
      :text="post.contents[parseInt($t('code'))]"/>
  </div>
</template>

<script>
import Error from '../Error';
import Loading from '../Loading';

import PostView from './Post/PostView';
import PostReply from './Post/PostReply';

export default {
  name: 'Post',
  data() {
    return {
      error: null,
      loading: null,

      post: null,
      replies: null,
    };
  },
  components: {
    Error,
    Loading,

    PostView,
    PostReply,
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData () {
      this.error = this.post = this.replies = null;
      this.loading = true;
      fetch(`./data/imposts/${this.$route.params.id}.json`).then(res => {
        this.loading = false;
        if (res.ok) res.json().then(data=>{
          this.post = data;
          console.log(data);
          this.replies = data.replies;
        }); else {
          this.error = res.status+' '+res.statusText
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.list {
  height: 100%;
  overflow-y: scroll;
}
</style>
