<template>
  <div class="outerBoxOverview">
    <div class="header">
      <div class="innerheader">
      <h1>Hi {{ this.firstname }}, <br> was möchtest du tun?</h1>
      </div>
    </div>
    <div class="tiles-wrapper">
      <div class="ctile" v-if="this.role === 'Admin' || this.role === 'Superadmin'">
        <router-link to="/user-overview">
          <h2>Benutzermanagement</h2>
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
      <div  class="ctile" v-if="this.role === 'Teacher' || this.role === 'Admin'">
        <router-link to="/keys">

          <h2>Schlüsselmanagement</h2>
          <i class="fa-solid fa-angle-right"></i>
        </router-link>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
axios.defaults.withCredentials = true;

export default {
  name: "DashList",
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
          console.log()
        })
        .catch((e) => {
          console.log(e);
        })
    },
  }

}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");
$green :#37b1c5;

.header{
  margin-left: 5%;
  display: flex;
  align-items: center;
  align-content: center;
  margin-top: 5%;
  margin-bottom: 5%;
  width: 100%;
  justify-content: center;
}
.innerheader{
  width: 75%;
  display: flex;
  align-items:center;
  align-content:center;
}
h1{
  text-align: center;
  font-family: "Open Sans", sans-serif;
  font-weight: bold;
  font-size: 3.5rem;
}

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
      h2{
      color:white;
      }
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
  font-family: 'Open Sans', sans-serif;
  font-weight: 100;
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
.lineItem{
  padding-left: 1rem;
  flex-direction: row;
  display: flex;
  justify-content: space-around;
}

.lineItem p{
  margin-right: 2rem;
}

</style>
