<template>
  <div class="container">
      <h1>Login</h1>
    <form>
      <div class="input-group form-group">
        <div class="input-group-prepend">
          <span class="input-group-text"><b-icon icon="person-fill"></b-icon></span>
        </div>
        <input type="text" class="form-control" placeholder="username" />
      </div>
      <div class="input-group form-group">
        <div class="input-group-prepend">
    <span class="input-group-text"><b-icon icon="key-fill"></b-icon></span>
        </div>
        <input type="password" class="form-control" placeholder="password" />
      </div>
      <!-- <div class="row align-items-center remember">
        <input type="checkbox" />Remember Me
      </div> -->
      <div class="form-group">
        <input type="submit" value="Login" class="btn btn-primary float-right" />
      </div>
    </form>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      pTag: null
    };
  },
  async created() {
    const resp = await fetch("http://localhost:5000/greeting");
    console.log("response", resp);
    const obj = await resp.json();
    console.log("obj", obj);
    this.pTag = obj.test;
  }
};
</script>

<style scoped>
h1 {
  font-family: "Lobster Two";
}
</style>
