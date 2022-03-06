<template>
  <section class="card-container">
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
          <p>{{movieList[0].overview}}</p>
        </div>
      </Vue2InteractDraggable>
    </div>
  </section>
</template>

<script>
/* eslint-disable */
import Book from "./Book.vue";
import { Vue2InteractDraggable } from "vue2-interact";
export default {
  data() {
    return {
      isVisible: true,
      movieList: []
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
    async getBookList() {
      const resp = await fetch("http://localhost:5000/movies", {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      });
      let responseData = await resp.json(responseData);
      console.log("CATEGORY LIST WHOLE", responseData);
      this.movieList = responseData.data.results;
      // this.getSummary(responseData.data.results);
    }
  },
  async created() {
    this.getBookList();
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
