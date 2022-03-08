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
      scrollable
    >
      <!-- <h1 class="text-center" style="font-family:'limelight'; font-size: 2rem;">
        {{ movieList[0].title }}
      </h1> -->
      <div class="d-flex flex-column justify-content-center align-items-center">
        <div class="modal-top-left">
          <img
            :src="'https://image.tmdb.org/t/p/w500' + movieList[0].poster_path"
            alt=""
            class="img-fluid"
            style="width:100%;"
          />
        </div>
        <div class="modal-top-right mt-5 px-4">
          <p>{{ movieList[0].overview }}</p>
        </div>
      </div>

      <h2>Where to watch:</h2>
      <a target="_blank" :href="'https://www.justwatch.com/us/search?q=' + movieList[0].title"
        >Link</a
      >
    </b-modal>
  </div>
</template>

<script>
/* eslint-disable */
import Book from "./Book.vue";
import { Vue2InteractDraggable } from "vue2-interact";
export default {
  data() {
    return {
      isVisible: true,
      movieList: [],
      matchModal: false
    };
  },
  components: {
    Book,
    Vue2InteractDraggable
  },
  methods: {
    swipedRight() {
      setTimeout(() => {
        this.matchModal = true;
        this.isVisible = false;
      }, 200);
    },
    swipedLeft() {
      setTimeout(() => {
        this.movieList.shift();
        this.isVisible = false;
        console.log(this.movieList);
      }, 200);
      setTimeout(() => {
        this.isVisible = true;
      }, 300);
    },
    onHidden() {
      this.movieList.shift();
      this.isVisible = true;
      this.matchModal = false;
    }
  },
  async mounted() {
    let loading = this.$loading.show({
      loader: "dots",
      color: "#653780",
      backgroundColor: "#fff",
      opacity: 0.5
    });
    const resp = await fetch("http://localhost:5000/movies", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ genre_id: this.$route.params.genre })
    });
    let responseData = await resp.json(responseData);
    console.log("CATEGORY LIST WHOLE", responseData);
    loading.hide();
    this.movieList = responseData.data.results;
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
</style>
