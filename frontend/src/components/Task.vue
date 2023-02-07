<template>
  <v-card>
    <v-card-text>
      <div>#{{ task.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ task.description }}
      </p>
      <v-btn icon="mdi-heart" :to="{ name: 'base-home' }"></v-btn>
      <v-btn icon="mdi-trash-can" :to="{ name: 'base-home' }"></v-btn>
    </v-card-text>

  </v-card>
</template>

<script>
export default {
  name: "TasksModel",
  props: {
    task: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({}),
}
</script>
