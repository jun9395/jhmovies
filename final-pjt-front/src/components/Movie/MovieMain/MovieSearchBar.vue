<template>
  <div>
    <input class="mt-3 mb-4" v-model="keyword" type="text" style="width:500px" placeholder="찾으실 영화의 제목을 입력하세요.">
  </div>
</template>

<script>
export default {
  name: 'MovieSearchBar',
  data () {
    return {
      keyword: '',
      options: [],
    }
  },
  watch: {
    keyword () {
      this.$emit('search', this.keyword)
    }
  },
}
</script>

<style>

</style>