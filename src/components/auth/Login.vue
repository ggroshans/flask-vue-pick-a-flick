<template>
  <div class="container">
    <h1>Login</h1>
    <form>
      <div class="input-group form-group">
        <div class="input-group-prepend">
          <span class="input-group-text"
            ><b-icon icon="person-fill"></b-icon
          ></span>
        </div>
        <input type="text" class="form-control" placeholder="username"  v-model="username" />
      </div>
      <div class="input-group form-group">
        <div class="input-group-prepend">
          <span class="input-group-text"
            ><b-icon icon="key-fill"></b-icon
          ></span>
        </div>
        <input type="password" class="form-control" placeholder="password" v-model="password"/>
      </div>
      <!-- <div class="row align-items-center remember">
        <input type="checkbox" />Remember Me
      </div> -->
      <div class="form-group">
        <button
          @click.prevent="submitLogin"
          value="Login"
          class="btn btn-primary float-right"
        >Submit</button>
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
export default {
  data() {
    return {
      username: null,
      password: null
    };
  },
      async submitLogin() {
      console.log("fired")
    const resp = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        "username": this.username,
        "password": this.password
      })
    });
    this.username = "";
    this.password = "";
    }

};
</script>

<style scoped>
h1 {
  font-family: "Lobster Two";
}
</style>
