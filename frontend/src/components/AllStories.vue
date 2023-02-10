<template>
  <v-card
    class="mx-auto title"
    color="#fffaaf"
    theme="dark"
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
  data: () => ({}),
}
</script>
