<template>
    <v-container class="bg-surface-variant">
      <v-row no-gutters>
        <v-col
          v-for="n in 3"
          :key="n"
          cols="12"
          sm="4"
        >
          <v-sheet class="ma-2 pa-2">
            <v-card
                class="mx-auto"
                href=""
                max-width="344"
                height="100"
                prepend-icon="mdi-dumbbell"
                rel="noopener"
                target="_blank"
                title="WORKOUT_NAME_GOES_HERE"
            ></v-card>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>

</script>