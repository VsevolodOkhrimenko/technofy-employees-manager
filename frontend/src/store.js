import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  strict: true,
  state: {
    isAuth: JSON.parse(localStorage.getItem('isAuth')),
    userList: [],
    id: localStorage.getItem('myId'),
    activeNav: null,
    token: localStorage.getItem('token'),
  },
  mutations: {
    setUserId(state, id) {
      state.id = id;
      localStorage.setItem('myId', id);
    },
    changeAuthState(state, isAuth) {
      state.isAuth = isAuth;
      if (!isAuth) {
        state.id = null;
        localStorage.removeItem('myId');
      }
      localStorage.setItem('isAuth', isAuth);

    },
    setActiveNav(state, page) {
      state.activeNav = page;
    },
    setAccessToken(state, token) {
      localStorage.setItem('token', token);
      state.token = token
    },
  },
  actions: {
  },
  getters: {
    getUserId: () => {
      return store.state.id;
    },
    getActiveNav: () => {
      return store.state.activeNav;
    },
    getAuthState: () => {
      return store.state.isAuth;
    },
    getAccessToken: () => {
      return store.state.token;
    }
  }
})

export default store
