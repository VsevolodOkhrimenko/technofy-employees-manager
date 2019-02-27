<template>
    <div>
        <h2>Dashboard</h2>
        <user-retrive-item :user="user"></user-retrive-item>
    </div>
</template>

<script>
import axios from "axios"
import router from "../router"
import store from "../store"
import UserRetrive from '@/components/UserRetrive.vue'

export default {
  name: "Dashboard",
  data () {
    return {
      user: {},
    }
  },
  methods: {
    getUserData: function () {
      let self = this;
      axios.get(`/api/users/${store.getters.getUserId}`)
        .then((response) => {
          self.$set(this, "user", response.data);
        })
        .catch((errors) => {
          console.log(errors);
        })
    }
  },
  mounted () {
    this.getUserData();
    store.commit('setActiveNav', 'dashboard');
  }
}
</script>
