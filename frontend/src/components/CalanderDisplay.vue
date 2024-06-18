<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="today"
          :events="events"
          color="primary"
          type="month"
        ></v-calendar>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { useDate } from 'vuetify'

interface Workout {
  title: string
  date: string
}

interface CalendarEvent {
  name: string
  start: string
  end: string
  color: string
  allDay: boolean
}

export default defineComponent({
  setup() {
    const today = ref(new Date().toISOString().substr(0, 10))
    const events = ref<CalendarEvent[]>([])

    const fetchWorkouts = ({ start, end }: { start: Date; end: Date }) => {
      const workouts: Workout[] = [
        { title: 'Run', date: '2024-06-01' },
        { title: 'Swim', date: '2024-06-03' },
        { title: 'Yoga', date: '2024-06-05' }
        // Add more predefined workouts here
      ]

      events.value = workouts.map((workout) => ({
        name: workout.title,
        start: workout.date,
        end: workout.date,
        color: 'blue', // Default color for visibility
        allDay: true
      }))
    }

    onMounted(() => {
      const adapter = useDate()
      fetchWorkouts({
        start: adapter.startOfDay(adapter.startOfMonth(new Date())),
        end: adapter.endOfDay(adapter.endOfMonth(new Date()))
      })
    })

    return {
      today,
      events
    }
  }
})
</script>
