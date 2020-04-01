<template>
  <div class="options">
      <div class="title" @click="toggle">
        <span>{{title}}</span>
        <img src="@/assets/btn-drop.svg" alt="dropdown"/>
      </div>
      <div :class="{ hidden }" style="max-height: 300px; overflow-y: scroll;">
        <div
          class="item"
          v-for="item in items"
          :key="item.id"
          @click="()=>{toggle();item.onclick();}"
        >
          {{item.title}}
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Options',
  props: ['title', 'items'],
  data() {
    return { hidden: true };
  },
  methods: {
    toggle() {
      this.hidden = !this.hidden;
    }
  }
}
</script>

<style lang="scss" scoped>
.options {
  margin-top: .25em;
  height: 1.5em;
  z-index: 500;
  cursor: pointer;
  user-select: none;
  .title {
    display: flex;
    align-items: center;
    justify-content: flex-end;

    margin-bottom: 2px;
    img {
      height: 16px;
      margin: 0px 4px;
    }
  }
  .item {
    padding: 4px 6px;
    text-align: center;
    background: #5a5f73;
  }
}
</style>