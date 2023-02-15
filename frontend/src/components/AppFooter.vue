<template>
  <v-footer :absolute="!fixed" app class="footer">
    <v-container>
    <v-row  justify="center">
      <div>
        <v-btn
          class="mx-4"
          href="https://www.linkedin.com/in/ovictorprata/"
          target="_blank"
          icon="mdi-linkedin"
          variant="text"
          :absolute="!fixed"
        ></v-btn>
        <v-btn
          class="mx-4"
          href="https://api.whatsapp.com/send?phone=5531973114856&text=Ol%C3%A1%20@ovictorprata,%20gostaria%20de%20conversar%20sobre%20o%20hist%C3%B3ria%20sem%20gra%C3%A7a%20com%20voc%C3%AA."
          target="_blank"
          icon="mdi-whatsapp"
          variant="text"
          :absolute="!fixed"
        ></v-btn>
        <v-btn
          class="mx-4"
          href="https://www.github.com/ovictorprata/"
          target="_blank"
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