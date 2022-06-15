<template>
    <div v-if="userDeleted === false">
        <div class="box">
                    <div class="entry-wrapper">
                        <div class="data-wrapper">
                            <div class="entry">
                                <p v-if="edit === false">
                                    {{ userName }}

                                </p>
                                <p class="userNameList" v-else>
                                    <input v-model="firstname" type="text" class="input is-small"
                                        :placeholder="this.firstname" />
                                </p>
                            </div>
                        
                        <div class="entry">
                                <p v-if="edit === false">
                                    {{ userLastName }}

                                </p>
                                <p class="userNameList" v-else>
                                    <input v-model="name" type="text" class="input is-small"
                                        :placeholder="this.name" />
                                </p>
                            </div>

                            <div class="entry">
                                <p v-if="edit === false">
                                {{ this.email }}

                                </p>
                                <p class="userNameList" v-else>
                                    <input v-model="email" type="text" class="input is-small"
                                        :placeholder="this.email" />
                                </p>
                            </div>

                            <div class="entry">
                                <span v-if="edit === false">
                                 {{ organisation }}
                            </span>
                            <span class="UserNameList" v-else>
                                <div v-if="currentRole === 420 && isLoadedOrga === true">
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


                            <div class="entry">
                            <span v-if="edit === false">
                                {{ roleDescription }}
                            </span>
                            <span class="UserNameList" v-else>
                                <div v-if="currentRole >= 29">
                                    <div class="field">
                                        <div class="dropdown is-hoverable">
                                            <div class="dropdown-trigger">
                                                <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                                    <span> {{ roleDescription }} </span>
                                                    <span class="icon is-small">
                                                        <i class="fas fa-angle-down" aria-hidden="true"></i>
                                                    </span>
                                                </button>
                                            </div>
                                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                                <div class="dropdown-content">
                                                    <a v-for="rolle in roles" :key="rolle.roleid">
                                                        <a href="#" class="dropdown-item"
                                                            @click="changeRole(rolle.description, rolle.roleid)">
                                                            {{ rolle.description }}
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
                        
                        </div>
                        <div class="button-wrapper">
                            <div v-if="edit" class="lineItem">

                            <button  class="button is-success is-rounded" @click="update">Update</button>
                            <button class="button is-danger is-rounded" @click="cancel"
                                buttonText="Cancel">Cancel</button>
                           </div>
                        <div v-if="!edit" class="lineItem">
                            <button  class="button is-link is-rounded" @click="editing">Edit</button>                            
                             <button class="button is-danger is-rounded is-outlined" @click="deleteUser">
                                <span>Delete</span>
                                <span class="icon is-small">
                                    <i class="fas fa-times"></i>
                                </span>
                            </button>
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
            roleDescription: this.userDetails[2].description,
            error: false,
            message: '',
            toDelete: {},
            toUpdate: {},
            choosenOrgaID: this.userDetails[1].orgaid,
            choosenOrga: this.userDetails[1].name,
            userid: this.userDetails[3],
            roles: {},
            userDeleted: false,
            currentRole: 0,
        }
    },
    mounted() {
        this.getOrgaInfo();
        this.getRoleInfo();
        this.getCurrentRole();
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
            this.toUpdate = JSON.stringify({ email: this.email, name: this.name, firstname: this.firstname, role: this.role, organisation: this.choosenOrgaID });
            console.log(this.toUpdate);
            axios.patch(path, this.toUpdate, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            }).then(() => {
                this.editing()
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
            location.reload();
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
                    console.log(this.cookies);
                })
        },
        changeRole(name, id) {
            this.role = id;
            this.roleDescription = name;
        },
        getRoleInfo() {
            const path = '/api/role/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.roles = response.data;
                })
                .catch((err) => {
                    console.log(err);
                    console.log(this.cookies)
                })
        },
        getCurrentRole() {
            const path = '/api/role/own/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.currentRole = response.data.role;
                })
                .catch((err) => {
                    console.log(err);
                    console.log(this.cookies)
                })
        },
    }
}
</script>


<style  lang="scss" scoped>


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




.box {
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
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
