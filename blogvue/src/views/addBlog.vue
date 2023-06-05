<!-- BELOW IS THE CODE FOR THE POST AND I TRIED TO MAKE EXPLANATIONS IN THE FORM OF COMMENTS

THANK YOU, PRINCE MARECHA-->


<template>
    <h1 class="flex items-center text-5xl font-extrabold text-yellow-800 md:mt-50 " id="Post">Post Your Blog</h1>
   <form action="" enctype="multipart/form-data"  @submit.prevent="submitForm">
<div class="border-double md:p-10 border mt-100 shadow-2xl  " id="Post2">
<div class="mb-6">
    <!-- BLOG TITLE FIELD -->
    <label for="base-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Blog Title</label>
    <input type="text" v-model="blogtitle" id="base-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
</div>    
<div class="mb-6">
    <!-- BLOG CONTENT FIELD -->
    <label for="large-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Blog Content</label>
    <textarea rows="8" cols="50" v-model="blogcontent" id="large-input" class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"/>
</div>

<div>
    <!-- BLOG IMAGE FIELD -->
    <!-- the @change event triggers a function "onFileSelected" which feeds value to variable "fileSelected" which is
    image data, from the event.target object -->

    <label for="small-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">The Image</label>
    <input class="my-4" type="file" accept="image/jpeg" @change="onFileSelected"/>

    <!-- CATEGORY FIELD which is a dropdown with 4 options -->

    <label for="small-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Category</label>
    <select id="small-input"  v-model="category" class="block w-1/2 p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        <option value="4">Entertainment</option>
        <option value="3">News</option>
    </select>

    <!-- KEYWORDS OR HASHTAGS FIELD FOR THE BLOG -->

    <label for="small-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Keywords</label>
    <input type="text"  v-model="keywords" id="small-input" class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
    
</div>
<div class="justify-end flex my-4">

    <!-- THE SUBMIT BUTTON  with the onclick event to run a "submitForm()" function which will post the blog to
    storage database -->

<button @click="submitForm()"  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Post
</button>
</div>
<div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
</div>
</form>

</template>


<script>
// this is the "axios" module for our CRUD purposes, we are importing to use in this component.
import axios from 'axios';

export default{
    name: 'AddProduct',
    data (){
        // instantiation of the selectedFile variable to store image data
        // instantiation of the errors array to store errors
        return{selectedFile:null,
                errors:[]
        }
    },
    methods:{

        // asynchronous method "SUBMIT" to submit form to storage database 

        async submitForm(event){
            // prevent default behaviour of the button
            event.preventDefault()
            axios.defaults.headers.common["Authorization"] = ""
            const formData = new FormData()

            // get userid from the local storage
            let b  = parseInt(localStorage.getItem("userid"))
            
            // append to form an "image" with data from "selectedFile"
            formData.append("image",this.selectedFile)
            // append to form a "name" with data from "blogtitle" which was taken from input using v-model
            formData.append("name", this.blogtitle)
             // append to form an "author" with data from "b" which was taken from localstorage
            formData.append("author", b)
             // append to form a "category" with data from "category" which was taken from  a "select" using v-model
            formData.append("category", parseInt(this.category))
             /*append to form a "slug" with data from a function "cleanSlug" which accepts the blogtitle data as a parameter
             and returns a more unique blog value, to make sure that each blog is unique and a "GET" request for a single value 
             wouldn't attempt to return multiple values */
            formData.append("slug",this.cleanSlug(this.blogtitle))
            // append to form a "content" with data from "blogcontent" which was taken from  input using v-model
            formData.append("content", this.blogcontent)
            // append to form a "keywords" with data from "blogcontent" which was taken from  input textarea using v-model
            formData.append("keywords", this.keywords)

            await axios
                //axios "POST" request to post the fully formed formData information to backend for storage
                .post("/api/v1/getBlogs/", formData)
                .then(response => {
                    // if response is successful and record has been created, "201" response status is returned, the site 
                    // is redirected to the account page 
                    if (response.status === 201)
                        {
                            location.href = '/my-account'
                        }

                    // otherwise if the response status is 400, just log the response for debugging purposes
                    else if(response.status === 400){
                        
                        console.log(response)
                    }
                })
                //the catch block to catch exceptions and push the error response to the error array which will be 
                // instantly displayed in the front end to alert the user of what may have gone wrong
                .catch(error => {
                    if (error.response) {
                        this.errors = []
                        for (const property in error.response.data) {
                            this.errors.push(`${error.response.data[property]}`)
                        }
                //else if there is an exception error but the error object doesn't have a response, we push a generic error
                //message to the error array to display
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
            console.log(formData)
        },
        //function to save Image data to the "selectedFile" variable
        onFileSelected(event){
            this.selectedFile = (event.target.files[0])
        },
        //function to add random number to slug string to make it more unique
        cleanSlug(slug){
            var terry = slug.toLowerCase().split(" ").join("_")
            let x = Math.floor((Math.random() * 1000) + 1)
            terry = terry + x
            return terry
        }
    }
}
</script>