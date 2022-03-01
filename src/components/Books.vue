<template>
  <div>
    <!-- <router-link v-for="book in bookList" :key="book" :to="{name: 'Book', params: {book: book.list_name_encoded}}">{{category.display_name}}</router-link> -->

    <!-- <ul v-for="book in bookList" :key="book.primary_isbn10"><li>{{book}}</li></ul> -->
    <vue-swing
      :config="config"
      @throwout = swiped()
      class="swipe"
      ><li v-if="bookList.length > 0" v-html="bookList[0].snippet"></li
    ></vue-swing>

  </div>
</template>

<script>
/* eslint-disable */
import Category from "./Book.vue";
import VueSwing from "vue-swing";
export default {
  data() {
    return {
      bookList: [],
      config: {
        allowedDirections: [VueSwing.Direction.LEFT, VueSwing.Direction.RIGHT],
        minThrowDistance: 250,
        maxThrowDistance: 300
      }
    };
  },
  components: {
    Category,
    VueSwing
  },
  methods: {
    swiped(book) {
        this.bookList.shift()
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
            console.log("fired")
            bookList[i]["snippet"] =
              responseData.data.items[0].searchInfo.textSnippet;
            this.bookList.push(bookList[i]);
            console.log("BOOKLIST", this.boo)
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
      this.getDescription(responseData.data.results);

    },
  },
  async created() {
    this.getBookList();

  }
};
</script>

<style scoped>
li {
    min-width: 600px;
    margin: auto;
}
.swipe {
  position: absolute;
}
</style>
