<template>
  <div @click="queryCategory">
    {{ category.display_name }}
  </div>
</template>

<script>
/* eslint-disable */
    export default {
        props: {
            'category': Object,
        },
        methods: {
        async queryCategory() {
            const resp = await fetch("http://localhost:5000/category", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body:
                    JSON.stringify({"category": this.category.list_name_encoded})
            });
            let responseData = await resp.json()
            console.log(responseData)
        }
        }
    }
</script>

<style scoped></style>
