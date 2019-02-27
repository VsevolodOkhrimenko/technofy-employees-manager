<template>
  <footer class="footer">
    <div class="container">
      <span class="text-muted">©2019 Design with ♥ by Vsevolod Okhrimenko</span>
    </div>
  </footer>
</template>
<style>
  .footer {
      position: fixed;
      bottom: 0;
      width: 100%;
      height: 60px;
      line-height: 60px;
      background-color: #f5f5f5;
      text-align: center;
      z-index: 100;
  }
</style>
<script>
import Vue from 'vue'

export default Vue.component('footer-technofy', {
  name: "Footer",
})
</script>
