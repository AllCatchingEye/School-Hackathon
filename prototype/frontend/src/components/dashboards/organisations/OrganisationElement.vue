<template>
    <div class="box">
        <div>
            <div class="HackathonData">
                <div class="lineItem">
                    <span>
                        {{ OrganisationID }}
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ OrganisationName }}
                    </span>
                    <span class="HackathonNameList" v-else>
                        <input type="text" v-model="newName" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span class="HackathonNameList button-wrapper" v-if="edit === true">
                        <button class="button is-success is-rounded" @click="update">Update</button>
                        <button class="button is-danger is-rounded" @click="cancel">Cancel</button>
                    </span>
                    <span v-else>
                        <button class="button editbutton is-link is-rounded" @click="editing">Edit</button>
                        <button class="button is-danger is-rounded is-outlined" @click="deleting">Delete</button>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    props: {
        OrganisationName: {
            type: String,
            default: () => "Place",
        },
        OrganisationID: {
            type: String,
            default: () => "",
        },
    },
    data() {
        return {
            newName: this.OrganisationName,
            edit: false
        }
    },
    methods: {
        editing() {
            this.edit = !this.edit
        },
        update() {
            const path = "/api/organisation/" + this.OrganisationID + "/";
            const data = JSON.stringify({orgaid: this.OrganisationID, name: this.newName});

            axios.patch(path, data, {
                ithCredentials: true,
                headers: {
                 'Content-Type': 'application/json'
                }
            })
                .then((response) => {
                    console.log(response);
                    setTimeout(() => {location.reload();}, 100);
                })
                .catch((err) => {
                    console.log(err);
                    console.log(this.cookies)
                })
        },
        cancel() {
            this.edit = false
        },
        deleting() {
            const path = "/api/organisation/" + this.OrganisationID + "/";

            axios.delete(path, {
                withCredentials: true
            })
                .then((response) => {
                    console.log(response);
                    setTimeout(() => {location.reload();}, 100);
                })
                .catch((err) => {
                    console.log(err);
                    console.log(this.cookies)
                })
        }
    }
}
</script>


<style scoped>

.HackathonData {
  vertical-align: top;
  flex-direction: row;
  display: flex;
  align-items: center;
  justify-content: space-around;
  width: 55vw;
  height: auto;
  flex-wrap: nowrap;
}

.editbutton{
  background-color: #1ABC9C;
}

.editbutton:hover{
  background-color: #1ABC9C;
}
.button{
  border: white 2px solid;
}

.HackathonNameList{
  width: 100%;
  margin-right: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;

}

.lineItem {
  display: flex;
  text-align: center;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  height: auto;
  width:100%;


}

::-webkit-scrollbar {
  width: 5px;
  height: 5px;
}

::-webkit-scrollbar-track {
  background: white;
}


.button{
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.HackathonName .input{
  margin-right: 1rem;
}

.input{
  width: 10vw;
  margin-left: 1rem;
}
.box {
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 56vw;
    margin: 0.5rem 1%;
    vertical-align: middle;
    padding-top:0px;
    padding-bottom:0px;

}

</style>
