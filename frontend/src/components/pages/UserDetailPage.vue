<template>
 <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs6>
        <h1>{{movieList[0].title}}</h1>
      </v-flex>
      <v-flex>
        <div> 영화 번호 :{{movieId}}</div>
        <h2>장르 : {{ movieList[0].genres.join('/') }}</h2>
        <div>조회수: {{ movieList[0].viewCnt }}</div>
        <div>평점: {{ movieList[0].rating }}</div>
      </v-flex>

    </v-layout>
    <v-layout justify-center wrap>
      <div  v-for="(user,i) in users" :key="i">
        <v-btn id="mar">
          {{ user.username }}
        </v-btn>
      </div>
    </v-layout>
  </v-container>
</template>
<script>
import { mapState, mapActions } from "vuex";
import axios from 'axios'
const apiUrl = '/api'

export default {
  components: {
  },
  props: {
    type: Number,
    movieId: 0
  },
  computed: {
   ...mapState({
    movieList: state => state.data.movieSearchList
    })
  },
  data() {
    return{
      users: []
    }
  },
  methods: mapActions("data", ["searchMovies"]),
  mounted() {
    const params = {
      id: this.movieId
    };
    const params1 = {
      movieid: this.movieId
    };
    this.searchMovies(params)
    axios.get(`${apiUrl}/ratings/?movieid=${this.movieId}`).then(response => (this.users=response.data))
    console.log(this.users)
  }
};
</script>