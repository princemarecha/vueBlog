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

    <div class="">
      <div class="">
          <h2 class="is-size-2 ">Latest Blogs</h2>
      </div>
  <div class="grid lg:grid-cols-3 md:grid-cols-2 mx-auto place-content-center">
      <blogBox 
              v-for="blog in latestBlogs "
              v-bind:key="blog.id"
              v-bind:blog="blog"> 
      </blogBox>
    </div>
  </div>
  </div>
</template>

<script>

import axios from 'axios'
import blogBox from './blogBox.vue'

export default {
  name: 'HomeView',
  data(){
    return{
      latestBlogs:[]
    }
  },
  components: {
    blogBox
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

