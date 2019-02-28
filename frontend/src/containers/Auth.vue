<template>
  <div class="container">
    <h2>Auth</h2>
    <ul id="tabsJustified" class="nav nav-tabs">
      <li class="nav-item"><a href="" data-target="#login" data-toggle="tab" class="nav-link small text-uppercase active">Login</a></li>
      <li class="nav-item"><a href="" data-target="#register" data-toggle="tab" class="nav-link small text-uppercase">Register</a></li>
    </ul>
    <br>
    <div id="tabsJustifiedContent" class="tab-content">
        <div id="login" class="tab-pane fade active show">
          <login/>
        </div>
        <div id="register" class="tab-pane fade">
          <register/>
        </div>
    </div>
  </div>
</template>

<style>
  .nav-tabs .nav-link {
    color: #0d2749;
    font-weight: 600;
  }
  .nav-tabs .nav-link:hover {
    color: #e38f34;
  }
  .nav-tabs .nav-link.active {
    color: #e38f34;
  }
</style>

<script>
import axios from "axios"
import router from "../router"
import store from "../store"
import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'

export default {
  name: "Auth",
  methods: {
  },
  mounted () {
    store.commit('changeAuthState', false);
    store.commit('setAccessToken', null);
  }
}
</script>
