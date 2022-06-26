<template>
  <div id="app">
    <img src="@/assets/logo3_new.png" alt="" style="width:500px" class="m-5">
    <div id="nav" class="pt-0" style="font-size:25px">
      <router-link :to="{ name: 'Home' }">Home</router-link> |
      <router-link :to="{ name: 'Recommend' }">Recommend</router-link> |
      <span v-if="isLogin">
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span>
    </div>
    <router-view />

    <br>

    <footer id="footer">
      <div class="mt-4 p-4">
        <p>본 콘텐츠의 저작권은 저작권자 또는 제공처에 있으며, 이를 무단 이용하는 경우 저작권법 등에 따라 법적 책임을 질 수 있습니다.</p>

        <p>주소 : 서울특별시 강남구 역삼동 테헤란로 212 멀티캠퍼스 | 대표전화 : 1588-3357</p>
        <div class="d-flex flex-row justify-content-center align-items-center">
          <img src="@/assets/logo3.png" style="width:80px;" alt="" class="rounded-lg mx-2">
          <p class="m-0"> Copyright ⓒ2020 JH Movie Review Rating. All Right Reserved</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'App',
  methods: {
    logout () {
      localStorage.removeItem('jwt')
      localStorage.removeItem('myName')
      // this.$store.dispatch('myNameIs', '')
      this.$store.dispatch('weAreLogin', false)
      this.$router.push({ name: 'Home' })
    },
  },
  computed: {
    ...mapState([
      'isLogin'
    ])
  },
  created () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.$store.dispatch('weAreLogin', true)
    }
  },
}
</script>

<style>
#app {
  background-color:#020C53;
  font-family: 'Sunflower', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #FFCA3D;
}

#nav a.router-link-exact-active {
  color: #D94E0C;
}

#footer {
  background-color: #FFCA3D;
}
</style>
