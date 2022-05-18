<template>
  <div class="header-container">
    <div>
      <b-navbar type="dark" variant="dark">
        <b-navbar-nav>
          <b-nav-item href="#">
            <router-link
              to="/movies"
              v-if="
                isLoggedIn &&
                !(this.$route.name == 'Movies') &&
                !(this.$route.name == 'Genres') &&
                !(this.$route.name == 'EmptyStack')
              "
              ><b-icon icon="arrow-left"></b-icon> Back to Search
            </router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link
              to="/genres"
              v-if="isLoggedIn && !(this.$route.name == 'Genres')"
              ><b-icon icon="plus"></b-icon> New Search
            </router-link>
          </b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <div class="d-flex justify-content-center align-items-center mr-4">
            <div>
              <b-form-checkbox
                @change="darkMode"
                switch
                size="lg"
                :checked="isDarkMode"
                class="mb-1"
              ></b-form-checkbox>
            </div>
            <b-icon v-if="!isDarkMode" icon="sun" class="sun-icon"></b-icon>
            <b-icon v-if="isDarkMode" icon="moon" class="moon-icon"></b-icon>
          </div>

          <b-nav-item-dropdown
            v-if="isLoggedIn"
            text="User"
            right
            class="user-dropdown"
          >
            <b-dropdown-item href="#">
              <router-link to="/user/profile" v-if="isLoggedIn"
                ><b-icon icon="person-fill"></b-icon> Profile
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item href="#">
              <a @click="logout" v-if="isLoggedIn"
                ><b-icon icon="door-open"></b-icon> Logout</a
              >
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-navbar>
    </div>

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
          "X-CSRF-TOKEN": $cookies.get("csrf_access_token"),
        },
      });
      const responseData = await resp.json();
      $cookies.remove("csrf_access_token");
      console.log(responseData);
      this.$router.push("/login");
      this.$store.commit("setAuthStatus", false);
    },
    darkMode() {
      let body = document.getElementsByTagName("body")[0];
      if (Array.from(body.classList).includes("dark")) {
        body.classList.remove("dark");
        this.$store.commit("setDarkMode", false);
      } else {
        body.classList.add("dark");
        this.$store.commit("setDarkMode", true);
      }
    },
  },
  computed: {
    isLoggedIn() {
      console.log(this.$store.getters.getAuthStatus);
      return this.$store.getters.getAuthStatus;
    },
    isDarkMode() {
      return this.$store.getters.getDarkMode;
    },
  },
  created() {
    let body = document.getElementsByTagName("body")[0];
    let darkModeStatus = this.isDarkMode;
    if (darkModeStatus) {
      body.classList.add("dark");
    } else {
      body.classList.remove("dark");
    }
  },
};
</script>

<style scoped>
.header-container {
  opacity: 0.75;
}

h1 {
  font-family: "Lobster";
  font-size: 4.5rem;
}

.user-dropdown {
  margin-left: auto;
}

.sun-icon {
  color: orange;
}

.moon-icon {
  color: teal;
}
</style>
