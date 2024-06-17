import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import CreateWorkoutView from '../views/CreateWorkoutView.vue'
import WorkoutView from '../views/WorkoutView.vue'
import CreateLogView from '../views/CreateLogView.vue'
import LogView from '@/views/LogView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    //The actual real important routes below
    {
      path: '/workout/create',
      name: 'create',
      component: CreateWorkoutView
    },
    {
      path: '/workout/:workoutid/log',
      name: 'log',
      component: CreateLogView
    },
    {
      path: '/workout/:workoutid',
      name: 'workoutview',
      component: WorkoutView
    },
    {
      path: '/workout/:workoutid/log/:logid',
      name: 'logview',
      component: LogView
    }
  ]
})

export default router
