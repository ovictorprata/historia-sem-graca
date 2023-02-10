<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <!-- <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Tasks </v-card-title>
        </v-card>
      </v-col> -->

      <v-col cols="12">
        <task-form :form-label="'Insira sua história sem graça...'" @new-task="addNewTask" />
      </v-col>

      <hr>
      <p>Confira as histórias sem graça:</p>
      <v-col v-for="item in items" :key="item.id" cols="12">
        <task :task="item" @delete-story="deleteStory"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"
import Task from "@/components/Task.vue"
import TaskForm from "@/components/TaskForm.vue"

export default {
  name: "TasksList",
  components: { Task, TaskForm },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      items: [],
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks() {
      this.loading = true
      TasksApi.getTasks().then((data) => {
        this.items = data.todos
        this.loading = false
      })
    },
    addNewTask(task) {
      this.loading = true
      TasksApi.addNewTask(task.title).then((task) => {
        this.appStore.showSnackbar(`Sua história sem graça foi adicionada #${task.id}`)
        this.getTasks()
        this.loading = false
      })
    },
    deleteStory(story) {
      this.loading = true
      TasksApi.removeTask(story.id).then((data) => {
        this.items = data.todos
        this.loading = false
        this.getTasks()
        
      })
    },
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
