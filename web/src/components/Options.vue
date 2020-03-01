<template>
  <div class="options">
      <div class="title" @click="toggle">
        <span>{{title}}</span>
        <img src="@/assets/os-open.svg" alt="dropdown" />
      </div>
      <div :class="{ fold: fold }">
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
    return { fold: true };
  },
  methods: {
    toggle() {
      this.fold = !this.fold;
    }
  }
}
</script>

<style lang="scss" scoped>
.options {
  z-index: 500;
  cursor: pointer;
  text-align: right;
  user-select: none;
  .title {
    display: flex;
    align-items: center;
    justify-content: flex-end;

    padding: 2px 3px;
    margin-bottom: 2px;
    img {
      height: 1em;
      margin: 4px;
    }
  }
  .item {
    padding: 4px 5px;
    background: #5a5f73;
  }
  .fold {
    display: none;
  }
}
</style>