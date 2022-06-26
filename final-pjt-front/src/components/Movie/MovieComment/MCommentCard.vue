<template>
  <div class="d-flex row mt-1">
    <star-rating class="mx-1 pb-1 col-3 align-center" :increment="0.5" :star-size="20" :show-rating="false" :rating="comment.score/2" :read-only="true"/>
    <div class="mx-1 my-auto col-5 px-0 text-left" id="movie-comment">
      {{ comment.user.username }} : {{ comment.content }}
    </div>
    <div>
      <button
        class="btn btn-outline-warning mr-1 py-0"
        style="height: 24px"
        @click="updateMovieComment"
        v-if="comment.user.username === myName">
          수정
      </button>
      <button
        class="btn btn-outline-warning mr-1 py-0"
        style="height: 24px"
        @click="deleteMovieComment"
        v-if="comment.user.username === myName">
          삭제
      </button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import StarRating from 'vue-star-rating'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'MCommentCard',
  data () {
    return {
      myName: localStorage.getItem('myName'),
    }
  },
  components: {
    StarRating,
  },
  props: {
    comment: Object,
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt');

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    deleteMovieComment () {
      const config = this.setToken()

      const commentItem = {
        movie: this.selectedMovie,
        commentId: this.comment.id
      }

      if (this.selectedMovie) {
        axios.post(`${SERVER_URL}/movies/comment/update-delete/`, commentItem, config)
        .then( () => {
          this.$emit('deleteCompleteComment', commentItem.commentId)
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
    updateMovieComment () {
      this.$emit('updateMovieComment', this.comment)
    },
  },
  computed: {
    ...mapState([
      'selectedMovie',
    ]),
  },
}
</script>

<style>

</style>