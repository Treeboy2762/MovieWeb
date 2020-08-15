<template>
  <v-form ref="form">
    <v-text-field v-model="username" label="사용자 정보" />
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
    <v-layout column>
      <v-flex v-for="card in users" :key="card.id" pa-2>
        <UserListCard
          :id="card.id"
          :username="card.username"
          :gender="card.gender"
          :age="card.age"
          :occupation="card.occupation"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-form>
</template>

<script>
import axios from 'axios'
import UserListCard from "./UserListCard"
const apiUrl = '/api'

export default {
  components: {
    UserListCard
  },
  
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array(),
    },
    username: {
      type: Number,
      default: " "
    }
  },
  data: () => ({
    cardsPerPage: 10,
    page: 1,
    users: []
  }),
  computed: {
    // pagination related variables
    movieListEmpty: function() {
      return this.movieListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.movieListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    movieListCardsSliced: function() {
      return this.movieListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  },
  methods: {
    onSubmit: function() {
      const params = {
        id: this.username,
      };
      // this.submit(params);
      console.log(this.username)
      axios.get(`${apiUrl}/user-many/?id=${this.username}`).then(response => (this.users=response.data))
      console.log(this.users)
    },
  },
};
</script>