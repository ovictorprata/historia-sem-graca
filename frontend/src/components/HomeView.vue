<template>
  <v-container class="background-principal fill-height">
  <app-nav-bar/>
    <v-responsive class="d-flex align-center text-center">
    <v-col v-for="item in items" :key="item.id" cols="12">
        <task-sem-permissoes :task="item"/>
        <v-btn
            color="yellow"
            min-width="400"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4"
            @click="getTasksNonLogged()"
            >
            
            <v-icon v-if="loading === false" icon="mdi-cached" size="large" start />
            <v-progress-circular
              v-if="loading"
              indeterminate
              color="black"
              class="mr-3"
              :size="21"
            ></v-progress-circular>
            Ler outra história
          </v-btn>  
            <popup-form-story @new-task="addNewTask" />
      </v-col>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import AppNavBar from "@/components/AppNavBar.vue"
import TasksApi from "@/api/tasks.api.js"
import TaskSemPermissoes from "@/components/TaskSemPermissoes.vue"
import PopupFormStory from "@/components/PopupFormStory.vue"
import { useAppStore } from "@/stores/appStore"
export default {
  
  components: {
    AppNavBar,
    TaskSemPermissoes,
    PopupFormStory
  },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: null,
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
    addNewTask(task) {
      this.loading = true
      TasksApi.addNewTask(task.title).then((task) => {
        this.appStore.showSnackbar(`Sua história sem graça foi adicionada #${task.id}`)
        this.loading = false
      })
    },    
  }
}
</script>

<style>
  template {
    background-color: white !important;
  }
  .background-principal {
    background: #fffaaf;
  }
  .v-card-text {
    min-height: 200px;
  }
</style>