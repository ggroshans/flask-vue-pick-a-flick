<template>
<div>
  <div v-for="book in books" :key="book.primary_isbn13">
      <img :src=book.book_image alt="">

  </div>
</div>

</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      books: null
    };
  },
  async created() {
    const resp = await fetch("http://localhost:5000/category", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ category: this.$route.params.category })
    });
    let responseData = await resp.json();
    this.books = responseData.data.results.books;
    console.log(responseData)
    console.log(this.books)
  }
};
</script>

<style scoped></style>
