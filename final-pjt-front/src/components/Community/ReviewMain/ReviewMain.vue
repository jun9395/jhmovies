<template>
  <div>
    <span class="container row mx-auto" v-if="switchReviewCreate">
      <span class="col-7 ml-5">
        <ReviewList :selectedMovie="selectedMovie" :isDelete="isDelete" />
      </span>
      <div class="col-3">
        <button class="my-2 btn btn-outline-warning" style="width:75px" @click="selectReviewCreate">새 글</button>
        <div v-if="selectedReview && selectedReview.user.username == myName">
          <button class="my-2 btn btn-outline-warning" style="width:75px" @click="selectReviewUpdate">수정</button> <br>
          <button class="my-2 btn btn-outline-warning" style="width:75px" @click="selectReviewDelete">삭제</button>
        </div>
      </div>
    </span>
    <span v-else>
      <ReviewForm :selectedMovie="selectedMovie" @createReview="selectReviewCreate"/>
    </span>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

import ReviewList from './ReviewList'
import ReviewForm from './ReviewForm'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'ReviewMain',
  data () {
    return {
      switchReviewCreate: true,
      isDelete: '',
      myName: localStorage.getItem('myName'),
    }
  },
  components: {
    ReviewList,
    ReviewForm,
  },
  props: {
    selectedMovie: [String, Object],
    selectReview: Boolean,
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
    selectReviewCreate () {
      if (!this.isLogin) {
        return this.$router.push({ name: 'Login' })
      }

      this.switchReviewCreate = !this.switchReviewCreate
      this.$store.dispatch('selectReview', '')
    },
    selectReviewUpdate () {
      this.switchReviewCreate = !this.switchReviewCreate
    },
    selectReviewDelete () {
      const config = this.setToken()

      const reviewItem = {
        movie: this.selectedMovie,
        review: this.selectedReview
      }

      if (this.selectedReview) {
        axios.post(`${SERVER_URL}/community/update-delete/`, reviewItem, config)
        .then( () => {
          this.$store.dispatch('selectReview', '')
          this.$emit('deleteReview')
          this.isDelete = reviewItem.review.id
        })
        .catch( error => {
          console.log(error)
        })
      }
    }
  },
  computed: {
    ...mapState([
      'selectedReview',
      'isLogin',
    ])
  },
  watch: {
    selectReview () {
      this.switchReviewCreate = true
    }
  },
}
</script>

<style>

</style>