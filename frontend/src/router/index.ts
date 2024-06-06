import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import CreateView from '../views/CreateView.vue'
import WorkoutView from '../views/WorkoutView.vue'

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
    {
      path: '/create',
      name: 'create',
      component: CreateView
    },
    {
      path: '/workouts',
      name: 'workouts',
      component: WorkoutView
    }
  ]
})

export default router
