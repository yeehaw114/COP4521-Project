<template>
    <div class="text-red-lighten-1">Error: {{ props.text }}</div>
</template>

<script setup lang="ts">

const props = defineProps({
    text: {
        type: String,
        required: true
    }
})

</script>