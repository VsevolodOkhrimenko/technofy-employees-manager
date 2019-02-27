<template>
    <div class="container">
        <form v-on:submit.prevent="userSettings">
          <h3>User settings</h3>
          <div v-if="userError" class="alert alert-danger" role="alert">
            {{userError}}
          </div>
          <div v-if="successUsersSettings" class="alert alert-success" role="alert">
            User Settings saved!
          </div>
          <div class="form-group">
            <label for="first_name">First name</label>
            <input
              required
              id="first_name"
              :value="initialVals.first_name"
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
              :value="initialVals.last_name"
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
              :value="initialVals.email"
              placeholder="Enter email"
              class="form-control"
              type="email"
              ref="email"
              name="email"
            />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input
              required
              class="form-control"
              id="password"
              placeholder="Password"
              type="password"
              name="new_password"
              ref="new_password"
            />
          </div>
          <button type="submit" class="btn btn-primary">Save User Settings</button>
        </form>
        <hr />
        <form v-on:submit.prevent="profileSettings">
          <h3>Profile settings</h3>
          <div v-if="profileError">
            <div v-for="errors in profileError">
              <div v-for="error in errors" class="alert alert-danger" role="alert">
                {{error}}
              </div>
            </div>
          </div>
          <div v-if="successProfileSettings" class="alert alert-success" role="alert">
            Profile Settings saved!
          </div>
          <div class="form-group">
            <label for="avatar">Avatar Image</label>
            <input
              type="file"
              class="form-control-file"
              id="avatar"
              ref="avatar"
              name="avatar"
              @change="handleFileUpload"
            >
          </div>
          <div class="form-group">
            <label for="age">Age</label>
            <input
              :value="initialVals.age"
              class="form-control"
              id="age"
              placeholder="Age"
              type="number"
              name="age"
              ref="age"
            />
          </div>
          <div class="form-group">
            <label for="nationality">Nationality</label>
            <input
              :value="initialVals.nationality"
              class="form-control"
              id="nationality"
              placeholder="Nationality"
              type="text"
              name="nationality"
              ref="nationality"
            />
          </div>
          <div class="form-group">
            <label for="phone_number">Phone number</label>
            <input
              :value="initialVals.phone_number"
              class="form-control"
              id="phone_number"
              placeholder="Phone number"
              type="tel"
              name="phone_number"
              ref="phone_number"
            />
          </div>
          <div class="form-group">
            <label for="sectorInput">Sector</label>
            <input
              id="sectorInput"
              class="form-control"
              v-model="sector.name"
              type="text"
              ref="sector"
              list="sectors"
              placeholder="Enter your sector"
              @input="sectorAutocomplete"
            />
            <datalist id="sectors">
              <option v-for="sector in sectors" :value="sector.value" :text="sector.text"/>
            </datalist>
          </div>
          <div class="form-group">
            <label for="skillsInput">Skills</label>
            <input
              id="skillsInput"
              class="form-control"
              type="text"
              ref="skill"
              list="skills"
              placeholder="Enter your skills"
              @input="skillAutocomplete"
              @change="skillChange"
            />
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
                {{skill}} &#10006;
              </span>
            </div>
          </div>
          <div class="form-group">
            <label for="salary">Salary in BGN</label>
            <input
              :value="initialVals.salary"
              class="form-control"
              id="salary"
              placeholder="Salary in BGN"
              type="number"
              name="salary"
              ref="salary"
            />
          </div>
          <div class="form-group">
            <label for="started">Started in company</label>
            <input
              :value="initialVals.started"
              class="form-control"
              id="started"
              placeholder="Started in company"
              type="date"
              name="started"
              ref="started"
            />
          </div>
          <div class="form-group">
            <label for="ended">Ended work in company</label>
            <input
              :value="initialVals.ended"
              class="form-control"
              id="ended"
              aria-describedby="endedHelp"
              placeholder="Salary in BGN"
              type="date"
              name="ended"
              ref="ended"
            />
            <small id="endedHelp" class="form-text text-muted">Leave this field blank, if you're still part of the company.</small>
          </div>
          <div style="margin-bottom: 20px;" class="custom-control custom-checkbox">
            <input
              name="is_archived"
              ref="is_archived"
              :checked="initialVals.is_archived"
              type="checkbox"
              class="custom-control-input"
              id="isArchived"
            />
            <label class="custom-control-label" for="isArchived" aria-describedby="archivedHelp">Archive My Profile</label>
            <small id="archivedHelp" class="form-text text-muted">If marked, will make your profile invisible in Employees list.</small>
          </div>
          <button type="submit" class="btn btn-primary">Save Profile Settings</button>
        </form>
    </div>
</template>

<style>
  .badge-success {
    padding: .5em .8em;
  }
</style>

<script>
import router from "../router"
import store from "../store"
import axios from "axios"
import Vue from 'vue'

export default Vue.component('profile-settings', {
  name: "ProfileSettings",
  data () {
    return {
      avatar: '',
      userError: null,
      profileError: null,
      initialVals: {
        sector: {
          name: null,
        }
      },
      sector: {
        name: null,
      },
      sectors: [],
      skills: [],
      skillsApplyied: [],
      successUsersSettings: false,
      successProfileSettings: false,
    }
  },
  methods: {
    handleFileUpload: function() {
      let self = this;
      self.$set(this, "avatar", this.$refs.avatar.files[0]);
      debugger;
    },
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
            self.$set(this, "successUsersSettings", true);
            self.$set(this, "userError", null);
            self.getProfileData();
          })
          .catch((errors) => {
            self.$set(this, "userError", errors.response.data.error);
            self.$set(this, "successUsersSettings", false);
          })
      }
      userSettings();
    },
    profileSettings:  function () {
      let avatar = this.avatar;
      let age = this.$refs.age.value;
      let nationality = this.$refs.nationality.value;
      let phone_number = this.$refs.phone_number.value;
      let salary = this.$refs.salary.value;
      let started = this.$refs.started.value;
      let sector = this.$refs.sector.value;
      let skills = this.skillsApplyied
      let ended = this.$refs.ended.value;
      let is_archived = this.$refs.is_archived.checked;
      let self = this;

      let profileSettings = () => {
        let formData = new FormData();
        if (avatar) {
          formData.append('avatar', avatar);
        }
        let data = {
          token: store.getters.getAccessToken,
          age: age,
          nationality: nationality,
          phone_number: phone_number,
          salary: salary != 0 ? salary : null,
          sector: sector,
          skills: skills,
          started: started ? started : null,
          ended: ended ? ended : null,
          is_archived: is_archived,
        }
        Object.keys(data).forEach(function(key) {
            formData.append(key, data[key])
        });
        axios.post("/api/users/save_profile_settings/", formData, {
            'Content-Type': 'multipart/form-data',
          })
          .then((response) => {
            self.$set(this, "successProfileSettings", true);
            self.$set(this, "profileError", null);
            self.getProfileData();
          })
          .catch((errors) => {
            self.$set(this, "successProfileSettings", false);
            self.$set(this, "profileError", errors.response.data);
          })
      }
      profileSettings();
    },
    getProfileData: function () {
      let self = this;
      axios.get(`/api/users/${store.getters.getUserId}`)
        .then((response) => {
          self.$set(this, "initialVals", response.data);
          console.log(response.data)
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
