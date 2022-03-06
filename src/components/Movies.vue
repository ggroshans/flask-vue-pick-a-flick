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
        <div class="book-info">
          <!-- <img :src="bookList[0].bookImage" alt=""> -->
          <!-- <h1 v-if="bookList.length > 0">{{ bookList[0].title }}</h1> -->
          <p>{{movieList[0].title}}</p>
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
    // async getDescription(bookList) {
    //   for (let i = 0; i < bookList.length; i++) {
    //     //if the book has an isbn available
    //     if (bookList[i].isbns[0]) {
    //       const resp = await fetch("http://localhost:5000/description", {
    //         method: "POST",
    //         headers: {
    //           "Content-Type": "application/json"
    //         },
    //         body: JSON.stringify({
    //           isbn: bookList[i].isbns[0].isbn13
    //         })
    //       });
    //       let responseData = await resp.json();
    //       console.log("GOOGLE BOOK", responseData);

    //       //if the book has the book description available

    //       console.log("fired");
    //       bookList[i]["snippet"] =
    //         responseData.data.items[0].searchInfo.textSnippet;
    //       this.bookList.push(bookList[i]);
    //       console.log("BOOKLIST", this.bookList);
    //     }
    //   }
    // },
    //   }
    // async getSummary(bookList) {
    //   for (let i = 0; i < bookList.length; i++) {
    //     //if the book has an isbn available
    //     console.log(bookList[i]);
    //     if (bookList[i].isbns[0]) {
    //       const resp = await fetch("http://localhost:5000/summary", {
    //         method: "POST",
    //         headers: {
    //           "Content-Type": "application/json"
    //         },
    //         body: JSON.stringify({
    //           isbn: bookList[i].isbns[0].isbn13
    //         })
    //       });
    //       let responseData = await resp.json();
    //       console.log("GOOGLE BOOK", responseData);
    //       //if the book has the book results available
    //       if (responseData.data.results) {
    //         console.log("fired");
    //         bookList[i]["summary"] = responseData.data.results[0].summary;
    //         this.bookList.push(bookList[i]);
    //         console.log("BOOKLIST", this.bookList);
    //       } else if (responseData.data.fault) {
    //         setTimeout(() => {}, 15000);
    //         i--;
    //         continue;
    //       }
    //     }
    //   }
    // },
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

.book-info {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  padding: 1rem;
  color: black;
}
</style>
