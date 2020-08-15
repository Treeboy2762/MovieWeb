<template>
  <v-form ref="form">
    <template v-for="(genre, i) in genresName">
      <v-btn rounded id="mar" v-bind:key="i" large @keyup.enter="onSubmit" @click="onSubmit(genre.name)">
        {{ genre.name }}
      </v-btn>
    </template>
    <v-text-field v-model="select" label="장르" />
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    select:"",
    genres: "",
    genresName: [
        {
            name: "Action"
        },
        {
            name: "Adventure"
        },
        {
            name: "Animation"
        },
        {
            name: "Children's"
        },
        {
            name: "Comedy"
        },
        {
            name: "Crime"
        },
        {
            name: "Documentary"
        },
        {
            name: "Drama"
        },
        {
            name: "Fantasy"
        },
        {
            name: "Film-Noir"
        },
        {
            name: "Horror"
        },
        {
            name: "Musical"
        },
        {
            name: "Mystery"
        },
        {
            name: "Romance"
        },
        {
            name: "Sci-Fi"
        },
        {
            name: "Thriller"
        },
        {
            name: "War"
        },
        {
            name: "Western"
        },
    ]
  }),
  methods: {
    onSubmit: function(item) {
      this.select = item;
      const params = {
        genres: item
      }
      this.submit(params)
    }
  }
};
</script>

<style>
#mar{
    margin: 8px;
}
</style>