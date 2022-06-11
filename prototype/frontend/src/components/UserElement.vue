<template>
    <div class="box">
        <div>
            <div class="userData">
                <div class="lineItem">
                    <span class="userNameList" v-if="edit === false">
                        <div class="UserNameListTag">
                            {{ userName }}
                        </div>
                        <div class="UserNameListTag">
                            {{ userLastName }}
                        </div>
                    </span>
                    <span class="userNameList" v-else>
                        <input v-model="firstname" type="text" class="input is-small" :placeholder="this.firstname" />
                        <input v-model="name" type="text" class="input is-small" :placeholder="this.name" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ userDetails[0] }}
                    </span>
                    <div class="UserNameList" v-else>
                        <div class="control has-icons-left has-icons-right">
                            <div class="control">
                                <input v-model="email" class="input is-small" type="email" :placeholder="this.email">
                                <span class="icon is-left">
                                    <i class="fas fa-envelope"></i>
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="lineItem">
                        <span v-if="edit === false">
                            {{ userDetails[1].name }}
                        </span>
                        <span class="UserNameList" v-else>
                            <div v-if="role === 420 && isLoadedOrga === true">
                                <div class="field">
                                    <div class="dropdown is-hoverable">
                                        <div class="dropdown-trigger">
                                            <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                                <span> {{ choosenOrga }} </span>
                                                <span class="icon is-small">
                                                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                                                </span>
                                            </button>
                                        </div>
                                        <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                            <div class="dropdown-content">
                                                <a v-for="organisation in orgas" :key="organisation.orgaid">
                                                    <a href="#" class="dropdown-item"
                                                        @click="changeOrga(organisation.name, organisation.orgaid)">
                                                        {{ organisation.name }}
                                                    </a>
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-else>
                                <input type="text" class="input is-small" :value="organisation" disabled />
                            </div>
                        </span>

                    </div>
                    <div class="lineItem">
                        <span class="UserNameList button-wrapper" v-if="edit === true">
                            <button class="button is-success is-rounded" @click="update">Update</button>
                            <button class="button is-danger is-rounded" @click="cancel"
                                buttonText="Cancel">Cancel</button>
                            <button class="button is-danger is-rounded is-outlined" @click="deleteUser">
                                <span>Delete</span>
                                <span class="icon is-small">
                                    <i class="fas fa-times"></i>
                                </span>
                            </button>
                        </span>
                        <span v-else>
                            <button class="button is-link is-rounded" @click="editing">Edit</button>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import { useCookies } from 'vue3-cookies';

export default {
    setup() {
        const { cookies } = useCookies();
        return { cookies };
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
            edit: false,
            isLoadedOrga: false,
            name: this.userLastName,
            firstname: this.userName,
            email: this.userDetails[0],
            organisation: this.userDetails[1].name,
            role: this.userDetails[2].roleid,
            error: false,
            message: '',
            toDelete: {},
            toUpdate: {},
            choosenOrgaID: this.userDetails[1].orgaid,
            choosenOrga: this.userDetails[1].name,
            userid: this.userDetails[3],
        }
    },
    mounted() {
        this.getOrgaInfo();
    },
    methods: {
        editing() {
            this.edit = !this.edit
        },
        changeOrga(name, id) {
            this.organisation = name;
            this.choosenOrgaID = id;
            this.choosenOrga = name;
        },
        update() {
            const path = '/api/user/' + this.userid + '/';
            this.toUpdate = JSON.stringify({ email: this.email, name: this.name, firstname: this.firstname, role: this.role, organisation: this.orgaid });
            axios.patch(path, this.toUpdate, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
                .catch((err) => {
                    console.log(err);
                    error = true;
                    message = err.response.data.message;
                });
        },
        cancel() {
            this.edit = false
        },
        deleteUser() {
            const path = '/api/user/' + this.userid + '/';
            //this.toDelete = JSON.stringify({ email: this.userInfo[0] });
            axios.delete(path, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
                .catch((err) => {
                    console.log(err);
                    error = true;
                    message = err.response.data.message;
                });
        },
        getOrgaInfo() {
            const path = '/api/organisation/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.isLoadedOrga = true;
                    this.orgas = response.data;
                })
                .catch((err) => {
                    console.log(err);
                    console.log(this.cookies)
                })
        },
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

.UserNameListTag {
    margin-right: 2rem;
    margin-left: 2rem;
}

.userData {
    vertical-align: top;
    flex-direction: row;
    display: grid;
    align-items: center;
    grid-template-columns: 25% 10% 10% 10%;
    justify-content: space-around;
    width: 55vw;
    flex-wrap: nowrap;
}

.userNameList {
    width: 100%;
    margin-right: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;

}

.lineItem {
    margin-right: 1rem;
}

.button {
    margin-top: 1rem;
    margin-bottom: 1rem;
}

.userName .input {
    margin-right: 1rem;
}

.input {
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
    padding-top: 0px;
    padding-bottom: 0px;

}
</style>
