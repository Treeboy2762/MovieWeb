<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <div id="height">
      <div class="display-2 pa-10">영화 검색</div>
        <v-flex xs6>
          <v-select
            v-model="e1"
            :items="items"
            label="영화 제목"
            single-line
          />
        </v-flex>
        <div v-if="e1=='장르'">
          <GenreSearchForm :submit="searchMovies" />
        </div>
        <div v-else-if="e1=='조회수(높은순)'">
          <CountSearchForm :count=e1 :submit="searchMovies" />
        </div>
        <div v-else-if="e1=='조회수(낮은순)'">
          <CountSearchForm :count=e1 :submit="searchMovies" />
        </div>
        <div v-else-if="e1=='평점(높은순)'">
          <RatingSearchForm :sorting=e1 :submit="searchMovies" />
        </div>
        <div v-else-if="e1=='평점(낮은순)'">
          <RatingSearchForm :sorting=e1 :submit="searchMovies" />
        </div>
        <div v-else>
          <MovieSearchForm :submit="searchMovies" />
        </div>
      </div>
      <!-- 검색 결과 -->
    <MovieList id="width" :movie-list-cards="movieList" :submit="searchMovies" />

    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieSearchForm from "../MovieSearchForm";
import GenreSearchForm from "../GenreSearchForm";
import RatingSearchForm from "../RatingSearchForm";
import CountSearchForm from "../CountSearchForm";
import MovieList from "../MovieList";
export default {
  components: {
    MovieList,
    MovieSearchForm,
    GenreSearchForm,
    RatingSearchForm,
    CountSearchForm
  },
  data () {
    return {
      e1: null,
      items: [
        { text: '제목' },
        { text: '장르' },
        { text: '조회수(높은순)' },
        { text: '조회수(낮은순)' },
        { text: '평점(높은순)' },
        { text: '평점(낮은순)' },
        
      ],
      select:{
        type : Boolean,
        default: false
      }
    }
  },
  computed: {
    ...mapState({
      movieList: state => state.data.movieSearchList
    })
  },
  methods: mapActions("data", ["searchMovies"])
};
</script>

<style scoped>
#height {
  width: 80%;
}
#width {
  width: 60%;
}
</style>
