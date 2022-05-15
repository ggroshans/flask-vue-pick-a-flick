<template>
  <div>
    <div>
      <img
        @click="goToMoviePage()"
        :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path"
        alt=""
      />
    </div>
    <b-icon
      icon="x-square-fill"
      class="close-icon"
      @click="getDeletedMovieObj()"
    ></b-icon>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {
    movie: Object
  },
  methods: {
    getDeletedMovieObj() {
      this.$emit("deletedMovieObj", this.movie);
      this.$root.$emit("bv::show::modal", "delete-modal");
    },
    goToMoviePage() {
      this.$store.commit("setCurrentMovieObj", this.movie);
      this.$router.push({
        name: "Movie",
        params: { title: this.movie.title.split(" ").join("") }
      });
    }
  }
};
</script>

<style scoped>
img {
  width: 190px;
  border-radius: 0.5rem;
  z-index: 1;
}

.close-icon {
  position: absolute;
  right: 10px;
  top: 5px;
  font-size: 1.35rem;
  color: lightgray;
  background-color: tomato;
  opacity: 0.65;
  transition: all .5s ease;
  border: 1px solid gray;
  border-radius: 4px;
}

.close-icon:hover {
  color: tomato;
  border: 1px solid white;
  opacity: 1;
  background-color: white;
}
</style>
