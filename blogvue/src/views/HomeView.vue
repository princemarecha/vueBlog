<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
            Welcome to Prince Marecha's Opinions
        </p>
        <p class="subtitle">
            stay updated shamwari!
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest Blogs</h2>
      </div>

      <div 
      class="column is-3"
      v-for="blog in latestBlogs"
      v-bind:key="blog.id">
      
      <div class="box">
        <figure class="image mb-4">
            <img :src="blog.get_thumbnail">
        </figure>
      </div>

      <h3 class="is-size-4">{{ blog.name }}</h3>
      <router-link v-bind:to="blog.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
      </div>

  </div>
  </div>
</template>

<script>

import axios from 'axios'
export default {
  name: 'HomeView',
  data(){
    return{
      latestBlogs:[]
    }
  },
  components: {

  },
  mounted(){
    this.getLatestBlogs()
  },
  methods:{
    getLatestBlogs(){
      axios
        .get('api/v1/latest-blog')
        .then(response =>{
            this.latestBlogs = response.data
        })
        .catch(error =>{
            console.log(error)
          })
    }
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
