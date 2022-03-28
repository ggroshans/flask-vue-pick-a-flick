<template>
  <div>
    <h1>Movie Date</h1>
    <button @click="logout" v-if="isLoggedIn">Logout</button>
  </div>
</template>

<script>
export default {
   data() {
       return {

       }
   },
   methods: {
       async logout() {
           const resp = await fetch("http://localhost:5000/logout", {
               method: "POST",
               credentials: "include",
               headers: {
                   "Content-Type": "application/json",
                   "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
               }
           })
           const responseData = await resp.json()
           $cookies.remove("csrf_access_token")
           console.log(responseData)
           this.$router.push("/login")
           this.$store.commit("setAuthStatus", false)
       }
   },
  computed: {
        isLoggedIn() {
            console.log(this.$store.getters.getAuthStatus)
            return this.$store.getters.getAuthStatus;
    }
}
}
</script>

<style scoped>
h1 {
  font-family: "Lobster Two", cursive;
}
</style>
