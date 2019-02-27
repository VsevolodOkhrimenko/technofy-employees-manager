<template>
    <div>
        <h2>Login</h2>
        <form v-on:submit.prevent="login">
          <div v-if="error" class="alert alert-danger" role="alert">
            {{error}}
          </div>
          <div class="form-group">
            <label for="email">Email address</label>
            <input
              required
              id="email"
              aria-describedby="emailHelp"
              placeholder="Enter email"
              class="form-control"
              type="email"
              ref="email"
              name="email"
            />
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input
              required
              class="form-control"
              id="password"
              placeholder="Password"
              type="password"
              name="password"
              ref="password"
            />
          </div>
          <button type="submit" class="btn btn-primary">Login</button>
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
            self.$set(this, "error", "Invalid email or password");
          })
      }
      login();
    }
  }
})
</script>
