<template>
  <div class="container">
    <h1>Register</h1>
    <form>
      <div class="input-group form-group">
        <div class="input-group-prepend">
          <span class="input-group-text"
            ><b-icon icon="person-fill"></b-icon
          ></span>
        </div>
        <input type="text" class="form-control" placeholder="username" v-model="username"/>
      </div>
      <div class="input-group form-group">
        <div class="input-group-prepend">
          <span class="input-group-text"
            ><b-icon icon="key-fill"></b-icon
          ></span>
        </div>
        <input type="password" class="form-control" placeholder="password" v-model="password" />
      </div>
      <!-- <div class="row align-items-center remember">
        <input type="checkbox" />Remember Me
      </div> -->
      <div class="form-group">
        <button
          @click.prevent="submitRegistration"
          type="submit"
          class="btn btn-primary float-right"
        >Submit</button>
      </div>
    </form>
    <div>
      <p>
        Already have an account?
        <router-link to="/login">Log In Here</router-link>
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
  methods: {
    async submitRegistration() {
      console.log("fired")
    const resp = await fetch("http://localhost:5000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        "username": this.username,
        "password": this.password
      })
    });
    responseData = await resp.json();
    console.log('response data', responseData);
    this.username = "";
    this.password = "";
    }
  }

};
</script>

<style scoped></style>
