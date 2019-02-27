<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link class="navbar-brand" to="/">Employees manager</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav mr-auto">
        <router-link class="nav-item nav-link" :class="{active: getActiveNav === 'dashboard'}" to="/">Dashboard</router-link>
        <router-link class="nav-item nav-link" :class="{active: getActiveNav === 'user-list'}" to="/user-list">Employees list</router-link>
        <router-link class="nav-item nav-link" :class="{active: getActiveNav === 'settings'}" to="/settings">Settings</router-link>
      </div>
      <router-link v-if="getAuthState" class="btn btn-outline-info" to="/auth">Logout</router-link>
      <router-link v-else="getAuthState" class="btn btn-outline-info" to="/auth">Login</router-link>
    </div>
  </nav>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex';
import store from "../store"

export default Vue.component('nav-bar', {
  name: "Navbar",
  methods: {
  },
  computed: {
    ...mapGetters([
      'getActiveNav',
      'getAuthState',
    ])
  },
})
</script>
