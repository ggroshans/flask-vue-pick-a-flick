<template>
  <div>
    <div v-for="genre in genres" :key="genre.id">
      <!-- <router-link :to="{name: 'Movies', params: {genre: genre.id}}">{{genre.name}}</router-link> -->
      <b-button
        variant="secondary"
        :class="{ selected: genre.selected }"
        @click="clickGenre(genre)"
        >{{ genre.name }}</b-button
      >
    </div>
    <router-link to="/movies"><b-button variant="success">Submit</b-button></router-link> 
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      genres: [
        {
          id: 28,
          name: "Action",
          selected: false
        },
        {
          id: 12,
          name: "Adventure",
          selected: false
        },
        {
          id: 16,
          name: "Animation",
          selected: false
        },
        {
          id: 35,
          name: "Comedy",
          selected: false
        },
        {
          id: 80,
          name: "Crime",
          selected: false
        },
        {
          id: 99,
          name: "Documentary",
          selected: false
        },
        {
          id: 18,
          name: "Drama",
          selected: false
        },
        {
          id: 10751,
          name: "Family",
          selected: false
        },
        {
          id: 14,
          name: "Fantasy",
          selected: false
        },
        {
          id: 36,
          name: "History",
          selected: false
        },
        {
          id: 27,
          name: "Horror",
          selected: false
        },
        {
          id: 10402,
          name: "Music",
          selected: false
        },
        {
          id: 9648,
          name: "Mystery",
          selected: false
        },
        {
          id: 10749,
          name: "Romance",
          selected: false
        },
        {
          id: 878,
          name: "Science Fiction",
          selected: false
        },
        {
          id: 10770,
          name: "TV Movie",
          selected: false
        },
        {
          id: 53,
          name: "Thriller",
          selected: false
        },
        {
          id: 10752,
          name: "War",
          selected: false
        },
        {
          id: 37,
          name: "Western",
          selected: false
        }
      ],
      selectedGenres: []
    };
  },
  methods: {
    clickGenre(genre) {
      genre.selected = !genre.selected;
      if (this.selectedGenres.includes(genre.id)) {
        let index = this.selectedGenres.findIndex(number => number == genre.id);
        this.selectedGenres.splice(index, 1);
        this.$store.commit("setGenresQuery", this.selectedGenres)
      } else {
        this.selectedGenres.push(genre.id);
        this.$store.commit("setGenresQuery", this.selectedGenres)
      }
      console.log(this.selectedGenres);
    }
  },
  created() {
    let token = this.$store.getters.getToken;
    let auth = this.$store.getters.getAuthStatus;
    console.log("TEST --", token);
    console.log("AUTH STATUS", auth);

    if (!auth) {
      this.$router.push("/");
    }
  }
};
</script>

<style scoped>
.selected {
  background-color: #007bff;
  color: white;
}
</style>
