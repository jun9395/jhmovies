<template>
  <div>
    <span v-if="selectedReview">
      <ReviewDetail />
    </span>
    <span v-else>
      <div class='d-flex flex-row justify-content-between' style="color:#FFFFFF;">
        <h4 class="ml-3 mb-0 text-left">리뷰</h4>
        <p class="mr-3 mb-0">{{ reviews.length }}개</p>
      </div>
      <hr class="mt-1 bg-white">
      <p style="color:#FFFFFF" v-if="reviews.length == 0">작성된 리뷰가 없습니다.</p>
      <ReviewCard v-for="review in reviews" :key="review.id" :review="review" />
    </span>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

import ReviewCard from './ReviewCard'
import ReviewDetail from './ReviewDetail'


const SERVER_URL = process.env.VUE_APP_URL;

export default {
  name: 'ReviewList',
  data() {
    return {
      reviews: [],
    }
  },
  components: {
    ReviewCard,
    ReviewDetail,
  },
  props: {
    selectedMovie: Object,
    isDelete: [String, Number],
  },
  methods: {
    setToken() {
      const token = localStorage.getItem("jwt")

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      }
      return config;
    },
    getReviews() {
      const config = this.setToken()

      const movieItem = {
        movie: this.selectedMovie,
      }

      axios.post(`${SERVER_URL}/community/`, movieItem, config)
      .then(response => {
        this.reviews = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },
  },
  computed: {
    ...mapState([
      'selectedReview',
    ])
  },
  watch: {
    isDelete () {
      const reviewIdx = this.reviews.findIndex( review => {
        return review.id === this.isDelete
      })
      this.reviews.splice(reviewIdx, 1)
    }
  },
  created() {
    this.getReviews()
  },
}
</script>

<style>

</style>