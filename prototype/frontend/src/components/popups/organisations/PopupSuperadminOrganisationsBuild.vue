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
        <p>Organisation anlegen</p>
      </div>
      <div v-if="displayQuestions" class="BodyPopup">
        <div class="row">
          <div class="PopupQuestion">
              <div class="PopupInput">
                <input v-model="name" type="text" autocomplete="off" required />
                <label>Name</label>
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
          <div class="PopupFooterButton" @click="addHackathon()">
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
  name: "PopupSuperadminOrganisationBuild",
  components: {PopupButtonDisapprove, PopupButtonApprove},
  setup() {
    const { cookies } = useCookies();
    return { cookies };
  },
  data() {
    return {
      orgaid: '',
      name: '',
      result: '',
      displayQuestions: true,
      displayApproved: false,
      displayDisapproved: false
    }
  },

  methods: {
    async addHackathon(){
      const path = '/api/organisation/';
      this.test = JSON.stringify({name: this.name});
      await axios.post(path,this.test, {
        withCredentials: true,
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(() => {
          this.displayQuestions = false;
          this.displayApproved = true;
          setTimeout(() => {location.reload();}, 1000);
        }).catch(() => {
          this.displayQuestions = false;
          this.displayDisapproved = true;
          setTimeout(() => {location.reload();}, 1000);
        });
    },
    reload(){
      location.reload();
    }
}
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800&family=Roboto&display=swap');
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");


.dropdown{
  position: relative;
  height: 100%;
  width:100%;
}
.dropdown-trigger{
  height: 100%;
  width:100%;
  border-radius: 1rem;
}
.dropdown-menu{
  height: 100%;
  width:100%;
}



.button{
  font-size: 1rem;
  display: flex;
  align-content: flex-start;
  height: 100%;
  width: 100%;
  justify-content: space-around;
  font-family: inter, san-serif,serif;
  border: 0.2rem solid #D9D9D9;
  padding-top: 1rem;
  padding-bottom: 1rem;
  background: none;
  border-radius: 1rem;
}


.PopupOuter{
  position: fixed;
  width:100vw;
  height: 100vh;
  background-color: #00000078;
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
  background-color: #FFFFFF;
  width: 60%;
  height: 80%;
  border-radius: 40px;
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
  font-size: 50vh;
}

.HeaderPopup{
  font-family: inter, san-serif,serif;
  width: 100%;
  height: 15%;
  padding-left: 5%;
  font-size: 25px;
  font-weight: bold;
  color: black;
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
  height: 15%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  background-color: #F0F0F0;
  border-bottom-left-radius: 40px;
  border-bottom-right-radius: 40px;
  padding-right: 5%;
}


.PopupQuestion{
  height: 5%;
  width: 30%;
}

input{
  width: 100%;
  height: 100%;
  font-family:'Open Sans', san-serif, serif;
  border: .2rem solid #D9D9D9;
  font-size:1rem;
  padding: 1rem 1rem;
  border-radius: 1rem;
  background: none;
  outline: none;
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
  font-size: 1rem;
  background:#FFFFFF;
  transition: all .25s linear;
  pointer-events:none;
}

input:focus ~ label,
input:not(:focus):valid ~ label{
  transform: translateY(50%);
  top:-45%;
  left:1rem;
  font-size:1.25rem;
  padding: 0 .3rem;
  outline: none;
}

</style>
