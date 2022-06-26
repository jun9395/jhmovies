<template>
  <div id="card" class="card m-4 " style="width: 22rem; height: 35rem">
    <router-link to="/movie-detail">
      <img @click="movieDetail" :src="movie.poster_path" class="card-img-top p-2" alt="..." style="height:430px">
    </router-link>
    <div class="card-body p-2 px-3">
      <h5 class="card-title text-truncate"><i class="fas fa-film"></i> {{ movie.title }}</h5>

      <hr class="my-2">
      
      <p v-if="movie.overview" class="card-text text-truncate">{{ movie.overview }}</p>
      <p v-else class="card-text">작성된 줄거리가 없습니다.</p>
      <div class="d-flex flex-row justify-content-center">
        <div class="mx-2"><i class="far fa-comments"></i> 댓글 : {{ count_comment }}개</div>
        <div>|</div>
        <div class="mx-2"><i class="fas fa-clipboard-list"></i> 리뷰 : {{ count_review }}개</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'moviecard',
  props:{
    movie: Object,
  },
  methods: {
    movieDetail () {
      this.$store.dispatch('selectMovie', this.movie)
    }
  },
  computed: {
    count_comment () {
      return this.movie.moviecomments.length
    },
    count_review () {
      return this.movie.moviereviews.length
    }
  }
}
</script>

<style>
#card {
    background-color:#FFCA3D;
}
</style>