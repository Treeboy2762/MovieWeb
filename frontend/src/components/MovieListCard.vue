<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2" @click="cardSelect">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    {{ title }}
                  </v-list-item-title>
                  <v-list-item-subtitle>{{ genresStr }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-card-text>
                <v-layout justify-center>
                  <v-rating
                    :value="rating"
                    color="red"
                    background-color="red"
                    half-increments
                    dense
                    readonly
                  />
                  <div class="grey--text ml-4">{{ rating.toFixed(1) }}</div>
                </v-layout>
              </v-card-text>
              <v-card-text>
                <v-layout justify-center>
                  <v-icon color="black">mdi-eye</v-icon>
                  <div class="grey--text ml-4">{{ viewCnt }}</div>
                </v-layout>
              </v-card-text>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>

export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    },
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data() {
    return {
      cnt : 0
    }
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    },
  },
  methods: {
    cardSelect: function() {
      this.cnt+=1;
      // const params = {
      //   count: this.cnt
      // };
      this.$router.push({
        name: 'movie-detail',
        params:
        {
          "movieId": this.id
        }
      })
    }
  },
};
</script>