<template>
  <div class="json">
    <div class="msgs" v-if="file.type===0">
      <div class="msg" v-for="(item, index) in file.data"
        :key="index"
        :class="{
          self: item.MessageType===1||item.MessageType===3,
          system: item.MessageType===0,
        }">
        <div class="avatar" v-if="item.Avatar">
          <img :src="`./images/osavatars/${item.Avatar.toLowerCase()}.png`" :alt="item.Avatar">
        </div>
        <div class="body">
          <div class="info" v-if="item.UserName||item.Time">
            <div class="name">{{item.UserName}}</div>
            <div class="time">{{item.Time}}</div>
          </div>
          <div class="sticker" v-if="item.MessageType===3||item.MessageType===4">
            <img :src="`./images/osstickers/${item.Image.toLowerCase()}.png`" :alt="item.Image">
          </div>
          <div class="text" v-if="item.Content">{{item.Content}}</div>
        </div>
      </div>
    </div>
    <div class="image" v-if="file.type===1">
      <img :alt="file.data.Image"
        :src="`./images/osspecial/${file.data.Image.toLowerCase()}.jpg`"
        @click="()=>viewImage(`./images/osspecial/${file.data.Image.toLowerCase()}.jpg`)">
    </div>
    <template v-if="file.type===2">
      <div class="image" v-for="item in file.data" :key="item.Id">
        <img :alt="item.Id"
          :src="`./images/osfiles/${item.Id.toLowerCase()}.jpg`"
          @click="()=>viewImage(`./images/osfiles/${item.Id.toLowerCase()}.jpg`)">
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: 'JsonObject',
  props: ['raw'],
  computed: {
    file() {
      switch (this.raw.attrs[0]) {
        case 'msgs':
          return {
            type: 0,
            data:JSON.parse(this.raw.content.replace(/\n/g, "\\n"))
          };
        case 'imageviewer':
          return {
            type: 1,
            data:JSON.parse(this.raw.content)
          };
        case 'gallery':
          return {
            type: 2,
            data:JSON.parse(this.raw.content.replace(/\n/g, ""))
          };
        default:
          console.error('Unknown JsonObject');
          console.log(this.raw.content);
          return {};
      }
    }
  },
  methods: {
    viewImage(url) {
      window.open(url);
    }
  }
}
</script>

<style lang="scss" scoped>
.json {
  .msgs {
    .msg {
      display: flex;
    }
    .time, .system {
      color: gray;
    }
    .system {
      display: block;
      font-size: 0.9em;
      text-align: center;
    }
    .self {
      display: flex;
      flex-direction: row-reverse;
      .info {
        justify-content: flex-end;
      }
      .body {
        text-align: right;
      }
    }
    .avatar {
      margin: 0 8px;
    }
    .name {
      margin-right: 16px;
      color: #ff9800;
    }
    .info {
      display: flex;
      font-size: .9em;
    }
    .text {
      padding: 16px;
      font-size: 1.2em;
      white-space: pre-line;
      background: #ffffff10;
    }
  }
  .image img {
    width: 100%;
  }
}
</style>