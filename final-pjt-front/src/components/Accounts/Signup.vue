<template>
  <div class="signup" style="margin-top:50px">
    <div class="mx-auto my-1 d-flex flex-row justify-content-between align-items-center" style="width:280px">
      <label for="username" class="mb-0">사용자 이름: </label>
      <input id="username" v-model="username" type="text" class="rounded" style="width: 175px">
    </div>
    <div class="mx-auto my-1 d-flex flex-row justify-content-between align-items-center" style="width:280px">
      <label for="password" class="mb-0">비밀번호: </label>
      <input id="password" v-model="password" type="password" class="rounded" style="width: 175px">
    </div>
    <div class="mx-auto my-1 d-flex flex-row justify-content-between align-items-center" style="width:280px">
      <label for="passwordConfirmation" class="mb-0">비밀번호 확인: </label>
      <input
        id="passwordConfirmation"
        v-model="passwordConfirmation"
        @keydown.enter="signUp"
        type="password"
        class="rounded"
        style="width: 175px"
      >
    </div>

    <br>

    <button class="btn btn-outline-warning m-2" @click="signUp">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'Signup',
  data () {
    return {
      username: '',
      password: '',
      passwordConfirmation: '',
    }
  },
  methods: {
    signUp () {
      if (!(this.password === this.passwordConfirmation)) {
        return alert('비밀번호가 서로 다릅니다')
      }

      const userItem = {
        username: this.username,
        password: this.password,
        passwordConfirmation: this.passwordConfirmation,
      }

      axios.post(`${SERVER_URL}/accounts/signup/`, userItem)
      .then( () => {
        this.$router.push({ name: 'Login' })
      })
      .catch( error => {
        console.log(error)
        alert('존재하는 아이디입니다')
      })
    }
  }
}
</script>

<style>
.signup {
  color:#FFCA3D;
  height:600px;
}
</style>
