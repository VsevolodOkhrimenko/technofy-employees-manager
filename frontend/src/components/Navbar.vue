<template>
  <nav class="navbar navbar-expand-lg fixed-top navbar navbar-light">
    <router-link class="navbar-brand" to="/"><img src="/img/logoblue.png" /></router-link>
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

<style>
  nav.navbar {
    background-color: #fff;
    -webkit-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.75);
    box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.75);
  }
  .navbar-light .navbar-nav .nav-link {
    color: #0d2749;
    font-weight: 600;
  }
  .navbar-light .navbar-nav .nav-link.active {
    border-bottom: 2px solid #e38f34;
    color: #e38f34;
  }
  .navbar-light .navbar-nav .nav-link:hover {
    color: #e38f34;
  }
  .navbar .btn-outline-info {
    border-color: #0d2749;
    color: #0d2749;
    font-weight: 600;
  }
  .navbar .btn-outline-info:hover {
    background-color: #e38f34;
    color: #fff;
    border-color: #ce802c;
  }
  .navbar .btn-outline-info:focus {
    box-shadow: 0 0 0 0.2rem  #e0971080;
  }
</style>

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
