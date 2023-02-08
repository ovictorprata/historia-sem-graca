<template>
  <v-footer :absolute="!fixed" app class="footer">
    <v-container>
      <v-row justify="center">        
        <v-col cols="12" align-self="center" class="pa-0 text-center">
          <span> &copy; {{ new Date().getFullYear() }} - história sem graça </span>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  props: {
    fixed: {
      type: Boolean,
      default: true,
    },
    user: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
    nodeEnv: import.meta.env.VITE_NODE_ENV,
  }),
}
</script>

<style>
  .footer {
    background: rgb(199, 199, 71);
    color: white;
    font-weight: bold;
  }
</style>