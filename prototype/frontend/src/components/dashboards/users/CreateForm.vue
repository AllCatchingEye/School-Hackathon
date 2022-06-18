<template>

<div class="modal delete-model">

    <div class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
        <p class="modal-card-title">Add User</p>
        <button class="delete" aria-label="close" @click="cancel"></button>
        </header>
        <section class="modal-card-body">
            <article class="message is-danger" v-if="Errormessage.length">
          <div class="message-header">
            <p>Error</p>
          </div>
          <div class="message-body">
            {{Errormessage}}
          </div>
      </article>
            <form class="add-item">
                <label for="name">Name</label>

                <input type="text" id="name" required="required" v-model="Data.name" />

                <label for="firstname">Vorname</label>
                <input type="text" id="firstname" required="required" v-model="Data.firstname" />

                <label for="email">E-mail</label>
                <input  type="email" id="email" required="required" v-model="Data.email" />

                <label v-if="Organisations.length"  for="organisation">Organisation</label>
                <select v-if="Organisations.length" class="select" required="required" v-model="Data.organisation">
                    <option selected disabled value="0">Choose Organisation</option>
                    <option v-for="organisation in Organisations"
                            :value="organisation.orgaid"
                            :key="organisation.orgaid">{{organisation.name}}</option>
                </select>

                <label for="role">Rolle</label>
                    <select class="select" required="required" v-model="Data.role">
                    <option selected disabled value="0">Choose Role</option>
                    <option v-for="role in Roles"
                            :value="role.roleid"
                            :key="role.roleid">{{role.description}}</option>
                </select>
            </form>
        </section>
        <footer class="modal-card-foot">
            <button class="button is-danger is-rounded" @click="cancel">Cancel</button>
            <button  class="button is-success is-rounded" @click="onSubmit">Add</button>
        </footer>
    </div>
</div>

</template>
<script>
import axios from 'axios';

export default {
    props: ['organisations','roles','currentRole'],
  data() {
    return {
    Data: {"name": "", "firstname":"", "email":"", "role":0, "organisation": 0},
    Organisations: this.organisations,
    Roles: this.roles,
    Errormessage: ""
    };
  },
  methods: {
    onError(message){
      this.Errormessage = message;
      setTimeout(() => this.Errormessage = "", 2000);

    },
    onSubmit() {
        const path = '/api/register/'
        const dataJson = JSON.stringify(this.Data);
        axios.post(path, dataJson, {
          headers: {
            'Content-Type': 'application/json'
          },
          withCredentials: true
        })
        .then((response) => {
            this.$emit("item-added", response.data.dataobj);
            this.$emit("success", response.data.message);
            this.$emit("close-pop-up");

        }).catch((err)=>{
            this.onError(err.response.data.message);
            // this.$emit("close-pop-up");
        })
    },
    cancel(){
        this.$emit("close-pop-up");
    }
  }
};

</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
.delete-model{
    display:flex;
    .add-item{
        display:flex;
        flex-direction:column;
        width:100%;
        margin:0% 0 2%;
        padding:0px 8%;
        label{
            font-family:'Roboto';
            font-weight:bold;
        }
        input,select{
            height:40px;
            font-size:1.2em;
            margin-bottom:5%;

        }
    }
  }


</style>
