import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EditAreaView from '../views/EditAreaView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/Areas',
    name: 'areas',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "areas" */ '../views/AreasView.vue')
  },
  {
    path: '/Areas/Agregar',
    name: 'addarea',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "addarea" */ '../views/AddAreaView.vue')
  },
  {
    path: '/Areas/Editar/:id',
    name: 'editarea',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => EditAreaView
  },
  {
    path: '/activos',
    name: 'activos',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "areas" */ '../views/ActivosView.vue')
  },
  {
    path: '/activos/Agregar',
    name: 'addactivos',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "areas" */ '../views/AddActivoView.vue')
  },
  {
    path: '/activos/Editar/:id',
    name: 'editactivos',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "areas" */ '../views/EditActivoView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
