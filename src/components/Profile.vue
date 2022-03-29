<template>
    <div>
        <h3>Profile Page</h3>
        <ul>
            <li v-for="movie in movies">{{movie}}
                <hr>
            </li>
        </ul>
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

</style>