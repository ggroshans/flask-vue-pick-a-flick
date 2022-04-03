<template>
    <div>
        <h3>Profile Page</h3>
        <div class="movie-grid-container">
            <div class="movie-grid-item" v-for="movie in movies" :id="movie.id" @click="">
                <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt="">
                <b-icon icon="x-square-fill" class="close-icon"></b-icon> 
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                movies: null
            }
        },
        async created() {
            let resp = await fetch("http://localhost:5000/get_movies", {
                method: "GET",
                credentials: "include",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
                }
            })
            let responseData = await resp.json()
            this.movies = responseData;
        }
    }
</script>

<style scoped>
.movie-grid-container {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    justify-content: center;
    justify-items: center;
    align-items: center;
    align-content: center;
    gap: 1rem;
}
.movie-grid-item {
    position: relative;
    width: minmax(190px, 1fr);
}
img {
    width: 190px;
    border-radius: 0.5rem;
    z-index: 1;
}
.close-icon {
    position: absolute;
    right: 10px;
    top: 5px;
    font-size: 1.25rem;
    color: lightgray;
}

.close-icon:hover {
    color: tomato;
}

</style>