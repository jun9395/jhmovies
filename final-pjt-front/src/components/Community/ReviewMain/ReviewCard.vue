<template>
  <div class="d-flex flex-column mt-3">
    <div class="d-flex justify-content-between">
      <h2 @click="selectReview" style="cursor:pointer">제목 : {{ review.title }}</h2>
      <h4>작성자 : {{ review.user.username }}</h4>
    </div>
    <div class="d-flex justify-content-between">
      <p @click="selectReview" class="text-left text-truncate w-75" style="cursor:pointer">내용 : {{ review.content }}</p>
      <p style="font-size: 0.8rem">작성일 : {{ date }}</p>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ReviewCard',
  data () {
    return {
      date: this.review.created_at.slice(0,10),
    }
  },
  props: {
    review: Object,
  },
  methods: {
    selectReview () {
      if (!this.isLogin) {
        return this.$router.push({ name: 'Login' })
      }

      this.$store.dispatch('selectReview', this.review)
    }
  },
  computed: {
    ...mapState([
      'isLogin',
    ])
  },
}
</script>

<style scoped>
div {
  color: #FFCA3D;
}
</style>