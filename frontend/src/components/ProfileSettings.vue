<template>
    <div>
        <h2>Profile</h2>
        <form v-on:submit.prevent="userSettings">
          <p style="color: red;">{{userError}}</p>
          <input type="text" :value="initialVals.first_name" ref="first_name" name="first_name"/><br>
          <input type="text" :value="initialVals.last_name"  ref="last_name" name="last_name"/><br>
          <input type="email" :value="initialVals.email" ref="email" name="email"/><br>
          <input type="password" name="new_password" ref="new_password"/><br>
          <input type="submit" value="Save User Settings"/>
        </form>
        <form v-on:submit.prevent="profileSettings">
          <p style="color: red;">{{profileError}}</p>
          <input type="number" :value="initialVals.age" ref="age" name="age"/><br>
          <input type="text" :value="initialVals.nationality" ref="nationality" name="nationality"/><br>
          <input type="tel" :value="initialVals.phone_number" ref="phone_number" name="phone_number"/><br>
          <p>Sector</p>
          <input type="text" v-model="initialVals.sector.name" ref="sector" list="sectors" @input="sectorAutocomplete"/>
          <datalist id="sectors">
            <option v-for="sector in sectors" :value="sector.value" :text="sector.text"/>
          </datalist>
          <p>Skills</p>
          <input type="text" ref="skill" list="skills" @input="skillAutocomplete" @change="skillChange"/><br>
          <datalist id="skills">
            <option v-for="skill in skills" :value="skill.value" :text="skill.text"/>
          </datalist>
          <div style="width: 100%;">
            <span
              style="cursor: pointer; margin-right: 5px;"
              v-for="skill in skillsApplyied"
              @click="deleteSkill"
              :name="skill"
              class="badge badge-pill badge-success"
            >
              {{skill}}
            </span>
          </div>
          <input type="number" :value="initialVals.salary" ref="salary" name="salary"/><br>
          <input type="date" :value="initialVals.started" ref="started" name="started"/><br>
          <input type="date" :value="initialVals.ended" ref="ended" name="ended"/><br>
          <input type="submit" value="Save Profile Settings"/>
        </form>
    </div>
</template>

<script>
import router from "../router"
import store from "../store"
import axios from "axios"
import Vue from 'vue'

export default Vue.component('profile-settings', {
  name: "ProfileSettings",
  data () {
    return {
      userError: null,
      profileError: null,
      initialVals: {
        sector: {
          name: null,
        }
      },
      sector: null,
      sectors: [],
      skills: [],
      skillsApplyied: [],
    }
  },
  methods: {
    userSettings:  function () {
      let first_name = this.$refs.first_name.value;
      let last_name = this.$refs.last_name.value;
      let email = this.$refs.email.value;
      let new_password = this.$refs.new_password.value;
      let self = this;

      let userSettings = () => {
        let data = {
          token: store.getters.getAccessToken,
          first_name: first_name,
          last_name: last_name,
          email: email,
          new_password: new_password,
        }
        axios.post("/api/users/save_user_settings/", data)
          .then((response) => {
            let token = response.data.token;
            store.commit('setAccessToken', token);
          })
          .catch((errors) => {
            self.$set(this, "error", "Invalid data");
          })
      }
      userSettings();
    },
    profileSettings:  function () {
      let age = this.$refs.age.value;
      let nationality = this.$refs.nationality.value;
      let phone_number = this.$refs.phone_number.value;
      let salary = this.$refs.salary.value;
      let started = this.$refs.started.value;
      let sector = this.$refs.sector.value;
      let skills = this.skillsApplyied
      let ended = this.$refs.ended.value;
      let self = this;

      let profileSettings = () => {
        let data = {
          token: store.getters.getAccessToken,
          age: age,
          nationality: nationality,
          phone_number: phone_number,
          salary: salary,
          sector: sector,
          skills: skills,
          started: started? started : null,
          ended: ended ? ended : null,
        }
        axios.post("/api/users/save_profile_settings/", data)
          .then((response) => {
            let id = response.data.id;
          })
          .catch((errors) => {
            self.$set(this, "error", "Invalid data");
          })
      }
      profileSettings();
    },
    getProfileData: function () {
      let self = this;
      axios.get(`/api/users/${store.getters.getUserId}`)
        .then((response) => {
          self.$set(this, "initialVals", response.data);
          let skills = response.data.skills;
          let prepared_skills = []
          for (let i = 0; i < skills.length; i += 1) {
            prepared_skills.push(skills[i].name);
          }
          self.$set(this, "skillsApplyied", prepared_skills);
        })
        .catch((errors) => {
          console.log(errors);
        })
    },
    sectorAutocomplete: function(event) {
      const query = event.target.value;
      var self = this;
      axios.get(`/api/sectors/autocomplete/?q=${query}`)
        .then((response) => {
          const sectors = response.data.map(sector => ({ value: sector.name, text: sector.name }));
          self.$set(this, "sectors", sectors);
        })
        .catch((errors) => {
          console.log(errors);
        })
    },
    skillAutocomplete: function(event) {
      const query = event.target.value;
      var self = this;
      axios.get(`/api/skills/autocomplete/?q=${query}`)
        .then((response) => {
          const skills = response.data.map(skill => ({ value: skill.name, text: skill.name }));
          self.$set(this, "skills", skills);
        })
        .catch((errors) => {
          console.log(errors);
        })
    },
    skillChange: function(event) {
      const skill = event.target.value;
      var self = this;
      let skillsApplyied = self.skillsApplyied;
      var index = skillsApplyied.indexOf(skill);
      if (index === -1) {
        skillsApplyied.push(skill);
        self.$set(this, "skillsApplyied", skillsApplyied);
      }
      self.$set(this, "skills", []);
      event.target.value = "";
    },
    deleteSkill: function(event) {
      const skill = event.target.getAttribute("name");
      var self = this;
      let skillsApplyied = self.skillsApplyied;
      var index = skillsApplyied.indexOf(skill);
      if (index > -1) {
        skillsApplyied.splice(index, 1);
      }
      self.$set(this, "skillsApplyied", skillsApplyied);
    },
  },
  mounted () {
    this.getProfileData();
  }
})
</script>
