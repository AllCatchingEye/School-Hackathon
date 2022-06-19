<template>
  <div v-if="openPopup">
    <PopupAdminHackathonBuild></PopupAdminHackathonBuild>
  </div>
<div class="data">
  <sidebarDash :currentpage="this.currentpage"></sidebarDash>
    <div class="outerBoxOverview">
      <div class="headlineUsers">
        <p>Hackathons</p>
      </div>
      <div class="button-wrapper">
        <button class="add-hackathon button is-success is-rounded" @click="changePopup()">Hackathon hinzufügen</button>
      </div>
      <div class="scrollableUsers">
        <UserList></UserList>
      </div>
    </div>
  </div>
  </template>

<script>
/* eslint-disable */
import UserList from './HackathonList';
import OpenPopupButton from "../OpenPopupButton";
import PopupAdminHackathonBuild from "../../popups/hackathons/PopupAdminHackathonBuild";
import HomeButton from "../HomeButton";
import sidebarDash from "../sidebar/sidebarDash";

    export default {
        components: {HomeButton, PopupAdminHackathonBuild, OpenPopupButton, UserList, sidebarDash },
      data() {
        return {
          openPopup: false,
          currentpage: "hackathon"
        }},
      methods: {
        changePopup(){
          this.openPopup = true
        },
        goHome(){
          this.$router.push('/');
        }
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
  max-height: 75vh;
  height: 100%;
  width: 63vw;
  margin-top: 5%;
  margin-bottom: 5%;
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
  grid-template-columns: 15% 10% 10% 10%;
  justify-content: space-around;
  flex-wrap: nowrap;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
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

.userDataHeader{
  display: grid;
  justify-content: space-evenly;
  width: 60vw;
  grid-template-columns: 25% 10% 10% 10%;

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


.label{
  color: white;
  margin-top: 2vh;
}

.button-wrapper{
  width:84%;
  text-align:right;
}
</style>
