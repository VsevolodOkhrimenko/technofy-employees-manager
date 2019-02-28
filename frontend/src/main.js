import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import App from '@/App.vue'
import './registerServiceWorker'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
