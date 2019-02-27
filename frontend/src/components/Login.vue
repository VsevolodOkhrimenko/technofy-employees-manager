<template>
    <div>
        <h2>Login</h2>
        <form v-on:submit.prevent="login">
          <p style="color: red;">{{error}}</p>
          <input type="email" ref="email" name="email"/><br>
          <input type="password" name="password" ref="password"/><br>
          <input type="submit" value="Login"/>
        </form>
    </div>
</template>

<script>
import router from "../router"
import store from "../store"
import axios from "axios"
import Vue from 'vue'

export default Vue.component('login', {
  name: "Login",
  data () {
    return {
      error: null,
    }
  },
  methods: {
    login: function () {
      let email = this.$refs.email.value;
      let password = this.$refs.password.value;
      let self = this;

      let login = () => {
        let data = {
          email: email,
          password: password,
        }

        axios.post("/api/users/login", data)
          .then((response) => {
            let id = response.data.id;
            let token = response.data.token;
            store.commit('setUserId', id);
            store.commit('setAccessToken', token);
            store.commit('changeAuthState', true);
            router.push("/");
          })
          .catch((errors) => {
            self.$set(this, "error", "Invalid login");
          })
      }
      login();
    }
  }
})
</script>
