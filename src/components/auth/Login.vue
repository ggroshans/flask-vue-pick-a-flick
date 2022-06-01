<template>
  <div class="container mt-5">
    <h1>Login</h1>
    <form>
      <div class="input-group form-group mb-0">
        <div class="input-group-prepend">
          <span class="input-group-text"
            ><b-icon icon="person-fill"></b-icon
          ></span>
        </div>
        <input
          cy-test="login-username"
          type="text"
          class="form-control"
          placeholder="username"
          v-model="username"
        />
      </div>
      <div v-if="usernameError" class="username-error text-left">
        {{ usernameError }}
      </div>
      <div class="input-group form-group mt-3">
        <div class="input-group-prepend">
          <span class="input-group-text"
            ><b-icon icon="key-fill"></b-icon
          ></span>
        </div>
        <input
          cy-test="login-password"
          type="password"
          class="form-control"
          placeholder="password"
          v-model="password"
        />
      </div>
      <div v-if="passwordError" class="password-error text-left">
        {{ passwordError }}
      </div>
      <!-- <div class="row align-items-center remember">
        <input type="checkbox" />Remember Me
      </div> -->
      <div class="form-group">
        <button
          cy-test="login-submit"
          @click.prevent="submitLogin"
          value="Login"
          class="btn btn-primary float-right"
        >
          Submit
        </button>
      </div>
    </form>
    <div>
      <p>
        Don't have any account?
        <router-link to="/register">Register Here</router-link>
      </p>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import router from '../../router'
import requestPath from '../../fetchUtility';
export default {
  data() {
    return {
      username: null,
      password: null,
      usernameError: null,
      passwordError: null
    };
  },
  methods: {
    async submitLogin() {
      console.log("fired");
      const resp = await fetch(requestPath('login'), {
        method: "POST",
        credentials: 'include', //allows fetch to send cookie
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password
        })
      });
      let responseData = await resp.json();
      this.handleResponse(responseData);
    },
    handleResponse(responseData) {
      if (responseData["error"]) {
        if (responseData["error"]["username"]) {
          this.passwordError = "";
          this.usernameError = responseData["error"]["username"];
        } else if (responseData["error"]["password"]) {
          this.usernameError = ""
          this.passwordError = responseData["error"]["password"];
        }
      } else {
        console.log('response', responseData)
        // sessionStorage.setItem("access_token", responseData.access_token)
        // sessionStorage.setItem("refresh_token", responseData.refresh_token)
        // console.log("STORAGE", sessionStorage)
        this.$store.commit("setAuthStatus", true);
        this.$router.push('genres')
      }
    }
  },
    beforeCreate() {
    if (this.$store.getters.getAuthStatus) {
      router.push("/genres")
    }
  }
};
</script>

<style scoped>
h1 {
  font-family: "Lobster Two";
  font-weight: 600;
  font-size: 2rem; 
}
.username-error, .password-error {
  color: tomato;
  font-weight: 600;
}
.container {
  max-width: 500px;
}

</style>
