<template>
  <div class="d-flex flex-row justify-content-center align-items-center">
    <star-rating v-model="rating" :increment="0.5" :star-size="30" :show-rating="false" @rating-selected="setRating"/>
    <span v-if="selectedComment">
      <input @keydown.enter="updateMovieComment" v-model.trim="content" class="rounded" style="width: 175px" type="text" >
      <button class="btn btn-outline-warning m-2" @click="updateMovieComment">덧글 수정</button>
    </span>
    <span v-else>
      <input @keydown.enter="createMovieComment" v-model.trim="content" class="rounded" style="width: 175px" type="text">
      <button class="btn btn-outline-warning m-2" @click="createMovieComment">덧글 작성</button>
    </span>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import StarRating from 'vue-star-rating'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'MCommentForm',
  data () {
    return {
      content: '',
      rating: 0,
    }
  },
  components: {
    StarRating,
  },
  props: {
    selectedMovie: [String, Object],
    selectedComment: [String, Object],
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
    setRating: function (rating) {
      this.rating=rating
    },
    createMovieComment () {
      if (!this.isLogin) {
        return this.$router.push({ name: 'Login' })
      }

      const config = this.setToken()

      const movieCommentItem = {
        content: this.content,
        rating: 2 * this.rating,
        movie: this.selectedMovie,
      }

      if (movieCommentItem.content && movieCommentItem.movie) {
        axios.post(`${SERVER_URL}/movies/comment/create/`, movieCommentItem, config)
        .then( () => {
          this.content = ''
          this.rating = 0
          this.$emit('createcomment')
        })
        .catch( error => {
          console.log(error)
        })
      }
    },
    updateMovieComment () {
      const config = this.setToken()

      const movieCommentItem = {
        commentId: this.selectedComment.id,
        content: this.content,
        rating: 2 * this.rating,
        movie: this.selectedMovie,
      }

      if (movieCommentItem.content && movieCommentItem.movie) {
        axios.put(`${SERVER_URL}/movies/comment/update-delete/`, movieCommentItem, config)
        .then( () => {
          console.log('덧글갱신 성공')
          this.content = ''
          this.rating = 0
          this.$emit('updateCompleteComment')
        })
        .catch( error => {
          console.log(error)
        })
      }
    }
  },
  computed: {
    ...mapState([
      'isLogin'
    ])
  },
  watch: {
    selectedComment () {
      this.content = this.selectedComment.content
      this.rating = this.selectedComment.score/2
    }
  }
}
</script>

<style>

</style>