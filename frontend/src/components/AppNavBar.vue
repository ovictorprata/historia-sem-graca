<template>
  <v-app-bar class="background--principal text">
    <v-app-bar-title class="title--nav-bar">{{ title }}</v-app-bar-title>
    <template #append>
      abrir no Github<v-btn icon="mdi-github" href="https://github.com/ovictorprata/historia-sem-graca"  target=”_blank”></v-btn>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false,
      default: "história sem graça",
    },
  },

  data: () => {
    return {}
  },
  methods: {

  },
}
</script>

<style>
  .background--principal {
    background: #e3de9c !important;
  }

  .title--nav-bar {
    color: rgb(66, 66, 66);
    font-weight: 700;
  }
</style>

