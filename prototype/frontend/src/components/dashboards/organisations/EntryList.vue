<template>

<div v-if="PopUp" >
        <create-form @item-added="addItem"
                  @close-pop-up="closePopUp" 
                  @error="onError"
                  @success="onSuccess"
                  :organisations="Organisations"
                  :roles="Roles"
></create-form>
</div>

<div v-if="DeleteModal" class="modal delete-model">
    <div class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
        <p class="modal-card-title">Really delete?</p>
        <button class="delete" aria-label="close" @click="cancelApproval()"></button>
        </header>
       
        <footer class="modal-card-foot">
        <button class="button is-danger" @click="deleteApproval()">Delete</button>
        <button class="button"  @click="cancelApproval()">Cancel</button>
        </footer>
    </div>
</div>

<div class="data">  
<sidebarDash :currentpage="this.currentpage"></sidebarDash>


<div class="outerBoxOverview">  
      <div class="headlineItems">
        <p>Organisation</p>
      </div>
    <Transition name="slide-fade">
       <article class="message is-danger" v-if="Errormessage.length">
          <div class="message-header">
            <p>Error</p>
          </div>
          <div class="message-body">
            {{Errormessage}}
          </div>
      </article>
    </Transition>
    <Transition name="slide-fade">
      <article class="message is-success" v-if="Successmessage.length">
                <div class="message-header">
                  <p>Success</p>
                </div>
                <div class="message-body">
                  {{Successmessage}}
                </div>
      </article>
</Transition>
      <div class="button-wrapper">
            <button class="add-item button is-success is-rounded" @click="changePopup()">Add Organisation</button>
      </div>

    <div class="scrollable-items">
          <ul>
          <li v-for="item in orderedItemsById" :key="item.orgaid">  
              <entry-item @update-item="updateItem" 
                          @item-delete-approve="openDeleteApproval" 
                          @delete-item="deleteItem"
                          @error="onError"
                          @success="onSuccess"
                          :deleteApproval="DeleteApprove"
                          :data="item"></entry-item>
          </li>
          </ul>
    </div>
  </div>
</div>
</template>


<script>
import axios from 'axios';
import CreateForm from './CreateForm.vue';
import EntryItem from './EntryItem.vue';
import sidebarDash from "../sidebar/sidebarDash";

export default{
components:{
    CreateForm,
    EntryItem,
    sidebarDash
},
 data() {
    return {
      Data: [],
      Roles: [],
      Organisations: [],
      accessAllowed: false,
      currentpage: "schools",
      PopUp: false,
      Errormessage: "",
      Successmessage: "",
      DeleteModal: false,
      DeleteApprove: 0      
    };
  },
computed: {
  orderedItemsById: function () {
    return [...this.Data].sort((a,b) => b.orgaid - a.orgaid);
  }
},
mounted() {
        this.getData();
    },
methods:{
    changePopup(){
      this.PopUp=true;
    },
    closePopUp(){
      this.PopUp=false;
    },
    cancelApproval(){
      this.DeleteModal = false;
      this.DeleteApprove = 0;
    },
    addItem(item){
      this.Data.push(item);
    },
    onSuccess(message){
      this.Errormessage = "";
      this.Successmessage = message;
      setTimeout(() => this.Successmessage = "", 2000);

    },
    onError(message){
      this.Successmessage = "";
      this.Errormessa = message;
      setTimeout(() => this.Errormessage = "", 2000);

    },
    updateItem(item){
      const itemIndex = this.Data.findIndex(x => x.orgaid == item.orgaid);
      this.Data[itemIndex] = item;
    },
    deleteItem(id){
      let itemIndex = this.Data.findIndex(x => x.orgaid == id);
      this.Data.splice(itemIndex,1);
      this.DeleteApprove = 0;
      this.DeleteModal = false;
    },
    openDeleteApproval(id){
        this.DeleteApprove = id;
        this.DeleteModal = true;            
    },
    deleteApproval(){
        this.DeleteApprove = true;
        this.DeleteModal = true;            

    },
    getData(){
        const path = '/api/organisation/'
        axios.get(path, {
            withCredentials:true
        })
        .then((response) => {
            this.accessAllowed = true;
            this.Data = response.data;
        }).catch((err)=>{
            if(err.response.status == 403) {
              this.$router.push({name:"Login", params: {message: "You have to be logged in"}});
            }else{
              this.onError(err.response.data.message);                          
            }                                      
        })
    }, 
}

}

</script>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.delete-model{
    display:flex;
  }
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

.headlineItems {
  width: 59vw;
  text-align: left;
  align-items: flex-start;
  margin-bottom: 2rem;
  margin-top: 2rem;
  padding-bottom: 1rem;
  border-bottom: rgba(109, 105, 114, 0.46) 1px solid;
}

.scrollable-items {
  overflow-x: hidden;
  height: 80%;
  width: 64vw;
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
.message{
  width:80%;
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
  width:84%;
text-align:right;
}

/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(0.5, 1, 1, 0.8);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(20px);
  opacity: 0;
}

</style>
