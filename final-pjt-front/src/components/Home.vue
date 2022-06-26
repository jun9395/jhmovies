<template>
  <div class="home">
    <MovieSearchBar @search="search" :movies="movies"/>
    <MovieList :keyword="keyword" @getMovies="getMovies"/>
  </div>
</template>

<script>
import MovieSearchBar from '@/components/Movie/MovieMain/MovieSearchBar'
import MovieList from '@/components/Movie/MovieMain/MovieList'

export default {
  name: 'Home',
  data () {
    return {
      keyword: '',
      movies: '',
    }
  },
  components: {
    MovieSearchBar,
    MovieList,
  },
  methods: {
    search (keyword) {
      this.keyword = keyword
    },
    getMovies (movies) {
      this.movies = movies
    }
  }
}
</script>
