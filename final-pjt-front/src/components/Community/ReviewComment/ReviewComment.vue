<template>
  <div class="px-3">
    <h4 class="text-left" style="color:#FFFFFF">댓글 목록</h4>

    <hr class="bg-warning">

    <RCommentCard
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      @deleteReviewComment="deleteReviewComment"
    />
    <RCommentForm
      :selectedReview="selectedReview"
      @createcomment="createcomment"
    />
  </div>
</template>

<script>
import axios from 'axios'

import RCommentForm from './RCommentForm'
import RCommentCard from './RCommentCard'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'ReviewComment',
  data () {
    return {
      comments: '',
    }
  },
  components: {
    RCommentForm,
    RCommentCard,
  },
  props: {
    selectedReview: [String, Object],
  },
  methods: {
    readcomments () {
      const reviewItem = {
        review: this.selectedReview,
      }

      if (reviewItem.review) {
        axios.post(`${SERVER_URL}/community/comment/`, reviewItem)
        .then( response => {
          this.comments = response.data
        })
        .catch( error => {
          console.log(error)
        })
      }
    },
    createcomment () {
      this.readcomments()
    },
    deleteReviewComment () {
      this.readcomments()
    }
  },
  created () {
    this.readcomments()
  }
}
</script>

<style scoped>

</style>