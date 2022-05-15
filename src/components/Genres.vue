<template>
  <div>
    <div cy-test="genre-pill-container" class="genre-pill-container">
      <b-badge
        pill
        v-for="genre in genres"
        :key="genre.id"
        variant="outline-primary"
        :class="{ selected: genre.selected }"
        class="genre-pill"
        @click="clickGenre(genre)"
        >{{ genre.name }}</b-badge
      >
    </div>
    <router-link to="/movies"
      ><b-button
        cy-test="genre-submit"
        variant="success"
        class="submit-genres-btn"
        >Confirm Genres</b-button
      ></router-link
    >
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
      if (genre.selected == false) {
        let index = this.selectedGenres.findIndex(obj => obj.id == genre.id);
        this.selectedGenres.splice(index, 1);
        this.$store.commit("setGenresQuery", this.selectedGenres);
      } else {
        let genreObj = {};
        genreObj["name"] = genre.name;
        genreObj["id"] = genre.id;
        this.selectedGenres.push(genreObj);
        this.$store.commit("setGenresQuery", this.selectedGenres);
      }
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
  background-color: rgb(2, 170, 170);
  color: white;
}

.genre-pill-container {
  display: flex;
  margin: auto;
  justify-content: center;
  align-content: center;
  align-items: center;
  flex-wrap: wrap;
  width: 350px;
}

.genre-pill {
  cursor: pointer;
  font-size: 1.25rem;
  padding: 8px 10px 5px 10px;
  margin: 8px;
  display: inline-block;
  transition: all 0.8s ease;
  letter-spacing: 0.05rem;
}

.genre-pill:hover {
  color: beige;
  box-shadow: 0 0 10px goldenrod;
  text-shadow: 0 0 5px yellow;
}

.submit-genres-btn {
  margin-top: 2rem;
  font-weight: 800;
}
</style>
