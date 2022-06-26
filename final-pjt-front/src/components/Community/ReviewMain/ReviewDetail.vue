<template>
  <div>
    <div class=" rounded p-3">
      <h2 id="review-detail">제목 : {{ selectedReview.title }}</h2>
      <div class="text-right text-light">작성자: {{ selectedReview.user.username }}</div>
      <hr class="bg-warning">
      <h5 id="review-detail" class="ml-1 text-left">{{ selectedReview.content }}</h5>

      <br>
      
      <div class="text-right text-light">
        <span style="font-size: 0.9rem">작성시각 : {{ created }}</span> <br>
        <span style="font-size: 0.9rem">수정시각 : {{ updated }}</span>
      </div>

      <hr class="bg-warning">
    </div>

    <ReviewComment :selectedReview="selectedReview" />
  </div>
</template>

<script>
import { mapState } from 'vuex'

import ReviewComment from '@/components/Community/ReviewComment/ReviewComment'

export default {
  name: 'ReviewDetail',
  data () {
    return {
      isUpdate: false,
      created: '',
      updated: '',
    }
  },
  components: {
    ReviewComment,
  },
  methods: {
    updateReview () {
      this.isUpdate = true
    }
  },
  computed: {
    ...mapState([
      'selectedReview',
    ])
  },
  created () {
    
    if (!this.selectedReview) {
      this.$router.push({ name: 'ReviewMain' });
    }
    this.created = this.selectedReview.created_at.slice(0,10)+"/"+this.selectedReview.created_at.slice(11,19)
    this.updated = this.selectedReview.updated_at.slice(0,10)+"/"+this.selectedReview.updated_at.slice(11,19)
  }
}
</script>

<style scoped>
#review-detail {
  color: #FFCA3D;
}
</style>