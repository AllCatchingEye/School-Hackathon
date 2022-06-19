<template>
  <div class="navigation" v-if="isloaded">
    <div class="navigationheader">
      <p>Navigation</p>
    </div>
    <div class="navigationlist">
      <div class="navigationitem" :class="dashboardactive ? 'navigationitemcurrent' : 'navigationitem'">
        <router-link to="/dashboard">
        <p>Übersicht</p>
        </router-link>
      </div>
      <div class="navigationitem" :class="useractive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Admin' || this.role === 'Superadmin'">
        <router-link to="/user">
        <p>Benutzermanagement</p>
        </router-link>
      </div>
      <div class="navigationitem" :class="hackathonactive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Admin' || this.role === 'Teacher'">
        <router-link to="/hackathons">
        <p>Hackathonübersicht</p>
        </router-link>
      </div>
      <div class="navigationitem" :class="tokenactive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Admin' || this.role === 'Teacher'">
        <router-link to="/keys">
        <p>Token</p>
        </router-link>
      </div>
      <div class="navigationitem" :class="analyseactive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Admin' || this.role === 'Teacher'">
        <router-link to="/submissions">
        <p>Analyse</p>
        </router-link>
      </div>
      <div class="navigationitem" :class="schoolactive ? 'navigationitemcurrent' : 'navigationitem'" v-if="this.role === 'Superadmin'">
        <router-link to="/schools">
        <p>Schulmanagement</p>
        </router-link>
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
      analyseactive : false,
      schoolactive: false
    }},
  mounted() {
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
          this.role = response.data.roles.description;
        })
        .catch(() => {
          this.$router.push('/login');
        })
    },
    selectActive(){
      this.dashboardactive = this.currentpage === "dashboard";
      this.useractive = this.currentpage === "user";
      this.hackathonactive = this.currentpage === "hackathon";
      this.tokenactive = this.currentpage === "token";
      this.analyseactive = this.currentpage === "submissions";
      this.schoolactive = this.currentpage === "schools";
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

.navigationitemcurrent p{
  font-weight: bold;
  cursor: auto !important;
  color: #5AC6CE;
}
.navigationitemcurrent :hover{
  font-size: 1.15rem !important;

}

.navigationitem :hover{
  opacity:0.8;
  transition:.3;
}

p{
  color: black;
}

</style>
