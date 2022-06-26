<template>
  <div>
    <div class="d-flex flex-row justify-content-center mx-5">
      <div class="border border-warning rounded-left px-2 py-3 my-3" style="width: 455px">
        <h4 id="reco">👍👍 추천해요</h4>

        <hr class="bg-light">

        <p id="nocomments" v-if="goodComments.length == 0" class="mb-0">작성된 댓글이 없습니다.</p>
        <span v-else>
          <MCommentCard
            v-for="comment in goodComments"
            :key="comment.id"
            :comment="comment"
            @updateMovieComment="updateMovieComment"
            @deleteCompleteComment="deleteCompleteComment"
          />
        </span>
      </div>

      <div class="border border-warning rounded-right border-left-0 px-2 py-3 my-3" style="width: 455px">
        <h4 id="reco">👎👎 비추해요</h4>

        <hr class="bg-light">

        <p id="nocomments" v-if="badComments.length == 0" class="mb-0">작성된 댓글이 없습니다.</p>
        <span v-else>
          <MCommentCard
            v-for="comment in badComments"
            :key="comment.id"
            :comment="comment"
            @updateMovieComment="updateMovieComment"
            @deleteCompleteComment="deleteCompleteComment"
          />
        </span>
      </div>
    </div>

    <MCommentForm
      :selectedMovie="selectedMovie"
      :selectedComment="selectedComment"
      @createcomment="createcomment"
      @updateCompleteComment="updateCompleteComment"
    />
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

import MCommentForm from './MCommentForm'
import MCommentCard from './MCommentCard'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'MovieComment',
  data () {
    return {
      comments: '',
      selectedComment: '',
    }
  },
  components: {
    MCommentForm,
    MCommentCard,
  },
  props: {
    selectedMovie: [String, Object],
  },
  methods: {
    readcomments () {
      const movieItem = {
        movie: this.selectedMovie,
      }

      if (movieItem.movie) {
        axios.post(`${SERVER_URL}/movies/comment/`, movieItem)
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
    updateMovieComment (pickComment) {
      this.selectedComment = pickComment
    },
    updateCompleteComment () {
      console.log('업데이트에 성공했습니다')
      this.readcomments()
      this.selectedComment = ''
    },
    deleteCompleteComment () {
      console.log('제거에 성공했습니다')
      this.readcomments()
    }
  },
  computed: {
    goodComments () {
      return _.filter(this.comments, (comment) => {
        if (comment.score >= 5) {
          return true
        }
      })
    },
    badComments () {
      return _.filter(this.comments, (comment) => {
        if (comment.score < 5) {
          return true
        }
      })
    },
  },
  created () {
    this.readcomments()
  }
}
</script>

<style>
#movie-comment {
  color: #FFCA3D;
}
#reco {
  color: #FFFFFF;
}
#nocomments {
  color: #FFFFFF;
}
</style>