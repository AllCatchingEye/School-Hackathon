<template>
  <div class="navigation" v-if="isloaded">
    <div class="navigationheader">
      <p>Navigation</p>
    </div>
    <div class="navigationlist">
      <div class="navigationitem" :class="dashboardactive ? 'navigationitemcurrent' : 'navigationitem'" @click="routeHome()">
        <p>Dashboard</p>
      </div>
      <div class="navigationitem" :class="useractive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Admin' || this.role === 'Superadmin'" @click="routeUserManagement()">
        <p>Benutzerübersicht</p>
      </div>
      <div class="navigationitem" :class="hackathonactive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Admin' || this.role === 'Teacher'"  @click="routeHackathons()">
        <p>Hackathonübersicht</p>
      </div>
      <div class="navigationitem" :class="tokenactive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Teacher'" @click="routeKeys()">
        <p>Tokens</p>
      </div>
      <div class="navigationitem" :class="analyseactive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Admin' || this.role === 'Teacher'" @click="routeEvaluation()">
        <p>Analyse</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "navigationDash",
  props: {
    'currentpage':{
      type: String,
      default: "error"
    }
  },
  data() {
    return {
      isloaded: false,
      role: null,
      dashboardactive : false,
      useractive : false,
      hackathonactive : false,
      tokenactive : false,
      analyseactive : false
    }},
  mounted() {
    console.log(this.currentpage);
    this.getRoleInfo();
    this.selectActive();
    this.isloaded = true;
  },
  methods: {
    getRoleInfo() {
      const path = '/api/user/own/'
      axios.get(path, {
        withCredentials: true
      })
        .then((response) => {
          console.log(response);
          this.role = response.data.roles.description;
          console.log(this.role)
        })
        .catch((e) => {
          console.log(e);
        })
    },
    selectActive(){
      this.dashboardactive = this.currentpage === "dashboard";
      this.useractive = this.currentpage === "user";
      this.hackathonactive = this.currentpage === "hackathon";
      this.tokenactive = this.currentpage === "token";
      this.analyseactive = this.currentpage === "analyse";
    },
    routeHome() {
      window.open("/", "_self");
    },
    routeUserManagement(){
      window.open("/user-overview", "_self");
    },
    routeHackathons(){
      window.open("/hackathons", "_self");
    },
    routeEvaluation() {
      window.open("/evaluation", "_self");
    },
    routeSchools() {
      window.open("/schools", "_self");
    },
    routeKeys() {
      window.open("/keys", "_self");
    },
  }
  }
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800&family=Roboto&display=swap');

.navigation{
  width: 90%;
  font-family: inter, san-serif,serif;
  font-size: 1.15rem;
}

.navigationheader{
  width: 100%;
  font-weight: 600;
  padding-bottom: 5%;
  margin-bottom: 10%;
  border-bottom: black 1px solid;
}

.navigationitem{
  margin-bottom: 5%;
  cursor: pointer;
}

.navigationitemcurrent{
  font-weight: bold;
  cursor: auto !important;
  color: #5AC6CE;
}
.navigationitemcurrent :hover{
  font-size: 1.15rem !important;

}

.navigationitem :hover{
  font-weight: bold;
}

</style>
