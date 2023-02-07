<template>
  <v-card
    class="mx-auto title"
    color="#fffaaf"
    theme="dark"
    max-width="400"
    prepend-icon="mdi-face-man-outline"
    title="HSG"
  >

    <v-card-text class="text-h5 py-2" color="black">
      {{ task.description }}
    </v-card-text>

            <hr>
    <v-card-actions>
    <v-list-item-title>asdasdasdasds</v-list-item-title>
      <v-list-item class="w-100">
        <template #append>
          <div class="justify-self-end">
            <span class="subheading me-2">{{ task.like }}</span>
            <v-icon class="me-1 like" icon="mdi-thumb-up"></v-icon>
            <v-icon class="me-1 dislike" icon="mdi-thumb-down"></v-icon>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

  <!-- <v-card
    class="mx-auto"
    color="#fffaaf"
    dark
    max-width="400"
  >
    <v-card-text class="text-h5 font-weight-bold">
      {{ task.description }}
    </v-card-text>
    <v-btn icon="mdi-heart" :to="{ name: 'base-home' }"></v-btn>
    <v-btn icon="mdi-trash-can" :to="{ name: 'base-home' }"></v-btn>
    <v-card-actions>
     
    </v-card-actions>
  </v-card> -->

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