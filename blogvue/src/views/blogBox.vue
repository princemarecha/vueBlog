<template>

<div class="box">
    <figure class="image mb-4">
        <img :src="blog.get_thumbnail">
    </figure>
</div>

<h3 class="is-size-4">{{ blog.name }}</h3>
    <router-link v-bind:to="blog.get_absolute_url" class="button is-dark mt-4">View Details</router-link>

</template>

<script>
export default{
    name:'Blog',
    props:{
        blog: Object
    }
}
</script>

<style scoped>
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}
</style>
