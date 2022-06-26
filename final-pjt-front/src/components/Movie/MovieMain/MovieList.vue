<template>
  <div class="d-flex justify-content-center flex-wrap">
		<MovieCard v-for="movie in filteredMovies" :key="movie.id" :movie="movie" />
	</div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

import MovieCard from './MovieCard'


const SERVER_URL = process.env.VUE_APP_URL

export default {
	name: 'MovieList',
	data () {
		return {
			movies: '',
		}
	},
	components: {
		MovieCard,
	},
	props: {
		keyword: String,
	},
	computed: {
		filteredMovies () {
			if (this.keyword) {
				return _.filter(this.movies, (movie) => {
					return _.includes(movie.title, this.keyword)
				})
			} else {
				return _.sampleSize(this.movies, 12)
			}
		}
	},
	created () {
		axios.get(`${SERVER_URL}/movies/`)
		.then(response => {
			this.movies = response.data
			this.$emit('getMovies', this.movies)
		})
		.catch(error => {
			console.log(error)
		})
	}
}
</script>

<style>

</style>