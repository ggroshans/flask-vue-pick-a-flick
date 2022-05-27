<template>
  <div class="container">
    <div class="row justify-content-center">
      <router-link to="/login">
        <button cy-test="splash-login-btn" class="btn btn-info">Login</button>
      </router-link>
    </div>
    <div class="row mt-3 justify-content-center">
      <router-link to="/register">
        <button cy-test="splash-register-btn" class="btn btn-info">Register</button>
      </router-link>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
export default {
  beforeCreate() {
    if (this.$store.getters.getAuthStatus) {
      this.$router.push("/genres");
    }
  }
};
</script>

<style scoped>
h1 {
  font-family: "Lobster Two", cursive;
}
</style>
