<template>
<div class="data">
    <Sidebar :currentpage = "this.currentpage" ></Sidebar>
    <DashList></DashList>
  </div>
</template>

<script>
/* eslint-disable */
import { useCookies } from 'vue3-cookies';
import axios from 'axios';
import Sidebar from "../sidebar/sidebarDash";
import DashList from "./DashList";
axios.defaults.withCredentials = true;

export default {
  components:{Sidebar, DashList},
  data() {
    return {
      email: '',
      role: '',
      firstname: '',
      name: '',
      organisation: '',
      currentpage: 'dashboard',
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
    },}}
</script>


<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");

.data{
  display: grid;
  grid-template-columns: 30% 70%;
}

</style>
