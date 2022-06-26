<template>
  <div class="d-flex flex-column">
    <p class="d-flex justify-content-between mx-auto" style="width: 35rem">
      <label for="review-title" id="reviewform">제목: </label>
      <input style="width: 500px" id="review-title" v-model.trim="title" type="text">
    </p>

    <p class="d-flex justify-content-between align-items-start mx-auto" style="width: 35rem">
      <label for="review-content" id="reviewform">내용: </label>
      <textarea id="review-content" v-model.trim="content"></textarea>
    </p>

    <span>
      <button v-if="selectedReview" @click="createReview" class="btn btn-outline-warning m-2">수정하기</button>
      <button v-else @click="createReview" class="btn btn-outline-warning m-2" >글쓰기</button>
    </span>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'


const SERVER_URL = process.env.VUE_APP_URL;

export default {
  name: 'ReviewForm',
  data() {
    return {
      title: '',
      content: '',
    };
  },
  props: {
    selectedMovie: Object,
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt');

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      }
      return config
    },
    createReview() {
      const config = this.setToken();

      const reviewItem = {
        title: this.title,
        content: this.content,
        movie: this.selectedMovie,
      }

      if (reviewItem.title && reviewItem.content) {
        if (this.selectedReview) {
          reviewItem.review = this.selectedReview

          axios.put(`${SERVER_URL}/community/update-delete/`, reviewItem, config)
          .then( () => {
            this.$emit('createReview')
          })
          .catch(error => {
            console.log(error)
          })
        }
        else {
          axios.post(`${SERVER_URL}/community/create/`, reviewItem, config)
            .then( () => {
              this.$emit('createReview')
            })
            .catch(error => {
              console.log(error)
            });
        }
      }
    },
  },
  computed: {
    ...mapState([
      'selectedReview'
    ])
  },
  created () {
    if (this.selectedReview) {
      this.title = this.selectedReview.title
      this.content = this.selectedReview.content
    }
  }
}
</script>

<style scoped>
#reviewform {
  color: #FFCA3D;
}

textarea{
	width:500px; 
	height:250px; 
  resize:none;
}
</style>