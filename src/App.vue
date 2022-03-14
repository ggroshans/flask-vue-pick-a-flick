<template>
  <div id="app">
    <Header></Header>
    <h1></h1>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/Header.vue'
export default {
  name: 'App',
  components: {
    Header,
  
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Limelight&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
@import './styles/loading.css';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
