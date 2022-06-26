<template>
  <div class="signin" style="margin-top:50px">
    <div class="mx-auto my-1 d-flex flex-row justify-content-between align-items-center" style="width:280px">
      <label for="username" class="mb-0">사용자 이름: </label>
      <input id="username" v-model="credentials.username" type="text" class="rounded" style="width: 175px">
    </div>
    <div class="mx-auto my-1 d-flex flex-row justify-content-between align-items-center" style="width:280px">
      <label for="password" class="mb-0">비밀번호: </label>
      <input
        id="password"
        v-model="credentials.password"
        @keydown.enter="logIn"
        type="password"
				class="rounded"
				style="width: 175px" 
      >
    </div>

    <br>

    <button @click="logIn" class="btn btn-outline-warning m-2">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'


const SERVER_URL = process.env.VUE_APP_URL

export default {
	name: 'Login',
	data () {
		return {
			credentials: {
				username: '',
				password: '',
			}
		}
	},
	methods: {
		logIn () {
			axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
			.then( response => {
				localStorage.setItem('jwt', response.data.token)
				localStorage.setItem('myName', this.credentials.username)
				this.$store.dispatch('weAreLogin', true)
				this.$router.push({ name: 'Home' })
			})
			.catch( error => {
				console.log(error)
				alert('아이디 혹은 비밀번호가 맞지 않습니다')
			})
		}
	}
}
</script>

<style>
.signin {
  color:#FFCA3D;
	height:600px;
}
</style>