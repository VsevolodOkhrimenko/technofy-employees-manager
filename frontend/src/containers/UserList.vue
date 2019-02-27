<template>
    <div class="container">
        <h2>User List</h2>
        <div class="row">
          <div class="col-md-3">
            <form ref="filter">
              <h4>Filter</h4>
              <div class="form-group">
                <label for="sortSelect">Sort by</label>
                <select class="form-control" id="sortSelect" @change="sortChange" :value="sortBy">
                  <option value="first_name">Name</option>
                  <option value="salary">Salary</option>
                  <option value="started">Arriving date</option>
                </select>
              </div>
              <div class="form-group">
                <label for="sectorInput">Sector</label>
                <input
                  id="sectorInput"
                  class="form-control"
                  v-model="sector"
                  type="text"
                  ref="sector"
                  list="sectors"
                  @change="sectorChange"
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
              <div class="custom-control custom-checkbox">
                <input :checked="notEmployee" @change="notEmployeeChange" type="checkbox" class="custom-control-input" id="notemployee">
                <label class="custom-control-label" for="notemployee">No longer in the company</label>
              </div>

            </form>
          </div>
          <div class="col-md-9">
            <div class="list-group" v-for="user in users">
              <user-list-item :user="user"></user-list-item>
            </div>
          </div>
        </div>
    </div>
</template>

<style>
  form {
    border: 1px solid #528cba;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 20px;
  }
  .badge-success {
    padding: .5em .8em;
  }
  .badge-success:hover {
    opacity: .8;
  }
</style>

<script>
import axios from "axios"
import router from "../router"
import store from "../store"
import UserListItem from '@/components/UserListItem.vue'

export default {
  name: "UserList",
  data () {
    return {
      users: [],
      sectors: [],
      skillsApplyied: [],
      skills: [],
      sortBy: 'first_name',
      notEmployee: false,
      sector: null,
      initSector: null,
      query: localStorage.getItem("query"),
    }
  },
  methods: {
    initFilterParams: function () {
      let self = this;
      let query = localStorage.getItem("query");
      if (!query) {
        return;
      }
      let queryParams = query.split('&');
      var i = queryParams.length;
      var x;
      var params;
      while (i--) {
        if (!queryParams[i]) {
          break;
        }
        x = queryParams[i].split('=');
        if (x[1] != undefined) {
          params = x[1].split('|');
          for (var j = 0; j < params.length; j += 1) {
            if (!params[j]) {
              break;
            }
            if (x[0] == 'skills') {
              const skills = params[j].split(",");
              self.$set(this, "skillsApplyied", skills);
            }
            else if (x[0] == 'sort') {
              const sort = params[j];
              self.$set(this, "sortBy", sort);
            }
            else if (x[0] == 'is_employee') {
              const is_employee = params[j];
              self.$set(this, "notEmployee", is_employee === 'false');
            }
            else if (x[0] == 'sector') {
              const sector = params[j];
              self.$set(this, "sector", sector);
              self.$set(this, "initSector", sector);
            }
          }
        }
      }
      this.filterSubmit();
    },
    getUserData: function () {
      let self = this
      axios.get("/api/users")
        .then((response) => {
          self.$set(this, "users", response.data)
        })
        .catch((errors) => {
          console.log(errors)
        })
    },
    filterSubmit: function () {
      let self = this
      let query = "";
      if (self.sortBy) {
        query = `${query}&sort=${self.sortBy}`;
      }
      if (self.notEmployee) {
        query = `${query}&is_employee=${!self.notEmployee}`
      }
      if (self.sector) {
        query = `${query}&sector=${self.sector}`;
      }
      if (self.skillsApplyied) {
        query = `${query}&skills=${self.skillsApplyied}`
      }
      localStorage.setItem("query", query);
      axios.get(`/api/users?${query}`)
        .then((response) => {
          self.$set(this, "users", response.data)
        })
        .catch((errors) => {
          console.log(errors)
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
    sectorChange: function(event) {
      let self = this
      const sector = event.target.value;
      self.$set(this, "sector", sector);
      this.filterSubmit();
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
      this.filterSubmit();
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
      this.filterSubmit();
    },
    sortChange: function(event) {
      const sortBy = event.target.value;
      var self = this;
      self.$set(this, "sortBy", sortBy);
      this.filterSubmit();
    },
    notEmployeeChange: function(event) {
      const notEmployee = event.target.checked;
      var self = this;
      self.$set(this, "notEmployee", notEmployee);
      this.filterSubmit();
    },
  },
  mounted () {
    store.commit('setActiveNav', 'user-list');
    this.getUserData();
    this.initFilterParams();
  }
}
</script>
