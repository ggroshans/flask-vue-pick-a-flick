<template>
  <div>
    <!-- <div v-if="!movieList[0]">
      <b-button variant="primary">
        <b-spinner small type="grow"></b-spinner>
        Loading...
      </b-button>
    </div> -->

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
      isLoading: true,
    };
  },
  components: {
    Book,
    Vue2InteractDraggable
  },
  methods: {
    swipedRight() {
      setTimeout(() => {
        this.movieList.shift();
        this.isVisible = false;
        console.log(this.movieList);
      }, 200);
      setTimeout(() => {
        this.isVisible = true;
      }, 300);
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
  },
  created() {

  },
  async mounted() {
      const resp = await fetch("http://localhost:5000/movies", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ genre_id: this.$route.params.genre })
      });
      let responseData = await resp.json(responseData);
      console.log("CATEGORY LIST WHOLE", responseData);
      this.isLoading = false;
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
