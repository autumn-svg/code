import { createRouter, createWebHistory } from 'vue-router'
import StudentViews from '../views/StudentViews.vue'
import StudentDetailView from '../views/StudentDetailView.vue'
import SomeView from '../views/SomeView.vue'
import OtherView from '../views/OtherView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'some',
      component: SomeView
    },
    {
      path: '/students',
    name: 'students',
    component: StudentViews
    },
    {
      path: '/students/:name',
      name: 'studentDetail',
      component: StudentDetailView
    },
    {
      path: '/other',
      name: 'other',
      component: OtherView
    },
  ]
})

export default router
