import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from '@/containers/Dashboard.vue'
import UserList from '@/containers/UserList.vue'
import UserView from '@/containers/UserView.vue'
import Settings from '@/containers/Settings.vue'
import Auth from '@/containers/Auth.vue'
import store from "./store"

const routes = [
  {path: '/', component: Dashboard},
  {path: '/auth', component: Auth},
  {path: '/user-list', component: UserList},
  {path: '/user/:id', component: UserView},
  {path: '/settings', component: Settings},
  {path: '/logout', redirect: '/auth'},
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})
router.beforeEach((to, from, next) => {
  if (!store.getters.getAuthState) {
    next('/auth');
  } else {
    next();
  }
})

export default router
