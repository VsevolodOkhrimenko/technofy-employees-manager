<template lang="html">
  <div style="margin-bottom: 80px; margin-top: 80px;">
    <nav-bar/>
    <router-view/>
    <footer-technofy/>
  </div>
</template>

<style>
  .btn-primary {
    background-color: #e38f34;
    font-weight: 600;
    color: #fff;
    border-color: #e38f34;
  }
  .btn-primary:hover, .btn-primary:focus {
    background-color: #528cba;
    border-color: #528cba;
    box-shadow: 0 5px 20px 5px rgba(13, 39, 73, 0.2);
  }
  body {
    color: #0d2749;
  }
</style>

<script>
  import Navbar from '@/components/Navbar.vue'
  import Footer from '@/components/Footer.vue'
  export default {
    name: 'App'
  }
</script>
