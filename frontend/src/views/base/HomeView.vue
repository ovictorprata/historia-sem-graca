<template>
  <div>
    <v-row justify="center" align="center">
  <app-nav-bar/>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-left fill-height">

    <v-col v-for="item in items" :key="item.id" cols="12">
        <task-sem-permissoes :task="item"/>
      </v-col>
        
      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            color="primary"
            :to="{ name: 'base-getstarted' }"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4">
            <v-icon icon="mdi-account-plus" size="large" start />
            Registre-se
          </v-btn>
          <v-btn
            v-if="!loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Login
          </v-btn>
          <v-btn
            v-else
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-logout' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Logout
          </v-btn>
          <v-btn
            v-if="loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'tasks-list' }"
            class="my-4">
            <v-icon icon="mdi-folder-star-multiple" size="large" start />
            tarefas
          </v-btn>
        </v-col>
      </v-row>
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
