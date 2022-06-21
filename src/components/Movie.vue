<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <img
          :src="'https://image.tmdb.org/t/p/w500' + getCurrentMovie.poster_path"
        />
      </div>
      <div class="col movie-details-container">
        <h2>Movie Title</h2>
        <p>{{ getCurrentMovie.title }}</p>
        <h2>Release Date</h2>
        <p>{{ getCurrentMovie.release_date }}</p>
        <h2>Overview</h2>
        <p>{{ getCurrentMovie.overview }}</p>
        <h2>Genre:</h2>
        <p>{{ genreNames(getCurrentMovie.genre_ids) }}</p>
        <h2>Popularity:</h2>
        <div class="progress-bar-container">
          <div class="progress-bar" :style="{height: 25 + 'px', width: generatePopularityBar() + 'px', color: 'green' }"></div>
        </div>
        <h2>Where can I watch?</h2>
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
    {{ getCurrentMovie }}
  </div>
</template>

<script>
import router from '../router';
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
      let percentage = ((this.getCurrentMovie.vote_average * 10) / 100) * 500;
      console.log(percentage)
      return percentage;
    }
  },
  computed: {
    getCurrentMovie() {
      console.log(this.$store.getters.getCurrentMovie);
      console.log(this.$store);
      return this.$store.getters.getCurrentMovie;
    },
  },
    created() {
    if (!this.$store.getters.getAuthStatus) {
      console.log("HHHHELLO");
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
}

.progress-bar-container {
  background-color: lightgray;
  height: 25px;
  width: 500px;
}

.progress-bar {
  background-color: green;
}

</style>
