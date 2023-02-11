<template>
  <v-row justify="center" >
    <v-dialog
      v-model="dialog"
      persistent
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
        
        <v-icon icon="mdi-plus-circle-outline" class="mr-4"/>
          Cadastrar história
        </v-btn>
      </template>
      <v-card class="bg-lime-lighten-3">
        <v-card-text>
        <v-card-title>
          <span class="text-h5">Cadastre nova história:</span>
        </v-card-title>
          <v-row>
            <v-col>
              <v-col>
                <v-textarea
                  solo
                  name="input-7-4"
                  label="Insira sua história aqui..."
                ></v-textarea>
              </v-col>
            <v-switch v-model="switchMe" :label="'Essa história é sem graça?'" class="left-aligned-label" color="yellow"></v-switch>
          </v-col>
        </v-row>

        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green"
            variant="text"
            @click="dialog = false"
          >
            Save
          </v-btn>
          <v-btn
            color="red"
            variant="text"
            @click="dialog = false"
          >
            Close
          </v-btn>
          
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      dialog: false,
      switchMe: false,
    }),
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