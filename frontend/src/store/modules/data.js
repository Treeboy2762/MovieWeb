import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  movieDetailUser: []
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: parseInt(d.count),
      rating: parseFloat(d.likes),
    }))

    commit('setMovieSearchList', movies)
  },

  async searchMoviesDetailUser({ commit }, params) {
    const resp = await api.searchMoviesDetailUser(params)
    const movies = resp.data.map(d => ({
      username: d.username,
      movieid: d.movieid,
      rate: d.rate,
      time: d.time
    }))

    commit('setMovieDetailUserList', moviesDetailUsers)
  },
 }

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  setMovieDetailUserList(state, moviesDetailUsers){
    state.movieDetailUser = moviesDetailUsers.map(m=>m)
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}