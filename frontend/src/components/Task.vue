<template>
  <v-card
    class="mx-auto title"
    color="#fffaaf"
    max-width="400"
    title="🗿"
  >

    <v-card-text class="text-h5 py-2" color="black">
      {{ task.description }}
    </v-card-text>

    <hr color="grey">
    <v-card-actions>
    <!-- <v-list-item-title>asdasdasdasds</v-list-item-title> -->
      <v-list-item class="w-100">
        <template #append>
          <div class="justify-self-end">
            <span class="subheading me-2">{{ task.likes }}</span>
            <v-icon class="me-1" icon="mdi-trash-can" @click="deleteStory(task.id)"></v-icon>
            <v-icon class="me-1 like" icon="mdi-thumb-up"></v-icon>
            <v-icon class="me-1 dislike" icon="mdi-thumb-down"></v-icon>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "TasksModel",
  props: {
    task: {
      type: Object,
      default: null,
    },
  },
  emits: ["deleteStory"],
  data: () => ({
    id: ''
  }),
  methods: {
    deleteStory(id) {
      this.id = id
      this.$emit("deleteStory", {
        id: this.id
      })
    },
  }
}
</script>

<style>
  .title {
    color: black;
  }

  .like {
    color: green
  }

  .dislike {
    color: red
  }
</style>