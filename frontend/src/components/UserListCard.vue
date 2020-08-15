<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2" @click="watchMovies">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    {{ username}}
                  </v-list-item-title>
                  <v-list-item-title>
                    {{ gender|genderfilter }}
                  </v-list-item-title>
                  <v-list-item-title>
                    {{ age }}
                  </v-list-item-title>
                  <v-list-item-title>
                    {{ occupation }}
                  </v-list-item-title>
                  <v-list-item-contents>
                    <span  v-for="(user,i) in movies" :key="i">
                      <v-btn id="mar">
                        {{ user.movieid }}
                      </v-btn>
                    </span>
                  </v-list-item-contents>
                </v-list-item-content>
              </v-list-item>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>
import axios from 'axios'
const apiUrl = '/api'

export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    username: {
      type: String,
      default: ""
    },
    gender: {
      type: String,
      default: ""
    },
    age: {
      type: Number,
      default: 0
    },
    occupation: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      cnt : 0,
      movies: []
    }
  },
  filters:{
    genderfilter(value){
      if(value=="F"){
        return "여성";
      }else if(value=="M"){
        return "남성";
      }
    }
  },
  methods: {
    watchMovies: function() {
      console.log(this.username)
      axios.get(`${apiUrl}/ratings/?username=${this.username}`).then(response => (this.movies=response.data))
      console.log(this.movies)
    }
  }
};
</script>