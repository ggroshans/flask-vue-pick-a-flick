<template>
    <div>
        <h1>Movie Date</h1>
        <router-link to="" v-if="this.$store.getters.getAuthStatus">Logout</router-link>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
h1 {
  font-family: "Lobster Two", cursive;
}
</style>