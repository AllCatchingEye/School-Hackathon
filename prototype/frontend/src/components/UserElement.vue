<template>
    <div class="box">
        <h1>
            <div class="userData">
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ userName }}
                    </span>
                    <span v-else>
                        <input type="text" :placeholder="userName" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ userLastName }}
                    </span>
                    <span v-else>
                        <input type="text" :placeholder="userLastName" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ userDetails[0] }}
                    </span>
                    <span v-else>
                        <input type="text" :placeholder="userDetails[0]" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ userDetails[1] }}
                    </span>
                    <span v-else>
                        <input type="text" :placeholder="userDetails[1]" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === true">
                        <button class="button is-success is-rounded" @click="update">Update</button>
                        <button class="button is-danger is-rounded" @click="cancel" buttonText="Cancel">Cancel</button>
                    </span>
                    <span v-else>
                        <button class="button is-link is-rounded" @click="editing">Edit</button>
                    </span>
                </div>
            </div><br>
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
            edit: false
        }
    },
    methods: {
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

.userData {
    vertical-align: top;
    flex-direction: row;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    width: 55vw;
    flex-wrap: nowrap;
}

.lineItem {}

.box {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 59vw;
    padding: 2rem;
    margin-top: 1%;
    margin-bottom: 1%;
    vertical-align: middle;
}
</style>
