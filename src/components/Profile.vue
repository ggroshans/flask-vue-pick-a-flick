<template>
  <div>
    <user-movies></user-movies>
    <reset></reset>
  </div>
</template>

<script>
import UserMovies from "../components/UserMovies.vue";
import Reset from "../components/Reset.vue";
import router from "../router";
export default {
  components: { UserMovies, Reset },
  methods: {},
  created() {
    if (!this.$store.getters.getAuthStatus) {
      console.log("HHHHELLO");
      $cookies.remove("access_token_cookie");
      $cookies.remove("csrf_access_token");
      router.push("/");
    }
  },
};
</script>

<style scoped>
</style>