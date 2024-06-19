<template>
  <v-snackbar color="success" :timeout="2000"
    >{{ props.text }}
    <template v-slot:actions> </template>
  </v-snackbar>
</template>

<script setup lang="ts">
const emit = defineEmits(['update:value'])
const props = defineProps({
  text: {
    type: String,
    required: true
  },
  value: {
    type: Boolean
  }
})
</script>
