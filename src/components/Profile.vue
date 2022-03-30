<template>
    <div>
        <h3>Profile Page</h3>
        <div class="movie-grid-container">
            <div class="movie-grid-item" v-for="movie in movies">
                <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt="">
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
    width: minmax(190px, 1fr);
    overflow:hidden;
}
img {
    width: 190px;
    border-radius: 0.5rem;
}

</style>