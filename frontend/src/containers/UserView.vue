<template>
    <div>
        <h2>User</h2>
        <user-retrive-item :user="user"></user-retrive-item>
    </div>
</template>

<script>
import axios from "axios"
import router from "../router"
import store from "../store"
import UserRetrive from '@/components/UserRetrive.vue'

export default {
  name: "UserView",
  data () {
    return {
      user: {},
    }
  },
  methods: {
    getUserData: function () {
      let self = this;
      axios.get(`/api/users/${this.$route.params.id}`)
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
    store.commit('setActiveNav', 'user-list');
  }
}
</script>
