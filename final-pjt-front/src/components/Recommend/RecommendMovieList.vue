<template>
  <div>
		<h3 v-if="!selectedGenre" class="mt-4" style="color:#FFFFFF">랜덤 추천영화</h3>
		<h3 v-else class="mt-4" style="color:#FFFFFF">{{ selectedGenre }}장르 추천영화</h3>
		<h3 v-if="!filteredMovies.length" class="mt-4" style="color:#FFFFFF">가 없습니다ㅜㅜ
			<br>
			<br>
			<img src="@/assets/sadness.png" style="width:250px" alt="">
		</h3>
		
		<span class="d-flex flex-row justify-content-center flex-wrap">
			<MovieCard v-for="movie in filteredMovies" :key="movie.id" :movie="movie" />
		</span>
	</div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

import MovieCard from '@/components/Movie/MovieMain/MovieCard'


const SERVER_URL = process.env.VUE_APP_URL

export default {
	name: 'RecommendMovieList',
	data () {
		return {
			movies: '',
		}
	},
	props: {
		selectedGenre: String,
		watchedmovies: Array,
	},
	components: {
		MovieCard,
	},
	computed: {
		filteredMovies () {
			if (this.selectedGenre) {
				return _.slice(_.filter(this.movies, (movie) => {					
					for (const idx in movie.genres) {
						if (!(_.includes(this.watchedmovies, movie.id)) && (movie.genres[idx].name == this.selectedGenre)) {
							return true
						}
					}
				}), 0, 4)
			} else {
				return _.sampleSize(this.movies, 1)
			}
		}
	},
	created () {
		axios.get(`${SERVER_URL}/movies/`)
		.then(response => {
			this.movies = response.data
		})
		.catch(error => {
			console.log(error)
		})
	}
}
</script>

<style>
.button {
	background-color: black;
}
.h3 {
	background-color: #D94E0C;
}
</style>