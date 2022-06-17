<template>
        <div class="box">
                    <div class="entry-wrapper" v-if="!edit">
                        <div class="data-wrapper">                          
                            <div class="entry"><p>{{ User.name }}</p></div>
                            <div class="entry"><p>{{ User.firstname }}</p></div>
                            <div class="entry"><p>{{ User.email }}</p></div>
                            <div class="entry"><p>{{ User.organisations.name }}</p></div>
                            <div class="entry"><p>{{ User.roles.description }}</p></div>
                        </div>
                        <div class="lineItem buttons">
                            <div  class="editbutton is-link is-rounded" @click="editing">Edit</div>
                             <button class="button is-danger is-rounded is-outlined" @click="deleteUser">
                                <span>Delete</span>
                                <span class="icon is-small">
                                    <i class="fas fa-times"></i>
                                </span>
                            </button>
                        </div>
                    </div>
                    <div class="entry-wrapper" v-else>
                        <div class="data-wrapper">   
                            <div class="entry"><p>
                            <input type="text" class="input is-small" v-model="User.name"  />
                            </p></div>
                            <div class="entry"><p>
                            <input type="text" class="input is-small" v-model="User.firstname"/>
                            </p></div>
                            <div class="entry"><p>
                            <input type="text" class="input is-small" v-model="User.email"/>
                            </p></div>
                            <div class="entry">
                                <select v-model="User.organisations.orgaid">
                                        <option v-for="organisation in Organisations" :value="organisation.orgaid" :key="organisation.orgaid">{{organisation.name}}</option>
                                </select>                                
                            </div>
                            <div class="entry">
                                <select v-model="User.roles.roleid">
                                        <option v-for="role in Roles" :value="role.roleid" :key="role.roleid">{{role.description}}</option>
                                </select>                                
                            </div>                             
                        </div>
                        <div v-if="!edit" class="lineItem buttons">
                            <div  class="editbutton is-link is-rounded" @click="edit">Edit</div>
                             <button class="button is-danger is-rounded is-outlined" @click="deleteUser">
                                <span>Delete</span>
                                <span class="icon is-small">
                                    <i class="fas fa-times"></i>
                                </span>
                            </button>
                        </div>
                    </div>

          <div class="newline">
            <div v-if="edit" class="buttonUserAction">
              <button class="button is-danger is-rounded is-outlined" @click="deleteUser">
                <span>Delete</span>
                <span class="icon is-small"><i class="fas fa-times"></i></span>
              </button>
              <button class="button is-danger is-rounded" @click="cancel">Cancel</button>
              <button  class="button is-success is-rounded" @click="update">Update</button>

            </div>
          </div>
        </div>

</template>
<script>
import axios from 'axios';
export default {
 props: ['organisations','roles', 'user'],
 data() {
    return{
        edit:false,
        User: this.user,
        Roles: this.roles,
        Organisations: this.organisations
    }
  },
  methods: {
      editing() {
            this.edit = true;
        },
       cancel() {
            this.edit = false;
        },
         deleteUser() {
            const path = '/api/user/' + this.User.userid + '/';
            axios.delete(path, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            }).then(() => {
                this.edit=false;
                this.$emit('user-delete', this.User.userid);
            }).catch((err) => {
                console.log(err);
                    // error = true;
                    // message = err.response.data.message;
                });
        },
        update() {
            const path = '/api/user/'  + this.User.userid +'/';
            const payload = {name: this.User.name, 
                            firstname: this.User.firstname, 
                            organisation: this.User.organisations.orgaid,
                            role: this.User.roles.roleid,
                            email: this.User.email
                            }
            axios.patch(path, JSON.stringify(payload), {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            }).then((response) => {
                this.User = response.data.dataobj;
                this.edit=false;
                this.$emit('user-updated', this.User);
            }).catch((err)=>{             
            switch(err.response.status) {
                case 409:
                    console.log("This Emails exists")
                    break;
                case 500:
                    // Error message
                    break;
                default:
                    console.log("An unexpected Error occurred.")
                }        
            }
        )
        
    }

  }
}


</script>


<style  lang="scss" scoped>
.buttons{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content: space-between;
  flex-wrap: nowrap;
}

.editbutton{
  margin-right: 3%;
  background-color: #1ABC9C;
  border-color: #dbdbdb;
  border-width: 1px;
  border-radius: 30px;
  color: white;
  cursor: pointer;
  justify-content: center;
  padding-bottom: calc(0.5em - 1px);
  padding-left: 1em;
  padding-right: 1em;
  padding-top: calc(0.5em - 1px);
  text-align: center;
  white-space: nowrap;
}
.entry-wrapper{
    width:100%;
    display:flex;
    .data-wrapper{
        width:80%;
        display:grid;
        grid-template-columns: 1fr 1fr 1.5fr 1fr 1fr;
        height:80px;
        align-items:center;
        grid-column-gap:10px;
    .entry{
            input{
                font-size:1em;
            }
        }

    }
    .button-wrapper{
        width:20%;
    }

}
.buttonUser {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
    margin-right: 1rem;
}

.buttonUser:hover {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
}

.buttonUser:active {
    color: white;
}


.lineItem {
    margin-right: 1rem;
}

.button {
    margin-top: 1rem;
    margin-bottom: 1rem;
}

.newline{
  width:100%;
  height: 100%;
}

.buttonUserAction{
  display: flex;
  justify-content: space-around;
}

.box {
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin: 0.5rem 1%;
    vertical-align: middle;
    padding-top: 0px;
    padding-bottom: 0px;

}

.dropdown{
                width:100%;

    .dropdown-trigger{
            width:100%;

.button{
            width:100%;
        }

    }

}
</style>
