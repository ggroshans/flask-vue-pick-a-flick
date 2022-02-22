<template>
    <div class="container">
        <h1>Blind Book Date</h1>
        <p>{{pTag}}</p>
    </div>
</template>

<script>
/* eslint-disable */
    export default {
    data() {
        return {

            pTag: null,
            }
            },
    async created() {
        
            const resp = await fetch("http://localhost:5000/greeting");
            console.log('response', resp)
            const obj = await resp.json();
            console.log("obj", obj);
            this.pTag = obj.test; 
        }
    }
    
</script>

<style scoped>
    h1 {
        font-family: 'Lobster Two';
    }
</style>