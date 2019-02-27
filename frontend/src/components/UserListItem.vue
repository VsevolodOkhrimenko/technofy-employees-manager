<template>
    <a :href="`/user/${user.id}`" class="list-group-item list-group-item-action list-group-item-secondary">
      <div class="card container-fluid">
        <div class="row">
          <div class="col-md-2">
            <img style="width: 100%" class="img" :src="user.avatar" alt="Card image cap">
          </div>
          <div class="col-md-10">
            <div class="card-body">
              <h5 class="card-title">{{user.full_name}}</h5>
              <p class="card-text">
                <ul class="list-group">
                  <li class="list-group-item">Email: {{user.email}}</li>
                  <li class="list-group-item" v-if="user.sector">Sector: {{user.sector.name}}</li>
                  <li class="list-group-item" v-if="user.skills">
                    Skills:
                    <span v-for="skill in user.skills">
                      {{skill.name}}
                    </span>
                  </li>
                  <li class="list-group-item">Salary: {{user.salary}} BGN</li>
                  <li class="list-group-item">Days in company: {{user.days_in_company}}</li>
                </ul>
              </p>
              <a :href="`/user/${user.id}`" class="btn btn-primary">Go to profile</a>
            </div>
          </div>
        </div>
      </div>
    </a>
</template>

<script>
import Vue from 'vue'
export default Vue.component('user-list-item', {
  name: "UserListItem",
  props: ['user'],
})
</script>
