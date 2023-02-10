<template>
  <div class='background-principal' :style="{minHeight: '50%'}">
    <v-row justify="center" align="center">
  <app-nav-bar/>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-left fill-height">

    <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            color="yellow"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4"
            @click="getTasksNonLogged()">
            
            <v-icon v-if="loading === false" icon="mdi-cached" size="large" start />
            <v-progress-circular
              v-if="loading"
              indeterminate
              color="amber"
              class="mr-3"
              :size="21"
            ></v-progress-circular>
            Outra história
          </v-btn>       
        </v-col>
      </v-row>

    <v-col v-for="item in items" :key="item.id" cols="12">
        <task-sem-permissoes :task="item"/>
      </v-col>
        
    </v-responsive>
  </v-container>
  </v-row>
</div>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import AppNavBar from "@/components/AppNavBar.vue"
import TasksApi from "@/api/tasks.api.js"
import TaskSemPermissoes from "@/components/TaskSemPermissoes.vue"

export default {
  
  components: {
    AppNavBar,
    TaskSemPermissoes
  },
  data() {
    return {
      loading: false,
      items: [],
      id: null,
      title: null,
    }
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
   mounted() {
    this.getTasksNonLogged()
  },
  methods: {
    getTasksNonLogged() {
      this.loading = true
      TasksApi.getTasksNonLogged().then((data) => {
        this.items = data.todos
        this.loading = false
      })
    },
  }
}
</script>