<template>
  <div class="d-flex flex-row justify-content-center align-items-center">
    <input v-model.trim="content" @keydown.enter="createReviewComment" class="rounded" style="width: 175px" type="text">
    <button @click="createReviewComment" class="btn btn-outline-warning mx-2 py-0" style="height: 30px">작성</button>
  </div>
</template>

<script>
import axios from 'axios'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'RCommentForm',
  data () {
    return {
      content: '',
    }
  },
  props: {
    selectedReview: [String, Object],
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      }
      return config
    },
    createReviewComment () {
      const config = this.setToken()

      const reviewCommentItem = {
        content: this.content,
        review: this.selectedReview,
      }

      if (reviewCommentItem.content && reviewCommentItem.review) {
        axios.post(`${SERVER_URL}/community/comment/create/`, reviewCommentItem, config)
        .then( () => {
          this.content = ''
          this.$emit('createcomment')
        })
        .catch(error => {
          console.log(error)
        })
      }
    }
  }
}
</script>

<style>

</style>