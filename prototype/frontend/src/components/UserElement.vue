<template>
    <div class="box" @click="showFullUser">
        <h1>
            <b>
                {{ userName }}
                {{ userLastName }} </b><br>
            <span v-if="showDetails == true">
                <span v-if="edit == true">
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
                <AppButton @click="editing" buttonText="Edit" />
                <span v-if="edit == true">
                <AppButton @click="update" buttonText="Update" />
                <AppButton @click="cancel" buttonText="Cancel" />
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
            if (this.edit == false) {
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
.box {
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 1px color black;
    width: 500px;
    margin-top: 1%;
    vertical-align: middle;
    cursor: pointer;
}
.buttonA {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>