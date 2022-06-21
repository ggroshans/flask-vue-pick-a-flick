<template>
  <div id="app" :class="{ filter: darkMode }">
    <Header></Header>
    <h1></h1>
    <router-view />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
export default {
  name: "App",
  components: {
    Header,
  },
  computed: {
    darkMode() {
      return this.$store.getters.getDarkMode;
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Limelight&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Lobster&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import "./styles/loading.css";
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.filter {
  min-height: 100vh;
  background-color: rgba(0, 0, 0, 0.45);
  background-size: cover;
  background-attachment: fixed;
  background-repeat: no-repeat;
  z-index: 2 !important;
}
</style>