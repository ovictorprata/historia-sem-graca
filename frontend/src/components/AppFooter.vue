<template>
  <v-footer :absolute="!fixed" app class="footer">
    <v-container>
    <v-row  justify="center">
      <div>
        <v-btn
          class="mx-4"
          icon="mdi-linkedin"
          variant="text"
          herf="https://www.linkedin.com/in/ovictorprata/"
          target="_blank"
          :absolute="!fixed"
        ></v-btn>
        <v-btn
          class="mx-4"
          icon="mdi-whatsapp"
          variant="text"
          :absolute="!fixed"
        ></v-btn>
        <v-btn
          class="mx-4"
          icon="mdi-github"
          variant="text"
          :absolute="!fixed"
        ></v-btn>
      </div>
    </v-row>
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
    icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
  }),
}
</script>

<style>
  .footer {
    background: #e3de9c !important;
    font-weight: bold;
  }
</style>