<template>
  <!-- <div class="card-container">
    <div
      ><li v-if="bookList.length > 0" v-html="bookList[0].title"></li
    ></div>




  </div> -->

  <section class="card-container">
    <div class="fixed-center">
      <Vue2InteractDraggable
        :interact-out-of-sight-x-coordinate="1000"
        :interact-max-rotation="15"
        :interact-x-threshold="200"
        :interact-y-threshold="200"
        class="rounded-borders shadow-10 card"
      >
        <div class="card__main" v-if="bookList.length > 0" v-html="bookList[0].title"></div>
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
      bookList: []
    };
  },
  components: {
    Book,
    Vue2InteractDraggable
  },
  methods: {
    swiped(book) {
      this.bookList.shift();
    },
    async getDescription(bookList) {
      for (let i = 0; i < bookList.length; i++) {
        //if the book has an isbn available
        if (bookList[i].isbns[0]) {
          const resp = await fetch("http://localhost:5000/description", {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              isbn: bookList[i].isbns[0].isbn13
            })
          });
          let responseData = await resp.json();
          console.log("GOOGLE BOOK", responseData);

          //if the book has the book description available
          if (
            responseData.data.items &&
            responseData.data.items[0].searchInfo.textSnippet
          ) {
            console.log("fired");
            bookList[i]["snippet"] =
              responseData.data.items[0].searchInfo.textSnippet;
            this.bookList.push(bookList[i]);
            console.log("BOOKLIST", this.bookList);
          }
        }
      }
      //if the bookList is under 100 in queue then grab more
      //   if (this.bookList.length < 100) {
      //     this.getBookList();
      //   }
    },
    async getBookList() {
      const resp = await fetch("http://localhost:5000/books", {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      });
      let responseData = await resp.json(responseData);
      console.log("CATEGORY LIST WHOLE", responseData);
      // this.getDescription(responseData.data.results);
      this.bookList = responseData.data.results; // remove this after bringing back Google api
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
</style>
