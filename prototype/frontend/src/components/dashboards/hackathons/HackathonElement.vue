<template>
    <div class="box">
        <div>
            <div class="HackathonData">
                <div class="lineItem">
                    <span  v-if="edit === false">
                        {{ HackathonName }}
                    </span>
                    <span class="HackathonNameList" v-else>
                      <input type="text" v-model="newName" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ HackathonDetails[0] }}
                    </span>
                    <span class="HackathonNameList" v-else>
                        <input type="text" v-model="newSlug" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ HackathonDetails[1] }}
                    </span>
                    <span class="HackathonNameList" v-else>
                        <input type="text" v-model="newDesc" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span class="HackathonNameList button-wrapper" v-if="edit === true">
                        <button class="button is-success is-rounded" @click="update">Update</button>
                        <button class="button is-danger is-rounded" @click="cancel" buttonText="Cancel">Cancel</button>
                    </span>
                    <span v-else>
                        <button class="button is-link is-rounded" @click="editing">Edit</button>
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
        HackathonID: {
            type: String,
            default: () => "",
        },
        HackathonName: {
            type: String,
            default: () => "Place",
        },
        HackathonDetails: {
            type: Array,
            default: () => []
        },
    },
    data() {
        return {
            newName: this.HackathonName,
            newSlug: this.HackathonDetails[0],
            newDesc: this.HackathonDetails[1],
            edit: false
        }
    },
    methods: {
        editing() {
            this.edit = !this.edit
        },
        update() {
            const path = "/api/hackathon/" + this.HackathonID + "/";
            const data = JSON.stringify({hackathonid: this.HackathonID, title: this.newName, 
                                        slug: this.newSlug, description: this.newDesc});
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
        }
    }
}
</script>


<style scoped>
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

.HackathonNameListTag{
  margin-right: 2rem;
  margin-left: 2rem;
}

.HackathonData {
  vertical-align: top;
  flex-direction: row;
  display: grid;
  align-items: center;
  grid-template-columns: 25% 10% 10% 10%;
  justify-content: space-around;
  width: 55vw;
  height: auto;
  flex-wrap: nowrap;
}

.HackathonNameList{
  width: 100%;
  margin-right: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;

}

.lineItem {
  margin-right: 1rem;
  height: auto;
  width: 100%;


}

::-webkit-scrollbar {
  width: 5px;
  height: 5px;
}

::-webkit-scrollbar-track {
  background: white;
}

::-webkit-scrollbar-thumb {
  background-color: #0D2385;
  border-radius: 10px;
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
