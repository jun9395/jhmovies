<template>
  <div>
    <div class="container row mx-auto">
      <div class="col-6">
        <img :src="selectedMovie.poster_path" alt="..." style="height:400px">
      </div>
      
      <div id="textline-box" class="col-6">
        <h3>{{ selectedMovie.title }}</h3>

        <hr class="bg-warning">

        <div class="d-flex flex-row align-items-center">
          <star-rating :increment="0.05" :star-size="20" :show-rating="false" :rating="selectedMovie.vote_average/2" :read-only="true"/>
          <span class="mt-2 ml-2">{{ selectedMovie.vote_average }}</span>
        </div>

        <hr class="bg-warning">

        <div>
          <span class="font-weight-bold" style="font-size: 1.5rem">장르</span>
          <span v-for="genre in selectedMovie.genres" :key="genre.id"> | {{ genre.name }}</span>
        </div>

        <div class="d-flex justify-content-between">
          <span>개봉일 : {{ selectedMovie.release_date }}</span>
          <span>누적관객: {{ selectedMovie.popularity }}명</span>
        </div>

        <hr class="bg-warning">

        <h4>줄거리</h4>
        <p>{{ selectedMovie.overview }}</p>
      </div>
    </div>

    <hr>  <!-- 댓글, 리뷰 부분 -->

    <div class="d-flex justify-content-center">
      <button
        class="btn btn-outline-warning m-2 mx-5"
        :class="{ active:switchCommentReview == 1 }"
        @click="selectMovieComment">
          Comment
      </button>
      <button
        class="btn btn-outline-warning m-2 mx-5"
        :class="{ active:switchCommentReview == 2 }"
        style="width:92px"
        @click="selectMovieReview">
          Review
      </button>
    </div>

    <br>

    <span v-if="switchCommentReview === 1">
      <MovieComment :selectedMovie="selectedMovie" />
    </span>
    <span v-else-if="switchCommentReview === 2">
      <ReviewMain :selectedMovie="selectedMovie" :selectReview="selectReview" @deleteReview="selectMovieReview" />
    </span>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import StarRating from 'vue-star-rating'

import MovieComment from '@/components/Movie/MovieComment/MovieComment'
import ReviewMain from '@/components/Community/ReviewMain/ReviewMain'

export default {
  name: 'MovieDetail',
  data () {
    return {
      switchCommentReview: 0,
      selectReview: true,
    }
  },
  components: {
    StarRating,
    MovieComment,
    ReviewMain,
  },
  methods: {
    selectMovieComment () {
      this.switchCommentReview = 1
    },
    selectMovieReview () {
      this.$store.dispatch('selectReview', '')
      this.switchCommentReview = 2
      this.selectReview = !this.selectReview
    }
  },
  computed: {
    ...mapState([
      'selectedMovie',
      'isLogin',
    ])
  },
  created () {
    console.log(this.isLogin)
    if (!this.selectedMovie) {
      this.$router.push({ name: "Home" });
    }
  }
}
</script>

<style scoped>
#textline-box {
  text-align: start;
  color: #FFCA3D;
}
</style>