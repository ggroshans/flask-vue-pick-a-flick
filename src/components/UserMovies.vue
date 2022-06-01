<template>
  <div>
    <h3>Movies</h3>
    <div class="movie-grid-container">
      <user-movie
        class="movie-grid-item"
        v-for="movie in movies"
        :id="movie.id"
        :movie="movie"
        :key="movie.id"
        @deletedMovieObj="movieObj = $event"
      >
      </user-movie>
    </div>
    <b-modal
      id="delete-modal"
      title="BootstrapVue"
      header-bg-variant="danger"
      header-text-variant="light"
      size="sm"
    >
      <div class="delete-modal-title" slot="modal-title">
        <strong>Delete Confirmation</strong>
      </div>
      <p v-if="movieObj" class="my-4">
        Are you sure you want to delete <br />"<strong>{{
          movieObj.original_title
        }}</strong
        >"?
      </p>
      <div slot="modal-footer">
        <b-button @click="closeModal" button-size="sm">Cancel</b-button>
        <b-button
          @click="deleteMovie(movieObj.id)"
          class="btn btn-danger"
          button-size="sm"
          >Delete</b-button
        >
      </div>
    </b-modal>
  </div>
</template>

<script>
import UserMovie from "./UserMovie.vue";
import requestPath from '../fetchUtility';
export default {
  data() {
    return {
      movieObj: null
    };
  },
  components: {
    UserMovie
  },
  methods: {
    async deleteMovie(selectedMovieId) {
      let index = this.movies.findIndex(movie => {
        return movie.id == selectedMovieId;
      });
      this.movies.splice(index, 1);
      this.$root.$emit("bv::hide::modal", "delete-modal");

      let resp = await fetch(requestPath("delete_movie"), {
        method: "DELETE",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
        },
        body: JSON.stringify(selectedMovieId)
      });
      let responseData = await resp.json();
      console.log("DELETE RESPONSE DATA", responseData);
    },
    closeModal() {
      this.$root.$emit("bv::hide::modal", "delete-modal");
    }
  },
  computed: {
    movies () {
      return this.$store.getters.getUserMovieList;
    } 
  },
  async created() {
    let resp = await fetch(requestPath("user_movie_list"), {
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
    this.$store.commit("setUserMovieList", responseData);
    this.movies = this.$store.getters.getUserMovieList;
    // this.movies = responseData;
  }
};
</script>

<style scoped>
.movie-grid-container {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;
  gap: 1.5rem;
  max-width: 1100px;
  margin: auto;
}
.movie-grid-item {
  cursor: pointer;
  position: relative;
  width: minmax(190px, 1fr);
  border: 1px solid beige;
  border-radius: 9px;
}

.modal-body p {
  color: black;
}
</style>
