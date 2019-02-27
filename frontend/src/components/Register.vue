<template>
    <div>
        <h2>Register</h2>
        <form v-on:submit.prevent="signUp">
          <p style="color: red;">{{error}}</p>
          <input type="text" ref="first_name" name="first_name"/><br>
          <input type="text" ref="last_name" name="last_name"/><br>
          <input type="email" ref="email" name="email"/><br>
          <input type="password" name="password" ref="password"/><br>
          <input type="submit" value="Register"/>
        </form>
    </div>
</template>

<script>
import router from "../router"
import store from "../store"
import axios from "axios"
import Vue from 'vue'

export default Vue.component('register', {
  name: "Register",
  data () {
    return {
      error: null,
    }
  },
  methods: {
    signUp:  function () {
      let first_name = this.$refs.first_name.value;
      let last_name = this.$refs.last_name.value;
      let email = this.$refs.email.value;
      let password = this.$refs.password.value;
      let self = this;

      let signUp = () => {
        let data = {
          first_name: first_name,
          last_name: last_name,
          email: email,
          password: password,
        }

        axios.post("/api/users/register/", data)
          .then((response) => {
            let id = response.data.id;
            let token = response.data.token;
            store.commit('setUserId', id);
            store.commit('setAccessToken', token);
            store.commit('changeAuthState', true);
            router.push("/settings");
          })
          .catch((errors) => {
            self.$set(this, "error", "Invalid data");
          })
      }
      signUp();
    }
  }
})
</script>
