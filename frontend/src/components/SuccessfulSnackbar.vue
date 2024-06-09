<template>
    <v-snackbar v-model="value" :timeout="3000"
    >{{ text }}
    <template v-slot:actions>
        <v-btn color="blue" variant="text" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
</template>

<script setup lang="ts">
const props = defineProps({
  text: {
    type: String,
    required: true
  },
  value: {
    type:bool,
  }
})

</script>