<template>
<div class="data">
      <sidebarDash :currentpage="this.currentpage"></sidebarDash>
<div class="outerBoxOverview">
      <div class="headlineUsers">
        <p>Benutzer</p>
      </div>
<div class="button-wrapper">
      <button class="add-user button is-success is-rounded" @click="changePopup()">Add User</button>
</div>
      <div class="scrollableUsers">
        <!-- <to-do-form @user-added="addUser"></to-do-form> -->
        <ul>
        <li v-for="user in orderedUsersById" :key="user.userid">  
            <to-do-item @user-updated="updateUser" @user-delete="deleteUser"
                        :user="user"                    
                        :roles="Roles"
                        :organisations="Organisations"></to-do-item>
        </li>
        </ul>
    </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
// import { useCookies } from 'vue3-cookies';

// import ToDoForm from './ToDoForm.vue';
import ToDoItem from './ToDoItem.vue';
import sidebarDash from "../dashboards/sidebar/sidebarDash";

export default{
components:{
    // ToDoForm,
    ToDoItem,
    sidebarDash
},
 data() {
    return {
      User: [],
      Roles: [],
      Organisations: [],
      accessAllowed: false,
      currentpage: "user"

    };
  },
computed: {
  orderedUsersById: function () {
    return [...this.User].sort((a,b) => b.userid - a.userid);
  }
},
mounted() {
        this.getRoleData();        
        this.getOrganisationData();
        this.getUserData();

    },
methods:{
    addUser(user){
        this.postUserData(user);
    },
    updateUser(user){
    const itemIndex = this.User.findIndex(x => x.userid == user.userid);
    this.User[itemIndex] = user;
    },
    deleteUser(id){
        let itemIndex = this.User.findIndex(x => x.userid == id);
        this.User.splice(itemIndex,1);
        
    },
    getUserData(){
        const path = '/api/user/'
        axios.get(path, {
            withCredentials:true
        })
        .then((response) => {
            this.accessAllowed = true;
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
            return axios.get(path, {
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
            return axios.get(path, {
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
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.data {
  display: grid;
  grid-template-columns: 30% 70%;
  height: 100vh;
  width: 100%;
  overflow: hidden;
}

.firstItem{
  margin-left: 2%;
}

.lineItem{
  padding-left: 1rem;
  flex-direction: row;
  display: flex;
  justify-content: space-around;
}

.lineItem p{
  margin-right: 2rem;
}

.headlineUsers {
  width: 59vw;
  text-align: left;
  align-items: flex-start;
  margin-bottom: 2rem;
  margin-top: 2rem;
  padding-bottom: 1rem;
  border-bottom: rgba(109, 105, 114, 0.46) 1px solid;
}

.scrollableUsers {
  overflow-x: hidden;
  height: 80%;
  width: 64vw;
  margin-top: 1%;
  margin-bottom: 2%;
}

.wirfuerschuleimg {
  align-items: center;
  width: 60%;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.headline {
  margin: 1rem;
  padding-bottom: 1rem;
  width: 80%;
  text-align: left;
  border-bottom: #d9d9d9 1px solid;
}

.outerBoxOverview {
  align-items: center;
  grid-template-columns: 20% 10% 10% 10%;
  justify-content: space-between;
  flex-wrap: nowrap;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  padding-bottom: 5%;
}

.fontHeadline {
  font-size: 20px;
  letter-spacing: 0.05em;
  font-family: 'Roboto', sans-serif;
  align-content: center;
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  text-align: center;
  color: #d9d9d9;
  align-items: center;
}



.label{
  color: white;
  margin-top: 2vh;
}


::-webkit-scrollbar {
  width: 10px;
  height: 5px;
}

::-webkit-scrollbar-track {
  background: white;
}

::-webkit-scrollbar-thumb {
  background-color: grey;
  border-radius: 10px;
}

a{
  color: #d9d9d9;
}

.button-wrapper{
  width:84%;
text-align:right;
}



</style>
