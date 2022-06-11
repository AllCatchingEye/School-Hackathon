<template>
  <div class="PopupOuter">
    <div class="PopupInner">
      <div class="IconApprove" v-if="displayApproved">
        <i class="fa-solid fa-check"></i>
      </div>
      <div class="IconApprove" v-if="displayDisapproved">
        <i class="fa-solid fa-xmark"></i>
      </div>
      <div v-if="displayQuestions" class="HeaderPopup">
        <p>Nutzer anlegen</p>
      </div>
      <div v-if="displayQuestions" class="BodyPopup">
        <div class="row">
          <div class="PopupQuestion">
              <div class="PopupInput">
                <input v-model="firstname" class="input is-medium" type="text" required/>
                <label>Vorname</label>
              </div>
            </div>
            <div class="PopupQuestion">
              <div class="PopupInput">
                <input v-model="name" class="input is-medium" type="text" required />
                <label>Nachname</label>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="PopupQuestion">
              <div class="PopupInput">
                <input v-model="email" class="input is-medium" type="email" required />
                <label>Email</label>
              </div>
            </div>
            <div class="PopupQuestion"  v-if="isLoadedRole === true">
              <div class="PopupInput">
                <div class="dropdown is-hoverable">
                  <div class="dropdown-trigger">
                    <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                      <span> {{ choosenRole }} </span>
                      <span class="icon is-small">
                            <i class="fas fa-angle-down" aria-hidden="true"></i>
                        </span>
                    </button>
                  </div>
                  <div class="dropdown-menu" id="dropdown-menu" role="menu">
                    <div class="dropdown-content">
                      <a v-for="rolle in roles" :key="rolle.roleid">
                        <a href="#" class="dropdown-item" @click="changeRole(rolle.description, rolle.roleid)">
                          {{ rolle.description }}
                        </a>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row" v-if="userRole === 420 && isLoadedOrga === true">
            <div class="PopupQuestion">
              <div class="PopupInput">
                <label class="label">Organisation</label>
                  <div class="dropdown is-hoverable">
                    <div class="dropdown-trigger">
                      <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                        <span> {{ choosenOrga }} </span>
                        <span class="icon is-small">
                              <i class="fas fa-angle-down" aria-hidden="true"></i>
                          </span>
                      </button>
                    </div>
                    <div class="dropdown-menu" id="dropdown-menu" role="menu">
                      <div class="dropdown-content">
                        <a v-for="organisation in orgas" :key="organisation.orgaid">
                          <a href="#" class="dropdown-item"
                             @click="changeOrga(organisation.name, organisation.orgaid)">
                            {{ organisation.name }}
                          </a>
                        </a>
                      </div>
                    </div>
                  </div>
              </div>
            </div>
            <div class="PopupQuestion">
              <div class="PopupInput">
              </div>
            </div>
          </div>
        </div>
        <div v-if="displayQuestions" class="PopupFooter">
          <div class="PopupFooterButton" @click="reload()">
            <PopupButtonDisapprove></PopupButtonDisapprove>
          </div>
          <div class="PopupFooterButton" @click="addNewUser()">
            <PopupButtonApprove></PopupButtonApprove>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import PopupButtonApprove from "../PopupButtonApprove";
import PopupButtonDisapprove from "../PopupButtonDisapprove";
import { useCookies } from 'vue3-cookies';
axios.defaults.withCredentials = true;

export default {
  name: "PopupAddUser",
  components: {PopupButtonDisapprove, PopupButtonApprove},
  setup() {
    const { cookies } = useCookies();
    return { cookies };
  },
  data() {
    return {
      isLoadedRole: false,
      isLoadedOrga: false,
      displayQuestions: true,
      displayApproved: false,
      displayDisapproved: false,
      choosenRole: 'none',
      role: 0,
      name: '',
      firstname: '',
      organisation: 0,
      roles: {},
      userRole: 0,
      error: false,
      message: '',
      choosenOrga: 'none',
      orgas: {},
      responseCode: 0,
    }
  },
  mounted() {
    this.getRoleInfo();
    this.getCurrentRole();
    this.getOrgaID();
    this.getOrgaInfo();
    this.getUserInfo();
  },
  methods: {
    getUserInfo() {
      const path = '/api/user/own/'
      axios.get(path, {
        withCredentials: true
      }).then((response) => {
        this.organisation = response.data.organisations.orgaid;
      })
        .catch((e) => {
          console.log(e);
        })
    },
    changeRole(text, id) {
      this.choosenRole = text;
      this.role = id;
    },
    changeOrga(text, id) {
      this.choosenOrga = text;
      this.organisation = id;
    },
    getRoleInfo() {
      const path = '/api/role/'
      axios.get(path, {
        withCredentials: true
      })
        .then((response) => {
          this.roles = response.data;
          this.isLoadedRole = true;
        })
        .catch((err) => {
          console.log(err);
          console.log(this.cookies)
        })
    },
    getCurrentRole() {
      const path = '/api/role/own/'
      axios.get(path, {
        withCredentials: true
      })
        .then((response) => {
          this.userRole = response.data.role;
        })
        .catch((err) => {
          console.log(err);
          console.log(this.cookies)
        })
    },
    getOrgaID() {
      const path = '/api/organisation/own/'
      axios.get(path, {
        withCredentials: true
      })
        .then((response) => {
          this.organisation = response.orgaid;
        })
        .catch((err) => {
          console.log(err);
          this.getUserInfo();
        })
    },
    getOrgaInfo() {
      const path = '/api/organisation/'
      axios.get(path, {
        withCredentials: true
      })
        .then((response) => {
          this.isLoadedOrga = true;
          this.orgas = response.data;
        })
        .catch((err) => {
          console.log(err);
          console.log(this.cookies)
        })
    },
    addNewUser() {
      const path = '/api/register/'
      console.log(this.organisation);
      this.user = JSON.stringify({ email: this.email, name: this.name, firstname: this.firstname, role: this.role, organisation: this.organisation });
      if (this.organisation === 0 || this.name === '' || this.firstname === '' || this.role === 0) {
        alert('Please provide all the information needed');
      } else {

        //location.reload();
        axios.post(path, this.user, {
          headers: {
            'Content-Type': 'application/json'
          },
          withCredentials: true
        })
        .then(() => {
          this.displayQuestions = false;
          this.displayApproved = true;
          setTimeout(() => {location.reload();}, 1000);
        }).catch(() => {
          this.displayQuestions = false;
          this.displayDisapproved = true;
          setTimeout(() => {location.reload();}, 1000000);
        });}
    },
    reload(){
      location.reload();
    }
}
}

</script>

<style scoped>

@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");


.dropdown{
  position: relative;
  height: 100%;
  width:100%;
}
.dropdown-trigger{
  height: 100%;
  width:100%;
}
.dropdown-menu{
  height: 100%;
  width:100%;
}

.button{
  font-size: 1.25rem;
  color: white;
  display: flex;
  align-content: flex-start;
  height: 100%;
  width: 100%;
  justify-content: space-around;
  font-family: 'Open Sans', san-serif, serif;
  border: 0.2rem solid #0c9bfa;
  padding-top: 1rem;
  padding-bottom: 1rem;
  background: none;
  border-radius: 0.5rem;
}


.PopupOuter{
  position: fixed;
  width:100vw;
  height: 100vh;
  background-color: #ffffff57;
  backdrop-filter: blur(30px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
}

.IconApprove{
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.PopupInner{
  position: relative;
  background-color: #000a38;
  width: 80%;
  height: 80%;
  border-radius: 40px;
  box-shadow: 11px 11px 23px 9px rgba(0,12,109,0.33);
}

.PopupFooterButton{
  cursor: pointer;
  height: 70%;
  width: 30%;
}

.row{
  margin-top: 5%;
  width: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: space-around;
}

.fa-solid{
  color: white;
  font-size: 50vh;
}

.HeaderPopup{
  width: 100%;
  height: 15%;
  padding-left: 5%;
  color: white;
  font-size: 40px;
  font-weight: normal;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.BodyPopup{
  width: 100%;
  height: 75%;
  padding-left: 5%;
  padding-right: 5%;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  flex-direction: column;
}

.PopupFooter{
  height: 10%;
  width: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: space-around;
}


.PopupQuestion{
  height: 5%;
  width: 30%;
}

input{
  width: 100%;
  height: 100%;
  font-family:'Open Sans', san-serif, serif;
  border: .2rem solid #0c9bfa;
  font-size:1.5rem;
  padding: 1rem 1rem;
  color:#fff;
  border-radius:.5rem;
  background: none;
}

input:focus{
  outline:none;
}

.PopupInput{
  position:relative;
}

label{
  position:absolute;
  top:50%;
  left:2rem;
  transform: translateY(-50%);
  font-size: 1.5rem;
  background:#000a38;
  color:#fff !important;
  transition: all .25s linear;
  pointer-events:none;
}

input:focus ~ label,
input:not(:focus):valid ~ label{
  transform: translateY(50%);
  top:-40%;
  left:1rem;
  font-size:1.25rem;
  padding: 0 .3rem;
}

</style>
