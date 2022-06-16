<template>
  <div class="sidebar">
    <div class="sidebarheader">
      <img class="wirfuerschuleimg" alt="wir für schule logo" src="../../../assets/wirfuerschuleLogo.png" />
    </div>
    <div class="sidebarbody">
      <navigation :currentpage = currentpage ></navigation>
    </div>
    <div class="sidebarfooter">
      <div class="logoutButton">
        <logoutButton></logoutButton>
      </div>
      <p class="label">© 2022 wirfuerschule.de</p><br>
    </div>
  </div>


</template>

<script>
import Navigation from "./navigationDash";
import logoutButton from "./logoutButton";
export default {
  name: "sidebarDash",
  components: {logoutButton, Navigation},
  props: {
    'currentpage':{
      type: String,
      default: "error"
    }
  },
}
</script>

<style scoped>

.sidebar{
  display: flex;
  height: 100vh;
  width: 30vw;
  background-color: #EEEEEE;
  flex-direction: column;
  justify-content: flex-start;
  align-content: center;
  align-items: center;
}

.sidebarheader{
  display: flex;
  align-items: center;
  width: 80%;
  margin-top: 5%;
  margin-bottom: 5%;
}
.sidebarbody{
  width: 90%;
  display: flex;
  align-items: self-start;
  margin-top: 5%;
  margin-left: 5%;
}
.sidebarfooter{
  display: flex;
  position: absolute;
  bottom: 5%;
  flex-direction: column;
  align-content: center;
  align-items: center;
}

.logoutButton{
  margin-bottom: 5%;
}

</style>
