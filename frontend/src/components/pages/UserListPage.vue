<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <div id="width">
      <div class="display-2 pa-10">사용자 정보</div>
      </div>
        <UserSearchForm id="width" :user-list-cards="userList"/>
    <!-- <UserList id="width" :movie-list-cards="movieList" :submit="searchMovies" /> -->
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserSearchForm from "../UserSearchForm";
export default {
  components: {
    UserSearchForm
  },
  data () {
    return {}
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
