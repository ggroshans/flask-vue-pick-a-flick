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
          class="rounded-borders shadow card"
          @draggedRight="swipedRight"
          @draggedLeft="swipedLeft"
        >
          <div class="movie-info">
            <p>{{ movieList[0].overview }}</p>
          </div>
        </Vue2InteractDraggable>
      </div>
    </section>

    <b-modal
      v-model="matchModal"
      @hidden="onHidden"
      size="md"
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
          style="width:100%; max-height: 600px"
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
export default {
  data() {
    return {
      isVisible: true,
      movieList: [],
      matchModal: false,
      swipedIds: []
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
        this.checkDuplicateMovie()
        this.isVisible = false;
        console.log(this.movieList);
      }, 200);
      setTimeout(() => {
        this.isVisible = true;
      }, 300);
    },
    onHidden() {
      this.movieList.shift();
      this.checkDuplicateMovie();
      this.isVisible = true;
      this.matchModal = false;
    },
    goToMoviePage() {
      this.$store.commit("setCurrentMovieObj", this.movieList[0]);
      this.$router.push({
        name: "Movie",
        params: { id: this.movieList[0].id }
      });
    },
    saveMovie() {
      const resp = fetch("http://localhost:5000/save_movie", {
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
      let resp = fetch("http://localhost:5000/swiped", {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
        },
        body: JSON.stringify(this.movieList[0])
      });
    },
    checkDuplicateMovie(){
      while (true) {
        if (this.swipedIds.includes(this.movieList[0].id)) {
          this.movieList.shift()
        } else {
          break;
        }
      }
    }
  },
  async created() {
    const resp = await fetch("http://localhost:5000/swiped", {
      method: "GET",
      credentials: 'include',
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
      },
    })
    let responseData = await resp.json()
    this.swipedIds = responseData
  },
  async mounted() {
    let loading = this.$loading.show({
      loader: "dots",
      color: "#653780",
      backgroundColor: "#fff",
      opacity: 0.5
    });
    const resp = await fetch("http://localhost:5000/movie_list", {
      method: "POST",
      credentials: "include", //allows fetch to send cookie
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
      },
      body: JSON.stringify({ genre_id: this.$route.params.genre })
    });

    let responseData = await resp.json(responseData);
    if (responseData.msg == "Token has expired") {
      $cookies.remove("access_token_cookie");
      $cookies.remove("csrf_access_token");
      this.$store.commit("setAuthStatus", false);
      this.$router.push("/login");
    }
    console.log("CATEGORY LIST WHOLE", responseData);
    loading.hide();
    this.movieList = responseData.data.results;
    this.checkDuplicateMovie()
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

  height: 100vh;
}

.rounded-borders {
  border-radius: 12px;
}

.card {
  width: 300px;
  height: 400px;
  color: white;
}

.movie-info {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  padding: 1rem;
  color: black;
}
>>> .modal-dialog {
  max-width: 400px;
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
