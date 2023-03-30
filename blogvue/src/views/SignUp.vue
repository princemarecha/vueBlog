<template>
    <div class="page-sign-up">
        <div class="column is-4 is-offset-4">
            <h1 class="title">Sign Up</h1>
                <form @submit.prevent="submitform">
                <div class="field">
                    <label for="Username">Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                </div>
                <div class="field">
                    <label >Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                </div>
                <div class="field">
                    <label >Repeat Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                </div>

                <div class="notification is-danger" v-if="errors.length">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="field">
                        <div class="control">
                            <button class="is-dark button">Sign Up</button>
                        </div>
                </div>

                <div>
                    Or <router-link to="/login">click here</router-link> to login!
                </div>

                </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';


export default{
    name: 'SignUp',
    methods:{
        submitform(){
            this.errors = [];

            if (this.username === ""){
                this.errors.push('The username is missing')
            }
            if (this.password === ""){
                this.errors.push('The password is too short')
            }
            if (this.password !== this.password2){
                this.errors.push('The passwords do not match')
            }
            if (!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios.post("/api/v1/users/", formData)
                .then(response=>{
                    console.log(response)

                    this.$router.push('/log-in')
                })
                 .catch(error =>{
                        if (error.response){
                            for (const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message){
                            this.errors.push('Something went wrong, Please try again')

                            console.log(error)
                        }
                    })
            }





            
        }
    },
    data(){
        return{
            username:'',
            password:'',
            password2:'',
            errors:[]
        }
    },
}

</script>