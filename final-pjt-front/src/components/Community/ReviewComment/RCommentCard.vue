<template>
  <div id="review-box" class="d-flex justify-content-between">
    <span>
      {{ comment.user.username }} : {{ comment.content }}
    </span>
    <span>
      <span style="font-size: 0.8rem">{{ this.created }}</span>
      <span v-if="myName == comment.user.username">
        <button @click="deleteReviewComment" class="btn btn-outline-warning mx-1 px-1 py-0">삭제</button>
      </span>
    </span>
  </div>
</template>

<script>
import axios from 'axios'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'RCommentCard',
  data () {
    return {
      created: '',
      myName: localStorage.getItem('myName'),
    }
  },
  props: {
    comment: Object,
  },
  methods: {
    setToken() {
      const token = localStorage.getItem("jwt");

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    deleteReviewComment () {
      const config = this.setToken()

      const commentItem = {
        commentId: this.comment.id
      }

      if (this.comment) {
        axios.post(`${SERVER_URL}/community/comment/delete/`, commentItem, config)
        .then(() => {
          this.$emit('deleteReviewComment', commentItem.commentId)
        })
        .catch(error => {
          console.log(error)
        })
      }
    }
  },
  created () {
    this.created = this.comment.created_at.slice(0,10)+"/"+this.comment.created_at.slice(11,19)
  }
}
</script>

<style scoped>
#review-box {
  color: #FFCA3D;
}
</style>