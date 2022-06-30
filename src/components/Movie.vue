<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <img
          class="movie-cover"
          :src="'https://image.tmdb.org/t/p/w500' + getCurrentMovie.poster_path"
        />
      </div>
      <div class="col movie-details-container">
        <div class="row">
          <div class="col">
            <h2 class="movie-detail-heading">Movie Title</h2>
            <p>{{ getCurrentMovie.title }}</p>
          </div>
          <div class="col">
            <h2 class="movie-detail-heading">Release Date</h2>
            <p>{{ getCurrentMovie.release_date }}</p>
          </div>
        </div>

        <h2 class="movie-detail-heading text-center">Overview</h2>
        <p>{{ getCurrentMovie.overview }}</p>

        <div class="row">
          <div class="col">
            <h2 class="movie-detail-heading">Genre:</h2>
            <p>{{ genreNames(getCurrentMovie.genre_ids) }}</p>
          </div>
          <div class="col">
            <h2 class="movie-detail-heading">Popularity:</h2>
            <div class="progress-bar-container">
              <div
                class="progress-bar"
                :style="{
                  height: 25 + 'px',
                  width: generatePopularityBar() + 'px',
                  color: 'green',
                }"
              ></div>
            </div>
          </div>
        </div>

        <h2 class="movie-detail-heading">Where can I watch?</h2>
        <p>
          <a
            :href="
              'https://www.justwatch.com/us/search?q=' + getCurrentMovie.title
            "
            >Streaming availability</a
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import router from "../router";
export default {
  data() {
    return {
      genres: [
        {
          id: 28,
          name: "Action",
        },
        {
          id: 12,
          name: "Adventure",
        },
        {
          id: 16,
          name: "Animation",
        },
        {
          id: 35,
          name: "Comedy",
        },
        {
          id: 80,
          name: "Crime",
        },
        {
          id: 99,
          name: "Documentary",
        },
        {
          id: 18,
          name: "Drama",
        },
        {
          id: 10751,
          name: "Family",
        },
        {
          id: 14,
          name: "Fantasy",
        },
        {
          id: 36,
          name: "History",
        },
        {
          id: 27,
          name: "Horror",
        },
        {
          id: 10402,
          name: "Music",
        },
        {
          id: 9648,
          name: "Mystery",
        },
        {
          id: 10749,
          name: "Romance",
        },
        {
          id: 878,
          name: "Science Fiction",
        },
        {
          id: 10770,
          name: "TV Movie",
        },
        {
          id: 53,
          name: "Thriller",
        },
        {
          id: 10752,
          name: "War",
        },
        {
          id: 37,
          name: "Western",
        },
      ],
    };
  },
  methods: {
    genreNames(genreIdArray) {
      let genreNames = [];
      genreIdArray.forEach((genreId) => {
        let index = this.genres.findIndex((obj) => obj.id == genreId);
        genreNames.push(this.genres[index].name);
      });
      return genreNames.join(", ");
    },
    generatePopularityBar() {
      let percentage = ((this.getCurrentMovie.vote_average * 10) / 100) * 200;
      return percentage;
    },
  },
  computed: {
    getCurrentMovie() {
      return this.$store.getters.getCurrentMovie;
    },
  },
  created() {
    if (!this.$store.getters.getAuthStatus) {
      $cookies.remove("access_token_cookie");
      $cookies.remove("csrf_access_token");
      router.push("/");
    }
  },
};
</script>

<style scoped>
.movie-details-container {
  text-align: left;
  background-color: rgba(255, 255, 255, 0.45);
  color: black;
  padding: 2rem;
  border-radius: 20px;
  margin: 2rem auto;
  max-width: 395px;
  position: fixed;
  top: 20%;
  transform: translateY(-20%);
  left: 50%;
  transform: translateX(-50%);
  height: 595px;
  z-index: 1;
}

.movie-details-container:hover {
  z-index: 3;
}

.movie-detail-heading {
  font-size: 1.5rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.progress-bar-container {
  background-color: lightgray;
  height: 25px;
  width: 200px;
}

.progress-bar {
  background-color: green;
}

.movie-cover {
  border-radius: 20px;
  max-width: 400px;
  margin: 2rem auto;
  height: 595px;
  position: fixed;
  top: 20%;
  transform: translateY(-20%);
  left: 50%;
  transform: translateX(-50%);
  z-index: 2;
  transition: 1s ease all;
}

.movie-cover:hover {
  opacity: 0;
}
</style>
