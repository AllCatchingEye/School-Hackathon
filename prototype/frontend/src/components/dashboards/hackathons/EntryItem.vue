<template>

        <div class="box">
                    <div class="entry-wrapper" v-if="!edit">
                        <div class="data-wrapper">                          
                            <div class="entry"><p>{{Data.title }}</p></div>
                            <div class="entry"><p>{{Data.description }}</p></div>
                            <div class="entry"><p>{{Data.slug }}</p></div>
                        </div>
                        <div class="lineItem buttons">
                            <div  class="editbutton is-link is-rounded" @click="editing">Edit</div>
                             <button class="button is-danger is-rounded is-outlined" @click="askDeleteItem">
                                <span>Delete</span>
                                <span class="icon is-small">
                                    <i class="fas fa-times"></i>
                                </span>
                            </button>
                        </div>


                    </div>
                    <div class="entry-wrapper" v-else>
                        <div class="data-wrapper fw">   
                            <div class="entry"><p>
                            <input type="text" class="input is-small" v-model="Data.title"  />
                            </p></div>
                            <div class="entry"><p>
                            <input type="text" class="input is-small" v-model="Data.description"/>
                            </p></div>
                            <div class="entry"><p>
                            <input type="text" class="input is-small" v-model="Data.slug"/>
                            </p></div>                          
                        </div>
                        <div v-if="!edit" class="lineItem buttons">
                            <div  class="editbutton is-link is-rounded" @click="edit">Edit</div>
                             <button class="button is-danger is-rounded is-outlined" @click="askDeleteItem">
                                <span>Delete</span>
                                <span class="icon is-small">
                                    <i class="fas fa-times"></i>
                                </span>
                            </button>
                        </div>
                    </div>

          <div class="newline">
            <div v-if="edit" class="buttonItemAction">
              <button class="button is-danger is-rounded is-outlined" @click="askDeleteItem">
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
 props: ['data',  'deleteApproval'],
 data() {
    return{
        edit:false,
        Data: this.data,
        WantDelete: -1
    }
  },
  methods: {
      editing() {
            this.edit = true;
            
        },
       cancel() {
            this.edit = false;
        },
         askDeleteItem() {       
            this.WantDelete = this.Data.hackathonid; 
            const id = this.Data.hackathonid;
            this.$emit('item-delete-approve', id);
        },
        deleteItem() {
            const path = '/api/hackathon/' + this.Data.hackathonid + '/';
            axios.delete(path, {
                headers: {
                    'Content-Type': 'application/json'
                    },
                withCredentials: true
            }).then((response) => {
                this.edit=false;
                this.$emit('delete-item', this.Data.hackathonid);
                this.$emit('success', response.data.message);  

            }).catch((err) => {
                this.$emit('error', err.response.data.message);
            });
        },

        update() {
            const path = '/api/hackathon/'  + this.Data.hackathonid +'/';
            const payload = {title: this.Data.title, 
                            description: this.Data.description, 
                            slug: this.Data.slug
                            }
            axios.patch(path, JSON.stringify(payload), {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            }).then((response) => {
                this.Data = response.data.dataobj;
                this.edit=false;
                this.$emit('update-item', this.Data);
                this.$emit('success', response.data.message);  

            }).catch((err)=>{             
                this.$emit('error', err.response.data.message);  
            }
        )     
    }
  },
    watch: {
        deleteApproval(newVal, oldVal) {     
            if(this.WantDelete == oldVal && newVal === true){
                this.deleteItem();
            }
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
        &.fw{
            width:100%;
        }
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
.buttonItem {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
    margin-right: 1rem;
}

.buttonItem:hover {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
}

.buttonItem:active {
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

.buttonItemAction{
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

select {
  /* Reset Select */
  appearance: none;
  outline: 0;
  border: 0;
  box-shadow: none;
  /* Personalize */
  flex: 1;
  padding: 0 1em;
  
  background-color: none;
  
  background-image: none;
  width:100%;
  cursor: pointer;
}
/* Remove IE arrow */
select::-ms-expand {
  display: none;
}
/* Custom Select wrapper */
.select {
  position: relative;
  display: flex;
  border-radius: .25em;
  overflow: hidden;
}
/* Arrow */
.select::after {
  content: '\25BC';
  position: absolute;
  top: 0;
  right: 0;
  padding: 1em;
  background-color: #34495e;
  transition: .25s all ease;
  pointer-events: none;
}
/* Transition */
.select:hover::after {
  color: #f39c12;
}

a {
  font-weight: bold;
  color: var(--gray);
  text-decoration: none;
  padding: .25em;
  border-radius: .25em;
  background: white;
}
</style>
