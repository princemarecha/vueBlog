<template>
    <div class="page-category">
<div class="columns is-multiline">
    <div class="columm is-12">
        <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
    </div>

    <blogBox 
              v-for="blog in category.blog "
              v-bind:key="blog.id"
              v-bind:blog="blog"> 
      </blogBox>
</div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma'
import blogBox from './blogBox.vue'

export default{
    name: 'Category',
    components: {
        blogBox
    },
    data(){
        return{
            category:{
                blogs:[]
            }
        }
    }, 
    mounted(){
        this.getCategory()
    },
    watch:{
        $route(to, from){
            if(to.name === 'category'){
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory(){
            const categorySlug = this.$route.params.category_slug

            axios
                .get(`/api/v1/blogs/${categorySlug}/`)
                .then(response =>{
                    this.category = response.data
                })
                .catch(error =>{
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: bottom-right,
                    })
                }
                )
        }
    }
}

</script>