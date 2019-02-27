<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <img class="card-img-top" :src="user.avatar" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">{{user.full_name}}</h5>
            <p class="card-text">{{user.email}}</p>
            <p class="badge badge-primary" v-if="user.is_employee">Employeee</p>
            <p class="badge badge-danger" v-else>Not Employeee</p>
          </div>
        </div>
      </div>
      <div class="col-md-8">
        <h3>Profile Info</h3>
        <p>Nationality:</p>
        <p>{{user.nationality}}</p>
        <p>Age:</p>
        <p>{{user.age}}</p>
        <p>Phone:</p>
        <p>{{user.phone_number}}</p>
        <h3>Work related Info</h3>
        <p>Sector:</p>
        <p v-if="user.sector">{{user.sector.name}}</p>
        <p>Skills:</p>
        <div v-if="user.skills">
          <span v-for="skill in user.skills" style="margin-right: 5px;" class="badge badge-dark">{{skill.name}}</span>
        </div>
        <p>Salary:</p>
        <p>{{user.salary}} BGN</p>
        <p>Days in Company:</p>
        <p>{{user.days_in_company}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.component('user-retrive-item', {
  name: "UserRetrive",
  props: ['user'],
})
</script>
