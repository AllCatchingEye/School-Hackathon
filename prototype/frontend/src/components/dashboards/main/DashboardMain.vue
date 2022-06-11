<template>
<div class="data">
    <div class="sidebar">
      <div class="fontHeadline">
        <img class="wirfuerschuleimg" alt="wir für schule logo" src="../../../assets/wirfuerschuleLogoweiß.png" />
        <p class="headline">Dashboard</p>
      </div>
      <div class="sidebarBottom">
        <div>
          <LogoutButton></LogoutButton>
        </div>
        <p class="label">© 2022 wirfuerschule.de</p><br>
        </div>
      </div>
    <div class="outerBoxOverview">

      <div class="headlineUsers">
        <p>Dashboard</p>
      </div>
      <div class="userDataHeader">
      </div>
      <div class="UpperLinks">
        <div class="ButtonElement UserManagement" @click="routeUserManagement()">
          <p>Usermanagement</p>
          <i class="fa-solid fa-angle-right"></i>
        </div>
        <div class="ButtonElement Hackathons" @click="routeHackathons()">
          <p>Hackathons</p>
          <i class="fa-solid fa-angle-right"></i>
        </div>
      </div>
      <div class="LowerLinks">
        <div class="bigButton" @click="routeEvaluation()">
          <p>Evaluation</p>
          <i class="fa-solid fa-angle-right"></i>
        </div>
      </div>
      <router-view></router-view>
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
          role: ''
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
          const path = '/api/role/own/'
          axios.get(path, {
            withCredentials: true
          })
            .then((response) => {
              this.email = response.data.email;
              this.role = response.data.role;
            })
            .catch(() => {
            })
        },

        routeUserManagement(){
          window.open("/user-overview", "_self");
        },
        routeHackathons(){
          window.open("/hackathons", "_self");
        },
        routeEvaluation(){
          window.open("/evaluation", "_self");
        }
      }

    }
</script>


<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");

.data {
  display: grid;
  grid-template-columns: 30% 70%;
  height: 100vh;
  width: 100%;
  overflow: hidden;
}

.UpperLinks{
  margin-top: 5%;
  position: relative;
  display: flex;
  width: 95%;
  height: 30%;
  flex-direction: row;
  align-content: center;
  justify-content: space-around;
  align-items: center;
}

.UserManagement{
  background: rgb(13,35,133);
  background: linear-gradient(142deg, rgba(13,35,133,1) 7%, rgba(52,152,219,1) 100%);
}

.Hackathons{
  background: rgb(85,0,61);
  background: linear-gradient(142deg, rgba(85,0,61,1) 7%, rgba(168,3,122,1) 100%);
}
.ButtonElement{
  cursor: pointer;
  border-radius: 30px;
  color: white;
  font-size: 2rem;
  font-family: 'Open Sans', sans-serif;
  font-weight: 100;
  display: flex;
  justify-content: space-around;
  align-items: center;
  align-content: center;
  width:40%;
  height: 80%;
}

.LowerLinks{
  width: 95%;
  height: 70%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  align-content: center;
}

.bigButton{
  cursor: pointer;
  border-radius: 30px;
  color: white;
  font-size: 3rem;
  font-family: 'Open Sans', sans-serif;
  font-weight: 100;
  background: rgb(223,80,0);
  background: linear-gradient(142deg, rgba(223,80,0,1) 7%, rgba(168,92,3,1) 100%);
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
