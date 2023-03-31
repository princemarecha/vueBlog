<template>
    <div class="mb-100">
        <div class="">
            <div class="">
                <figure class="grid place-content-center">
                    <img v-bind:src="blog.get_image"/>
                </figure>
                <hr/>
                <h1 class="italic overline font-roboto text-3xl text-extrabold">{{ blog.name }}</h1>
                <hr/>
                
               
                
<p class="mb-5 text-align:justify text-gray-500 dark:text-gray-400 first-line:uppercase first-line:tracking-widest first-letter:text-7xl first-letter:font-bold first-letter:text-gray-900 dark:first-letter:text-gray-100 first-letter:mr-3 first-letter:float-left">{{ blog.content }}</p>
<hr/>
            </div>
            <hr/>
            <div class="flex justify-end" >
                <button class="button is-danger mx-5" @click="deleteBlog(blog)">                       
                                <p><span class="fa fa-trash"></span></p>
                        </button>
                <button class="button is-caution" @click="toggleUpd()">                       
                                <p><span class="fa fa-edit"></span></p>
                </button>
            </div>
        </div>
    </div>
    <hr/>
<h1 class="flex items-center text-5xl font-extrabold text-yellow-800 md:mt-50 " id="update">Update Your Blog</h1>
<div class="border-double md:p-10 border mt-100 shadow-2xl  " id="update2">
<div class="mb-6">
    <label for="base-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Blog Title</label>
    <input type="text" id="base-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
</div>    
<div class="mb-6">
    <label for="large-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Blog Content</label>
    <input type="text" id="large-input" class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
</div>

<div>
    <label for="small-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">The Image</label>
    <input type="text" id="small-input" class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
    <input type="file"/>
</div>
<div class="justify-end flex">
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Update
</button>
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
        toggleUpd(){
            var element = document.getElementById("update")
            element.classList.toggle("hidden")
            var element2 = document.getElementById("update2")
            element2.classList.toggle("hidden")
        }
    }
}
</script>