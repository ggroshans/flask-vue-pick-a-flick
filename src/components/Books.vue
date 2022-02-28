<template>
    <div>
        <!-- <router-link v-for="book in bookList" :key="book" :to="{name: 'Book', params: {book: book.list_name_encoded}}">{{category.display_name}}</router-link> -->

        <!-- <ul v-for="book in bookList" :key="book.primary_isbn10"><li>{{book}}</li></ul> -->
        <vue-swing
            v-for="book in bookList" :key="book.primary_isbn10" :config="config"><li>{{book}}</li></vue-swing>
    </div>
</template>

<script>
/* eslint-disable */
    import Category from './Book.vue';
    import VueSwing from 'vue-swing';
    export default {
        data() {
            return {
                bookList: null,
                config: {
                    allowedDirections:  [VueSwing.Direction.LEFT, VueSwing.Direction.RIGHT],
                    minThrowDistance: 250,
                    maxThrowDistance: 300
                },
            }
        },
        components: {
            Category,
            VueSwing,
        },
        async created() {
            const resp = await fetch("http://localhost:5000/books", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            let responseData = await resp.json(responseData)
            console.log("CATEGORY LIST WHOLE", responseData)
            this.bookList = responseData.data.results
        }
    }
</script>

<style scoped>

</style>