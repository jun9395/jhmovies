<template>
  <div>
    <div class="d-flex justify-content-center flex-wrap">
			<button
				class="btn btn-outline-warning m-2" 
				:class="{ active:genre.name == selectedGenre }" 
				v-for="genre in genres1" 
				:key="genre.id+1000" 
				@click="selectgenre">{{ genre.name }}
			</button>
		</div>
		<div class="d-flex justify-content-center flex-wrap">
			<button
				class="btn btn-outline-warning m-2" 
				:class="{ active:genre.name == selectedGenre }" 
				v-for="genre in genres2" 
				:key="genre.id+1000" 
				@click="selectgenre">{{ genre.name }}
			</button>
		</div>

    <RecommendMovieList :selectedGenre="selectedGenre" :watchedmovies="watchedmovies" />
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

import RecommendMovieList from './RecommendMovieList'


const SERVER_URL = process.env.VUE_APP_URL

export default {
  name: 'Recommend',
  data () {
		return {
			genres1: '',
			genres2: '',
			selectedGenre: '',
		}
	},
  components: {
    RecommendMovieList,
  },
  methods: {
		selectgenre () {
			this.selectedGenre = event.target.innerText
		},
		setToken() {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      }
      return config
    },
  },
  created () {
		const config = this.setToken()
		
		axios.get(`${SERVER_URL}/movies/recommend`, config)
		.then(response => {
			this.genres1 = _.slice(response.data['genres'], 0, 10)
			this.genres2 = _.slice(response.data['genres'], 10, 20)
			this.watchedmovies = response.data['watchedmovies']
		})
		.catch(error => {
			console.log(error)
		})
	}
}
</script>

<style>

</style>