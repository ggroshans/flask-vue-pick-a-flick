<template>
  <div>
    <router-link
      to="/movies"
      v-if="
        isLoggedIn &&
          !(this.$route.name == 'Movies') &&
          !(this.$route.name == 'Genres') &&
          !(this.$route.name == 'EmptyStack')
      "
      ><b-button
        ><b-icon icon="arrow-left"></b-icon> Back to Current Search</b-button
      >
    </router-link>
    <router-link
      to="/genres"
      v-if="isLoggedIn && !(this.$route.name == 'Genres')"
      ><b-button><b-icon icon="plus"></b-icon> New Search</b-button>
    </router-link>
    <router-link to="/user/profile" v-if="isLoggedIn"
      ><b-button><b-icon icon="person-fill"></b-icon> Profile</b-button>
    </router-link>

    <b-button @click="logout" v-if="isLoggedIn"
      ><b-icon icon="door-open"></b-icon> Logout</b-button
    >

  <b-form-checkbox  @change="darkMode" switch size="lg" variant="danger">Dark Mode</b-form-checkbox>
    <h1>Movie Date</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {};
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
      });
      const responseData = await resp.json();
      $cookies.remove("csrf_access_token");
      console.log(responseData);
      this.$router.push("/login");
      this.$store.commit("setAuthStatus", false);
    },
    darkMode() {
      let bodyClassList = document.getElementsByTagName("body")[0].classList;
      if (Array.from(bodyClassList).includes("dark")) {
        bodyClassList.remove("dark");
      } else {
        bodyClassList.add("dark");
      }
    }
  },
  computed: {
    isLoggedIn() {
      console.log(this.$store.getters.getAuthStatus);
      return this.$store.getters.getAuthStatus;
    }
  }
};
</script>

<style scoped>
h1 {
  font-family: "Lobster Two", cursive;
  font-size: 4.5rem;
}
</style>
