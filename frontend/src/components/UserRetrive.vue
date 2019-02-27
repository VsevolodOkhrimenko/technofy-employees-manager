<template>
  <div class="row">
    <div class="col-md-4">
      <div class="card">
        <img class="card-img-top" :src="user.avatar" style="width: 100%" alt="Profile image">
        <div class="card-body">
          <h5 class="card-title">
            {{user.full_name}}
            <span class="badge badge-primary" v-if="user.is_employee">Employee</span>
            <span class="badge badge-danger" v-else>Not Employee</span>
          </h5>
          <p><a :href="`mailto:${user.email}`" class="card-text">{{user.email}}</a></p>
        </div>
      </div>
    </div>
    <div class="col-md-8">
      <h3>Profile Info</h3>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">Nationality: {{user.nationality}}</li>
        <li class="list-group-item">Age: {{user.age}}</li>
        <li class="list-group-item">Phone: <a :href="`tel:${user.phone_number}`">{{user.phone_number}}</a></li>
      </ul>
      <h3>Work related Info</h3>
      <ul class="list-group list-group-flush">
        <li v-if="user.sector" class="list-group-item">Sector: {{user.sector.name}}</li>
        <li class="list-group-item">Skills:
          <span v-for="skill in user.skills" style="margin-right: 5px;" class="badge badge-dark">{{skill.name}}</span>
        </li>
        <li v-if="user.salary" class="list-group-item">Salary: {{user.salary}} BGN</li>
        <li class="list-group-item">Days in Company: {{user.days_in_company}} Days</li>
      </ul>
    </div>
  </div>
</template>

<style>
  a {
    color: #528cba;
  }
  a:hover, a:focus {
    color: #e38f34;
  }
  .badge-primary {
    background-color: #528cba;
  }
  .badge-dark {
    padding: .5em .8em;
  }
</style>

<script>
import Vue from 'vue'

export default Vue.component('user-retrive-item', {
  name: "UserRetrive",
  props: ['user'],
})
</script>
