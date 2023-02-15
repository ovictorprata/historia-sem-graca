<template>
  <v-row justify="center" >
    <v-dialog
      v-model="dialog"
      width="500"
      
    >
      <template #activator="{ props }">
       <v-btn
            color="amber-darken-3"
            min-width="400"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4"
          v-bind="props"
        >
        
        <v-icon icon="mdi-plus-thick" class="mr-4"/>
          Cadastrar história
        </v-btn>
      </template>
      <v-card class="bg-yellow-lighten-3">
        <v-card-text>
        <v-card-title>
          <span class="text-h5">Cadastre nova história:</span>
        </v-card-title>
          <v-row>
            <v-col>
              <v-col>
                <v-textarea
                  v-model="title"
                  solo
                  name="input-7-4"
                  label="Insira sua história aqui..."
                  class="bg-white rounded-lg"
                  @keyup.enter="addNewTask()"
                ></v-textarea>
              <v-switch v-model="switchMe" :label="'Essa história é sem graça?'" class="left-aligned-label" color="orange-darken-4"></v-switch>
              </v-col>
          </v-col>
        </v-row>
          <v-row v-show="is_boring" class="ml-3">sad</v-row>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
          class="text-red"
          variant="text"
          @click="dialog = false"
          >
            Fechar
          </v-btn>

          <v-btn
            class="bg-green"
            rounded="pill"
            @click="addNewTask()"
          >
            Salvar
          </v-btn>

         
        </v-card-actions>
        </v-card-text>
        
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
  export default {
    emits: ["newTask"],
    data: () => ({
      dialog: false,
      switchMe: false,
      title: null,
      isnt_funny: false,
    }),
     methods: {
    addNewTask() {
      this.dialog = false
      this.$emit("newTask", {
      title: this.title,
      })
      this.title = ""      
      this.switchMe = ""      
    },
  },
  }
</script>

<style>
   .left-aligned-label {
    left: 0 !important;
  }

  .popup {
    backdrop-filter: blur(2px);
  }
</style>