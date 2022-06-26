import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../components/Home.vue'
import Recommend from '../components/Recommend/Recommend.vue'

import MovieDetail from '@/components/Movie/MovieMain/MovieDetail.vue'

import Signup from '@/components/Accounts/Signup.vue'
import Login from '@/components/Accounts/Login.vue'

// import ReviewMain from '@/components/Community/ReviewMain/ReviewMain.vue'
// import ReviewList from '@/components/Community/ReviewMain/ReviewList.vue'
// import ReviewForm from '@/components/Community/ReviewMain/ReviewForm.vue'
// import ReviewDetail from '@/components/Community/ReviewMain/ReviewDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/movie-detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
