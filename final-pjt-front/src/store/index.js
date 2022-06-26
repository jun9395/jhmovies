import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    selectedMovie: '',
    selectedReview: '',
  },
  getters: {
  },
  mutations: {
    WEARELOGIN (state, trigger) {
      state.isLogin = trigger
    },
    SELECTMOVIE (state, movie) {
      state.selectedMovie = movie
    },
    SELECTREVIEW (state, review) {
      state.selectedReview = review
    }
  },
  actions: {
    weAreLogin (context, trigger) {
      context.commit('WEARELOGIN', trigger)
    },
    selectMovie (context, movie) {
      context.commit('SELECTMOVIE', movie)
    },
    selectReview (context, review) {
      context.commit('SELECTREVIEW', review)
    },
  },
})
