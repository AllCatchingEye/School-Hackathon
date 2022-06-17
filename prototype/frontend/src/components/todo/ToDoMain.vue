<template>
<div class="data">
    <div v-if="accessAllowed">
    <h1>My To-Do List</h1>
    <to-do-form @user-added="addUser"></to-do-form>
    <ul>
      <li v-for="user in orderedUsersById" :key="user.userid">  
        <to-do-item @user-updated="updateUser"
                    :userid="user.userid"
                    :name="user.name" 
                    :firstname="user.firstname" 
                    :organisation="user.organisations.orgaid" 
                    :role="user.roles.roleid" 
                    :email="user.email"
                    :roles="Roles"
                    :organisations="Organisations"></to-do-item>
      </li>
    </ul>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
// import { useCookies } from 'vue3-cookies';

import ToDoForm from './ToDoForm.vue';
import ToDoItem from './ToDoItem.vue';
export default{
components:{
    ToDoForm,
    ToDoItem
},
 data() {
    return {
      User: [],
      Roles: [],
      Organisations: [],
      accessAllowed: false
    };
  },
computed: {
  orderedUsersById: function () {
    return [...this.User].sort((a,b) => b.userid - a.userid);
  }
},
mounted() {
        this.getUserData();
        this.getRoleData();
        this.getOrganisationData();
    },
methods:{
    addUser(user){
        this.postUserData(user);
        
    },
    updateUser(){
        //console.log(this.componentKey);



    },
    getUserData(){
        const path = '/api/user/'
        axios.get(path, {
            withCredentials:true
        })
        .then((response) => {
            this.accessAllowed = true;

            let bla = response.data;
            for(let i = 0; i < response.data.length; i++){
                bla[i]["incrementor"] = 0;
            }
            this.User = response.data;
            console.log(this.User);

        }).catch((err)=>{
             switch(err.response.status) {
                // case 409:
                //     console.log("Error 409")
                //     break;
                // case 500:
                //     console.log("Error 500")
                //     break;
                case 401:
                    this.$router.push({name:"Login", params: {message: "You have to be logged in"}});
                    break;
                default:
                    console.log("An unexpected Error occurred.")

                }   
        })
    },
    postUserData(user){
        const path = '/api/register/'
        const userJson = JSON.stringify(user);
        console.log(userJson);

        axios.post(path, userJson, {
          headers: {
            'Content-Type': 'application/json'
          },
          withCredentials: true
        })
        .then((response) => {
            console.log(response.data.dataobj)
            this.User.push(response.data.dataobj);
        }).catch((err)=>{             
            switch(err.response.status) {
                case 409:
                    console.log("This Emails exists")
                    break;
                case 500:
                    console.log("Please enter valid mail")
                    break;
                default:
                    console.log("An unexpected Error occurred.")
                }        
        })
    },
     getRoleData(){
            const path = '/api/role/'
            axios.get(path, {
                withCredentials:true
            })
            .then((response) => {
                this.Roles = response.data;
                console.log(this.Roles);
            }).catch((err)=>{
                console.log(err);
                switch(err.response.status) {

                    case 401:
                        this.$router.push({name:"Login", params: {message: "You have to be logged in"}});
                        break;
                    default:
                        console.log("An unexpected Error occurred.")

                    }   
            })
        },    
    getOrganisationData(){
            const path = '/api/organisation/'
            axios.get(path, {
                withCredentials:true
            })
            .then((response) => {
                this.Organisations = response.data;
                console.log(this.Organisations);
            }).catch((err)=>{
                console.log(err);
                switch(err.response.status) {
                    case 401:
                        this.$router.push({name:"Login", params: {message: "You have to be logged in"}});
                        break;
                    default:
                        console.log("An unexpected Error occurred.")

                    }   
            })
        },
}

}

</script>