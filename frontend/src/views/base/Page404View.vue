<template>
  <v-container class="fill-height back background-principal">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-card class="background-principal">
      
      <v-img
              src="https://cdn-icons-png.flaticon.com/512/580/580185.png"
              height="125"
              class="mt-12"
            ></v-img>
        <v-card-title class="headline">Opps! Página não encontrada</v-card-title>
          <v-btn color="yellow-darken-1" :to="{ name: 'base-home' }"> Voltar ao início </v-btn>
        <v-card-text> 😿 </v-card-text>
        <p class="text-h1">história sem graça</p>
        <v-card-actions>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-responsive>
  </v-container>
</template>

<style>
   .background-principal {
    background: #fffaaf;
  }
</style>
