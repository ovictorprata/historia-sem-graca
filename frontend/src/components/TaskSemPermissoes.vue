<template>
<div>
  <v-card
    class="mx-auto title "
    color="#dbd467"
    max-width="400"

    
    :title="'história - #' + String(task.id)"
  >
    
    <v-card-text class="text-black text-h5 py-2 bg-white">
      {{ task.description }}
    </v-card-text>

    <hr color="grey">
    <v-card-actions>
    <!-- <v-list-item-title>asdasdasdasds</v-list-item-title> -->
      <v-list-item class="w-100">
        <template #append>
          <div class="justify-self-end">
            <span class="subheading me-2 font-weight-bold">{{ fake_like }}</span>
                  <v-icon class="me-1 like" icon="mdi-thumb-up" color="grey-darken-1" @click="addLike()"></v-icon>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
  </div>
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
    emits: ["newLike"],
  data: () => ({
    fake_like: 0,
    click: false,
  }),
  methods: {
    addLike() {
      if(this.click === true) {
        this.fake_like -= 1
        this.click = false
      } else {
        this.fake_like += 1
        this.click = true
      }
  }
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

  .v-card-item {
    background: white !important;
    text-decoration: underline;
  }
</style>