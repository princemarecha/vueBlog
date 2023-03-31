<template>
    <div class="page-blog">
        <div class="column is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="blog.get_image"/>
                </figure>

                <h1 class="title">{{ blog.title }}</h1>
                
                <p>{{ blog.content }}</p>
            </div>
            <div class="is-column is-3">
                <button class="button is-danger" @click="deleteBlog(blog)">                       
                                <p>DELETE</p>
                        </button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default{
    name: 'Blog',
    data(){
        return{
            blog:{}
        }
    },
    mounted(){
        this.getBlog()
    },
    methods:{
        getBlog(){
            const category_slug = this.$route.params.category_slug
            const blog_slug = this.$route.params.blog_slug

            axios
                .get(`/api/v1/blogs/${category_slug}/${blog_slug}`)
                .then(response =>{
                    this.blog = response.data
                    console.log(response.data)
                })
                .catch(
                    error=>{
                        console.log(error)
                    }
                )
        },
        deleteBlog(blog) {
           axios.delete(`/api/v1/getBlogs/${blog.id}/`) 
            .then(location.href = '/my-account')
            .catch(error=>console.log(error))
        },
        
    }
}
</script>