<template>
  <div>
    <p>Hello</p>
    <p>{{this.getCurrentMovie}}</p>
  </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    methods: {},
    computed: {
      getCurrentMovie () {
          console.log(this.$store.getters.getCurrentMovie)
          console.log(this.$store)
          return this.$store.getters.getCurrentMovie;
      }
    }
  }
</script>

<style scoped>

</style>