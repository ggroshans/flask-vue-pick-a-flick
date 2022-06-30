<template>
  <div>
    <section v-if="movieList[0]" class="card-container">
      <div
        class="flex justify-content-center align-items-center"
        style="z-index: 3"
      >
        <Vue2InteractDraggable
          v-if="isVisible"
          :interact-out-of-sight-x-coordinate="1000"
          :interact-max-rotation="15"
          :interact-x-threshold="200"
          :interact-y-threshold="200"
          class="rounded-borders card"
          @draggedRight="swipedRight"
          @draggedLeft="swipedLeft"
        >
        <div class="content-container">
          <div class="genre-pill-container">
            <b-badge pill variant="dark" v-for="genreObj in currentGenres" :key="genreObj.id" class="genre-pill">
              {{ genreObj.name }}
            </b-badge>
          </div>
          <div class="movie-info">
            <p>{{ movieList[0].overview }}</p>
          </div>
        </div>

        </Vue2InteractDraggable>
      </div>
    </section>

    <b-modal
      v-model="matchModal"
      @hidden="onHidden"
      header-bg-variant="dark"
      header-text-variant="light"
      body-bg-variant="light"
      body-text-variant="dark"
      footer-bg-variant="dark"
      footer-text-variant="light"
      class="p-0"
    >
      <div
        slot="modal-title"
        style="font-family: 'Lobster';"
        class="text-center mx-auto w-100"
      >
        It's a Match!
      </div>

      <div class="d-flex flex-column justify-content-center align-items-center">
        <img
          :src="'https://image.tmdb.org/t/p/w500' + movieList[0].poster_path"
          alt=""
          class="img-fluid"
          style="width:100%; max-height: 500px"
        />
      </div>
      <div slot="modal-footer">
        <b-button @click="matchModal = false" variant="danger">Close</b-button>
        <b-button @click="goToMoviePage" variant="success"
          >Go to Movie Page</b-button
        >
      </div>
    </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
import { Vue2InteractDraggable } from "vue2-interact";
import router from '../router';
import requestPath from '../fetchUtility';
export default {
  data() {
    return {
      isVisible: true,
      movieList: [],
      matchModal: false,
      swipedIds: [],
      currentGenres: this.$store.getters.getGenresQuery,
      fetchMoreMovies: true
    };
  },
  components: {
    Vue2InteractDraggable
  },
  methods: {
    swipedRight() {
      this.addSwipedId();
      this.saveMovie();
      setTimeout(() => {
        this.matchModal = true;
        this.isVisible = false;
      }, 200);
    },
    swipedLeft() {
      this.addSwipedId();
      setTimeout(() => {
        this.movieList.shift();
        this.validateMovie();
        this.isVisible = false;
        console.log(this.movieList);
      }, 200);
      setTimeout(() => {
        this.isVisible = true;
      }, 300);
    },
    onHidden() {
      this.movieList.shift();
      this.validateMovie();
      this.isVisible = true;
      this.matchModal = false;
    },
    goToMoviePage() {
      this.$store.commit("setCurrentMovieObj", this.movieList[0]);
      this.$router.push({
        name: "Movie",
        params: { title: this.movieList[0].title.split(" ").join("") }
      });
    },
    saveMovie() {
      const resp = fetch(requestPath("save_movie"), {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
        },
        body: JSON.stringify(this.movieList[0])
      });
    },
    addSwipedId() {
      let resp = fetch(requestPath("swiped"), {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
        },
        body: JSON.stringify(this.movieList[0])
      });
    },
    validateMovie() {
      try {
        while (true) {
          if (this.swipedIds.includes(this.movieList[0].id)) {
            this.movieList.shift();
          } else {
            break;
          }
        }
        while (true) {
          if (
            this.movieList[0].overview == "" ||
            !this.movieList[0].poster_path
          ) {
            this.movieList.shift();
          } else {
            break;
          }
        }
      } catch (error) {
        this.$router.push("/movies/emptystack");
      }
    }
  },
  async beforeCreate() {

    if (!this.$store.getters.getAuthStatus) {
      router.push("/");
      $cookies.remove("access_token_cookie");
      $cookies.remove("csrf_access_token");
    }


    const resp = await fetch(requestPath("genre_query"), {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
      },
      body: JSON.stringify({ genres: this.$store.getters.getGenresQuery })
    });
    let responseData0 = await resp.json();
    if (responseData0.msg != "success") {
      console.log("LOGOUT TRIGGERED", responseData0, responseData0.msg);
      $cookies.remove("access_token_cookie");
      $cookies.remove("csrf_access_token");
      this.$store.commit("setAuthStatus", false);
      this.$router.push("/login");
    }

    const resp2 = await fetch(requestPath("swiped"), {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
      }
    });
    let responseData1 = await resp2.json();
    this.swipedIds = responseData1;

    let loading = this.$loading.show({
      loader: "dots",
      color: "#653780",
      backgroundColor: "#fff",
      opacity: 0.5
    });

    const resp3 = await fetch(requestPath("movie_list"), {
      method: "POST",
      credentials: "include", //allows fetch to send cookie
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
      },
      body: JSON.stringify({ genres: this.$store.getters.getGenresQuery })
    });

    let responseData2 = await resp3.json(responseData2);
    if (responseData2.msg == "Token has expired") {
      $cookies.remove("access_token_cookie");
      $cookies.remove("csrf_access_token");
      this.$store.commit("setAuthStatus", false);
      this.$router.push("/login");
    }
    console.log("CATEGORY LIST WHOLE", responseData2);
    loading.hide();
    this.movieList = responseData2.data.results;
    this.validateMovie();
  },
  watch: {
    movieList: async function getMoreMovies() {
      if (this.movieList.length <= 10 && this.fetchMoreMovies) {
        const resp1 = await fetch(requestPath("increment_page"), {
          method: "POST",
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
            "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
          },
          body: JSON.stringify({ genres: this.$store.getters.getGenresQuery })
        });
        const resp2 = await fetch(requestPath("movie_list"), {
          method: "POST",
          credentials: "include", //allows fetch to send cookie
          headers: {
            "Content-Type": "application/json",
            "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
          },
          body: JSON.stringify({ genres: this.$store.getters.getGenresQuery })
        });

        let responseData = await resp2.json(responseData);
        if (responseData.msg == "Token has expired") {
          $cookies.remove("access_token_cookie");
          $cookies.remove("csrf_access_token");
          this.$store.commit("setAuthStatus", false);
          this.$router.push("/login");
        } else if (
          responseData.data.results.length == 0 &&
          this.movieList.length == 0
        ) {
          this.$router.push("/movies/emptystack");
        } else if (responseData.data.results.length == 0) {
          this.fetchMoreMovies = false;
        }
        console.log("CATEGORY LIST WHOLE", responseData);
        this.movieList = this.movieList.concat(responseData.data.results);
        console.log(this.movieList);
      }
    }
  }
};
</script>

<style scoped>
li {
  max-width: 600px;
  margin: auto;
}

.card-container {
  display: flex;
  justify-content: center;
  }

.rounded-borders {
  border-radius: 12px;
}



.content-container {
  position: relative;
  top: 150px;
  left: 52px;
  width: 350px;
  height: 240px;
  background-color: white;
  z-index: 0;
  touch-action: none;
}

.card {
  width: 450px;
  height: 400px;
  background-image: url("https://www.pinclipart.com/picdir/big/35-353436_clapperboard-group-clapper-clip-art-library-claqueta-de.png");
  background-repeat:no-repeat;
  background-size: 375px 400px;
  background-position: center;
  background-color: white;
  color: white;
  text-align: left;
  background-color: transparent;
  border: none;
  touch-action: none;
  z-index: 2;
}

.movie-info {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  height: 240px;
  width: 100%;
  padding: 1rem;
  color: black;
  overflow: auto;
  padding-top: 1rem;
  touch-action: none;
}

.movie-info > p {
  height: 190px;
  overflow: auto;
  touch-action: none;
}

.genre-pill-container {}

.genre-pill {
  padding-top: 6px;
  margin-top: 0.5rem;
  margin-left: .25rem;;
  background-color: gray;
  touch-action: none;
}

>>> .modal-dialog {
  max-width: 400px;
  margin-top: 5rem;
}
>>> .modal-title {
  width: 100%;
  font-size: 2.5rem;
  letter-spacing: 0.1rem;
}
>>> .modal-body {
  padding: 0px !important;
}
</style>
