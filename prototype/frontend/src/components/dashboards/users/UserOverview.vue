<template>
  <div v-if="openPopup">
    <PopupAddUser ></PopupAddUser>
  </div>
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
        <UserList></UserList>
      </div>
    </div>
  </div>
  </template>

<script>
/* eslint-disable */
import UserList from './UserList.vue';
import OpenPopupButton from "../OpenPopupButton";
import PopupAddUser from "../../popups/users/PopupAddUser";
import HomeButton from "../HomeButton";
import sidebarDash from "../sidebar/sidebarDash";


export default {
  components: {PopupAddUser, UserList, OpenPopupButton, HomeButton, sidebarDash},
  data() {
    return {
      adding: false,
      rendered: false,
      openPopup: false,
      currentpage: "user"
    }
  },
  methods: {
    changePopup(){
      this.openPopup = true;
    },
    rerender(value) {
      this.rendered = value;
      this.$forceUpdate();
      location.reload();
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
  width: 63vw;
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
  width:85%;
text-align:right;
}
</style>
