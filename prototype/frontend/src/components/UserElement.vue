<template>
    <div class="box" @click="showFullUser">
        <h1>
            <div class="userData">
              <div class="lineItem">
                {{ userName }}
                {{ userLastName }}
              </div>
              <div class="lineItem">
                {{ userDetails[2] }}
              </div>
              <div class="lineItem">
                {{ userDetails[3] }}
              </div>
            </div><br>
            <span v-if="showDetails === true">
                <!--              <span v-if="role == admin || role == superadmin"></span>    -->
                <span v-if="edit === true">
                    <b>Vorname: </b><input type="text" :placeholder="userDetails[0]" class="input" required />
                    <b>Nachname: </b><input type="text" :placeholder="userDetails[1]" class="input" required />
                    <b>E-Mail: <input type="text" :placeholder="userDetails[2]" class="input" required /> </b>
                    <b>Organisation:</b>  {{ userDetails[2] }} <br>
                    <b>Role:</b>  {{ userDetails[3] }} <br>
                </span>
                <span v-else>
                    <td>
                        Email: {{ userDetails[0] }} <br>
                        Organisation: {{ userDetails[2] }} <br>
                        Role: {{ userDetails[3] }} <br>
                    </td>
                </span>
                <div class="buttonA">
                  <AppButton class="buttonUser" @click="editing" buttonText="Edit" />
                <span v-if="edit === true">
                <AppButton class="buttonUser" @click="update" buttonText="Update" />
                <AppButton class="buttonUser" @click="cancel" buttonText="Cancel" />
                </span>
                </div>
            </span>
        </h1>
    </div>
</template>

<script>
import AppButton from "./ButtonThing.vue"
export default {
    components: {
        AppButton,
    },
    props: {
        userName: {
            type: String,
            default: () => "Place",
        },
        userLastName: {
            type: String,
            default: () => "Holder"
        },
        userDetails: {
            type: Array,
            default: () => []
        },
    },
    data() {
        return {
            showDetails: false,
            edit: false,
            details: {},
        }
    },
    methods: {
        showFullUser() {
            if (this.edit === false) {
                this.showDetails = !this.showDetails
            }
        },
        editing() {
            this.edit = !this.edit
        },
        update() {
            this.edit = false
        },
        cancel() {
            this.edit = false
        }
    }
}
</script>


<style scoped>

.buttonUser{
  background-color: rgba(130,0,205,0.83);
  color: white;
  margin-right: 1rem;
}
.buttonUser:hover{
  background-color: rgba(130,0,205,0.83);
  color: white;
}

.buttonUser:active{
  color: white;
}
.userData{
  vertical-align: top;
  flex-direction: row;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  width: 55vw;
  flex-wrap: nowrap;
}

.lineItem{
}

.box {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 59vw;
    padding: 2rem;
    margin-top: 1%;
    margin-bottom: 1%;
    vertical-align: middle;
    cursor: pointer;

}
.buttonA {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
