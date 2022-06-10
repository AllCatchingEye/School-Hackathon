<template>
<div class="data">
    <div class="sidebar">
      <div class="fontHeadline">
        <img class="wirfuerschuleimg" alt="wir für schule logo" src="../assets/wirfuerschuleLogoweiß.png" />
        <p class="headline">Benutzerübersicht</p>
      </div>
      <div class="sidebarBottom">
        <div>
          <LogoutButton></LogoutButton>
        </div>
        <p class="label">© 2022 wirfuerschule.de</p><br>
        </div>
      </div>
    <div class="outerBoxOverview">
      <div>Management Dummy</div>
    </div>
  </div>
  </template>

  <script>
/* eslint-disable */
import LogoutButton from './LogoutButton.vue';

    export default {
        components: { LogoutButton },
    }
</script>

<style lang="scss">
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
