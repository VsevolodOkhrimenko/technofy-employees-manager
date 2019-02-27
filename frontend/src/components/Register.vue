<template>
    <div>
        <h2>Register</h2>
        <form v-on:submit.prevent="signUp">
          <div v-if="error" class="alert alert-danger" role="alert">
            {{error}}
          </div>
          <div class="form-group">
            <label for="first_name">First name</label>
            <input
              required
              id="first_name"
              class="form-control"
              type="text"
              ref="first_name"
              name="first_name"
              placeholder="Enter your first name"
            />
          </div>
          <div class="form-group">
            <label for="last_name">Last name</label>
            <input
              required
              id="last_name"
              class="form-control"
              type="text"
              ref="last_name"
              name="last_name"
              placeholder="Enter your last name"
            />
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
          <button type="submit" class="btn btn-primary">Register</button>
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
            self.$set(this, "error", errors.response.data.error);
          })
      }
      signUp();
    }
  }
})
</script>
