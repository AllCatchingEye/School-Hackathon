<template>
<div class="data">
    <div class="sidebar">
      <div class="fontHeadline">
        <img class="wirfuerschuleimg" alt="wir für schule logo" src="../../../assets/wirfuerschuleLogoweiß.png" />
        <p class="headline">Dashboard</p>
      </div>
      <div class="NameSection">
        <div class="NameItem">
          <p>Hallo</p>
          {{ this.firstname }}
          {{ this.name }}
        </div>
        <div class="NameItem">
          <p>Email:</p>
          {{ this.email }}
        </div>
        <div class="NameItem">
          <p>Organisation:</p>
          {{ this.organisation }}
        </div>
        <div class="NameItem">
          <p>Position:</p>
          {{ this.role }}
        </div>
      </div>
      <div class="sidebarBottom">
        <div>
          <LogoutButton></LogoutButton>
        </div>
        <p class="label">© 2022 wirfuerschule.de</p><br>
        </div>
      </div>


    <div class="tiles-wrapper">
      <h1>Hi {{ this.firstname }}, <br> was möchtest du tun?</h1>
      <div class="ctile" v-if="this.role === 'Admin' || this.role === 'Superadmin'">
            <router-link to="/user-overview">

            <h2>Usermanagement</h2>

            <i class="fa-solid fa-angle-right"></i>
                  </router-link> 

      </div>

      <div class="ctile" v-if="this.role === 'Admin'">
                  <router-link to="/hackathons">

      <h2>Hackathonmanagement</h2>
      <i class="fa-solid fa-angle-right"></i>
                        </router-link> 

      </div>
      
      <div  class="ctile" v-if="this.role === 'Superadmin'">
            <router-link to="/schools">

            <h2>Schulmanagement</h2>
            <i class="fa-solid fa-angle-right"></i>
              </router-link> 

      </div>
          <div  class="ctile" v-if="this.role === 'Teacher'">
            <router-link to="/keys">

            <h2>Schlüsselmanagement</h2>
            <i class="fa-solid fa-angle-right"></i>
            </router-link> 

          </div>
    </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import { useCookies } from 'vue3-cookies';
import LogoutButton from './../../LogoutButton.vue';
axios.defaults.withCredentials = true;

    export default {
      components: {LogoutButton},
      data() {
        return {
          email: '',
          role: '',
          firstname: '',
          name: '',
          organisation: '',
        }
      },
      mounted() {
        this.getUserInfo();
      },
      setup() {
        const { cookies } = useCookies();
        const cookieSet = cookies.isKey("access_token_cookie");
        if (cookieSet) {
          let cookieAllowed = false;
          const path = '/api/role/own/'
          axios.get(path, {
            withCredentials: true
          })
            .then(() => {
              cookieAllowed = true;
            })
            .catch(() => {
              cookies.remove("access_token_cookie");
              deleteCookie();
              document.cookie = "access_token_cookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
              routeLogin();
            })

      }else{
        routeLogin();
      }
        function deleteCookie(){
          const path = '/api/logout/';
          axios.post(path, {}, {
            headers: {
              'Content-Type': 'application/json'
            }
          });
        }
       function routeLogin() {
         window.open("/login", "_self");
        }
      },
      methods:{
        getUserInfo() {
          const path = '/api/user/own/'
          axios.get(path, {
            withCredentials: true
          })
            .then((response) => {
              console.log(response);
              this.email = response.data.email;
              this.role = response.data.roles.description;
              this.firstname = response.data.firstname;
              this.name = response.data.name;
              this.organisation = response.data.organisations.name;
              console.log(this.organisation, this.role, this.firstname, this.name, this.email)
            })
            .catch((e) => {
              console.log(e);
            })
        }
      }

    }
</script>


<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");
$green :#37b1c5;

.tiles-wrapper{

display: flex;
justify-content: space-around;
flex-wrap: wrap;
align-items:flex-start;
align-content:center;
margin-top:7%;

  h1{
    width: 100%;
    text-align: center;
    font-family: "Open Sans", sans-serif;
    font-weight: bold;
    font-size: 3.5rem;
    position: absolute;
    top: 5%;
  }
  .ctile{
    &:hover{
        background:$green;
        color:white;
        transition:.3s;

    }
    
    transition:.3s;
    cursor:pointer;
    width: 75%;
    max-height: 117px;
        height: 100%;

    box-shadow: 1px 6px 15px -3px rgba(0, 0, 0, 0.56);
    margin: 10px;
    border-left:6px solid $green;

    a{
      width:100%;
      display: flex;
      height:100%;
    align-items: center;
    justify-content: space-between;
    color:black;
    }
    h2{
      text-transform:uppercase;
      font-size: 2rem;
      font-family: 'Open Sans', sans-serif;
      font-weight: 100;
      font-weight:bold;
      width:75%;
      padding-left:8%;

    }
    i{
      width:20%;
      background:$green;
      color:white;
      height:100%;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 70px;
    }
  }
}

.data {
  display: grid;
  grid-template-columns: 30% 70%;
  height: 100vh;
  width: 100%;
  overflow: hidden;
}



.NameSection{
  margin-top: 5%;
  font-family: 'Open Sans', sans-serif;
  font-weight: 100;
  color: white;
  font-size: 1.5rem;
  width: 100%;
  height: 50%;
  display: flex;
  align-content: center;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.NameItem{
  margin-top: 3%;
  width: 80%;

}


.ButtonElement{
  cursor: pointer;
  color: black;
  font-size: 2rem;
  font-family: 'Open Sans', sans-serif;
  font-weight: 100;
  display: flex;
  justify-content: space-around;
  align-items: center;
  align-content: center;
  width:40%;
  height: 80%;
  background:white;

  p{
    font-weight:bold;
  }
  i{
    color:white;
    background:$green;

  }
}

.ButtonElement *{
  display: flex;
  justify-content: space-around;
  align-items: center;
  align-content: center;
  width:95%;
  height: 100%;
  margin-left: 5%;
}

.LowerLinks{
  width: 95%;
  height: 70%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  align-content: center;
}

p{
  font-family: 'Open Sans', sans-serif;
  font-weight: 100;
}

.bigButton{
  cursor: pointer;
  border-radius: 30px;
  color: white;
  font-size: 3rem;
  font-family: 'Open Sans', sans-serif;
  font-weight: 100;
  background: rgb(13,35,133);
  background: linear-gradient(142deg, rgba(13,35,133,1) 38%, rgba(168,3,122,1) 100%);
  height: 80%;
  width: 90%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  align-content: center;
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
  font-weight: bold;
  font-size: 1.5rem;
  width: 59vw;
  text-align: left;
  align-items: flex-start;
  margin-bottom: 2rem;
  margin-top: 2rem;
  padding-bottom: 1rem;
  border-bottom: rgba(109, 105, 114, 0.46) 1px solid;
}

.headlineUsers *{
  font-weight: bold;
}

.scrollableUsers {
  overflow: scroll;
  height: 75%;
  width: 60vw;
  margin-top: 5%;
  margin-bottom: 5%;
}

.sidebar {
  height: 100%;
  width: 100%;
  background-color: #000a38;
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
  justify-content: flex-start;
  flex-wrap: nowrap;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  padding-bottom: 10%;
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

.sidebarBottom{
  position: absolute;
  bottom: 2rem;
  width: 30%;
  text-align: center;
  color: #d9d9d9;
}

.userDataHeader{
  display: flex;
  justify-content: space-evenly;
  width: 60vw;

}

.label{
  color: white;
  margin-top: 2vh;
}
</style>
