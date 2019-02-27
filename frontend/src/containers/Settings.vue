<template>
  <div>
    <h2>Settings</h2>
    <profile-settings />
  </div>
</template>

<script>
import axios from "axios"
import router from "../router"
import store from "../store"
import ProfileSettings from "@/components/ProfileSettings.vue"

export default {
  name: "Settings",
  methods: {
  },
  mounted () {
    store.commit('setActiveNav', 'settings');
  }
}
</script>
