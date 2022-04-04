<template>
  <div>
    <h3>Profile Page</h3>
    <div class="movie-grid-container">
      <user-movie
        class="movie-grid-item"
        v-for="movie in movies"
        :id="movie.id"
        :movie="movie"
        :key="movie.id"
        :deleteMovie="deleteMovie"
      >
      
      </user-movie>
    </div>
    <b-modal id="modal-1" title="BootstrapVue" header-bg-variant="danger"
    header-text-variant="light">
      <div class="delete-modal-title" slot="modal-title">Delete Confirmation</div>
      <p class="my-4">Are you sure you want to delete</p>
    </b-modal>
  </div>
</template>

<script>
import UserMovie from './UserMovie.vue';
export default {
  data() {
    return {
      movies: null
    };
  },
  components: {
    UserMovie,
  },
  methods: {
    deleteMovie(selectedMovieId) {
    this.$root.$emit('bv::show::modal', 'modal-1')
    console.log(movieId)

    console.log(this.movies)
    let index = this.movies.findIndex(movie => {
      movie.id == selectedMovieId
    })

    console.log(index);
    },
  },
  async created() {
    let resp = await fetch("http://localhost:5000/get_movies", {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
      }
    });
    let responseData = await resp.json();
    if (responseData.msg == "Token has expired") {
      $cookies.remove("access_token_cookie");
      $cookies.remove("csrf_access_token");
      this.$store.commit("setAuthStatus", false);
      this.$router.push("/login");
    }
    this.movies = responseData;
  }
};
</script>

<style scoped>
.movie-grid-container {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;
  gap: 1rem;
}
.movie-grid-item {
  position: relative;
  width: minmax(190px, 1fr);
}


</style>
