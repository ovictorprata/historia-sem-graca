<template>
  <v-sheet width="400" class="mx-auto">
    <v-form @submit.prevent>
      <v-text-field
        v-model="title"
        :rules="rules"
        :label="formLabel"
        class="card--principal"
        required
        append-inner-icon="mdi-comment"
        @keyup.enter="addNewTask"
      ></v-text-field>
      <v-btn 
        type="submit" 
        block 
        class="mt-2 btn--form"
        @click="addNewTask"
      >
        Cadastrar história
      </v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
export default {
  props: {
    formLabel: {
      type: String,
      default: "Insira sua história sem graça",
    },
  },
  emits: ["newTask"],
  data: () => {
    return {
      title: "",
      firstName: null,
      rules: [
        value => {
          if (value.length >= 10) return true

          return 'Sua história deve ter pelo menos 10 caracteres.'
        },
      ],
    }
  },
  methods: {
    addNewTask() {
      if(this.title.length >= 10) {
        this.$emit("newTask", {
        title: this.title,
      })
      this.title = ""
      }
      
    },
  },
}
</script>

<style scoped>
.card--principal{
  background: #fffaaf;
  color: black
}

.btn--form {
  background: #c9c7b2;
  color: #fffaaf;
  font-weight: 900;
}

</style>
