<template>
    <div class="page-search">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <h1 class="title">Search</h1>

                    <h2 class="is-size-5 has-text-grey">Search Term:"{{ query }}"</h2>
                </div>
                <blogBox 
              v-for="blog in blogs "
              v-bind:key="blog.id"
              v-bind:blog="blog"/> 
      
            </div>
    </div>
</template>

<script>
import axios from 'axios';
import blogBox from './blogBox.vue';

export default{
    name: 'Search',
    components:{
        blogBox
    },
    data(){
        return{
            blogs:[],
            query:''
        }
    },
    mounted(){
        document.title = 'Search | Blog Redu'

        let uri =window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')){
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch(){
            await axios
                    .post('/api/v1/blogs/search', {'query':this.query})
                    .then(response=>{
                            this.blogs = response.data
                    })
                    .catch(error =>{
                            console.log(error)
                    })
           }
        }
    }
</script>