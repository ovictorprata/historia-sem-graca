<template>
  <v-app-bar class="background--principal text">
    <v-app-bar-title class="title--nav-bar">{{ title }}</v-app-bar-title>
    <template #append>
      <v-btn icon="mdi-home" :to="{ name: 'base-home' }" color="black"></v-btn>


      <!-- <v-btn icon="mdi-logout" color="black"> -->
        <!-- <v-icon icon="mdi-logout" />
        <v-menu activator="parent">
          <v-list>
            <v-list-item v-if="!loggedUser" :to="{ name: 'accounts-logout' }"> Sair </v-list-item>
          </v-list>
        </v-menu>
      </v-btn> -->
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
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {}
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
  },
}
</script>

<style>
  .background--principal {
    background: #fffaaf !important;
  }

  .title--nav-bar {
    color: rgb(66, 66, 66);
    font-weight: 700;
  }
</style>

