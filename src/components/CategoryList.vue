<template>
    <div>
        <router-link v-for="category in categoryList" :key="category" to="category"> <category :category="category"></category> </router-link>
    </div>
</template>

<script>
/* eslint-disable */
    import Category from './Category.vue'
    export default {
        data() {
            return {
                categoryList: null,
            }
        },
        components: {
            Category,
        },
        async created() {
            const resp = await fetch("http://localhost:5000/categorylist", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            let responseData = await resp.json(responseData)
            console.log("CATEGORY LIST WHOLE", responseData)
            this.categoryList = responseData.data.results.splice(29)
        }
    }
</script>

<style scoped>

</style>