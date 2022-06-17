<template>

<div class="wrapper">
<div class="inner-wrapper">

<h1>Add User</h1>
<form class="add-user" @submit.prevent="onSubmit">
    <label for="name">
        Name
    </label>
    <input type="text" id="name" required="required" v-model="User['name']" />
    <label for="firstname">
        Vorname
    </label>
    <input type="text" id="firstname" required="required" v-model="User['firstname']" />
    <label for="email">

        E-mail
    </label>
    <input  type="email" id="email" required="required" v-model="User['email']" />
      <label v-if="currentRole == 420"  for="organisation">
        Organisation
    </label>
    <select v-if="currentRole == 420" class="select" required="required" v-model="User.organisation">
        <option v-for="organisation in Organisations" :value="organisation.orgaid" :key="organisation.orgaid">{{organisation.name}}</option>
    </select>  

  <label for="orgroleanisation">
        Rolle
    </label>
    <select class="select" required="required" v-model="User.role">
    <option v-for="role in Roles" :value="role.roleid" :key="role.roleid">{{role.description}}</option>
    </select> 

<div class="button-wrapper">
     <button class="button is-danger is-rounded" @click="cancel">Cancel</button>

    <button  class="button is-success is-rounded" type="submit">Add</button>
  </div>
  </form>
  </div>
  </div>
</template>
<script>
export default {
    props: ['organisations','roles','currentRole'],
  data() {
    return {
    User: {"name": "", "firstname":"", "email":"", "role":12, "organisation": 0},
    Organisations: this.organisations,
    Roles: this.roles


    };
  },
  methods: {
    onSubmit() {
        this.$emit("user-added", this.User);

    },
  cancel(){
        this.$emit("close-pop-up");

  }
  }
   
};

</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.wrapper{
    position:absolute;
    width:100vw;
    height:100vh;
    z-index:10;

    display:flex;
    justify-content:center;
    align-items:center;
    h1{
        position:absolute;
        top:0%;
        padding:5% 0% 3%;
            display:flex;
    justify-content:center;
    align-items:center;
    background:#9fe3d7;
        font-size:2em;
        font-weight:bold;
        width:100%;
        color:white;
    }
    .inner-wrapper{
        box-shadow: 0 0.5em 1em -0.125em rgb(68, 61, 61), 0 0 0 1px rgba(0, 0, 0, 0);
        width:70vh;
        height:70vw;
        background:white;
        position:relative;
         display:flex;
        justify-content:center;
        max-height:750px;
        min-height:700px;
            .add-user{
                margin-top:15%;
                display:flex;
                flex-direction:column;
                width:60%;

                label{
                    margin-top:10%;
                    font-family:'Roboto';
                    font-weight:bold;
                }
                input,select{
                    height:40px;
                    font-size:1.2em;
                }
            }
    .button-wrapper{
        position:absolute;
        bottom:10px;
        right:20%;
        button{
            &:not(:first-child){
                margin-left:30px;
            }
        }
    }

}

}
</style>