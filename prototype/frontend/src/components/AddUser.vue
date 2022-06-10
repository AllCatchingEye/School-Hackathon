<template>
    <div v-if="isLoadedRole === true">
        <div class="field">
            <div class="control has-icons-left has-icons-right">
                <label class="label">Vorname</label>
                <div class="control">
                    <input v-model="firstname" class="input is-medium" type="text" placeholder="e.g. Merlinöse"
                        required>
                    <span class="icon is-left">
                        <i class="fas fa-solid fa-user"></i>
                    </span>
                </div>
            </div>
        </div>
    </div>
    <div class="field">
        <div class="control has-icons-left has-icons-right">
            <label class="label">Nachname</label>
            <div class="control">
                <input v-model="name" class="input is-medium" type="text" placeholder="e.g. Scammerino" required>
                <span class="icon is-left">
                    <i class="fas fa-solid fa-user"></i>
                </span>
            </div>
        </div>
    </div>
    <div class="field">
        <div class="control has-icons-left has-icons-right">
            <label class="label">Email</label>
            <div class="control">
                <input v-model="email" class="input is-medium" type="email" placeholder="e.g. test@mail.de" required>
                <span class="icon is-left">
                    <i class="fas fa-envelope"></i>
                </span>
            </div>
        </div>
    </div>
    <div v-if="isLoadedRole === true">
        <div class="field">
            <label class="label">Rolle</label>
            <div class="dropdown is-hoverable">
                <div class="dropdown-trigger">
                    <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                        <span> {{ choosenRole }} </span>
                        <span class="icon is-small">
                            <i class="fas fa-angle-down" aria-hidden="true"></i>
                        </span>
                    </button>
                </div>
                <div class="dropdown-menu" id="dropdown-menu" role="menu">
                    <div class="dropdown-content">
                        <a v-for="rolle in roles" :key="rolle.roleid">
                            <a href="#" class="dropdown-item" @click="changeRole(rolle.description, rolle.roleid)">
                                {{ rolle.description }}
                            </a>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-if="userRole == 420 && isLoadedOrga === true">
        <div class="field">
            <label class="label">Organisation</label>
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
                            <a href="#" class="dropdown-item" @click="changeOrga(organisation.name, organisation.orgaid)">
                                {{ organisation.name }}
                            </a>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div>
        <button class="button is-success is-rounded" @click="addNewUser">Submit</button>
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
    data() {
        return {
            isLoadedRole: false,
            isLoadedOrga: false,
            choosenRole: 'none',
            role: 0,
            name: '',
            firstname: '',
            organisation: 0,
            roles: {},
            userRole: 0,
            error: false,
            message: '',
            choosenOrga: 'none',
            orgas: {},
        }
    },
    mounted() {
        this.getRoleInfo();
        this.getCurrentRole();
        this.getOrgaID();
        this.getOrgaInfo();
    },
    methods: {
        changeRole(text, id) {
            this.choosenRole = text;
            this.role = id;
        },
        changeOrga(text, id) {
            this.choosenOrga = text;
            this.organisation = id;
        },
        getRoleInfo() {
            const path = '/api/role/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.roles = response.data;
                    this.isLoadedRole = true;
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
                    this.userRole = response.data.role;
                })
                .catch((err) => {
                    console.log(err);
                    console.log(this.cookies)
                })
        },
        getOrgaID() {
            const path = '/api/organisation/own/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.organisation = response.orgaid;
                })
                .catch((err) => {
                    console.log(err);
                    console.log(this.cookies)
                })
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
        addNewUser() {
            const path = '/api/register/'
            this.user = JSON.stringify({ email: this.email, name: this.name, firstname: this.firstname, role: this.role, organisation: this.organisation });
            if (this.organisation === 0 || this.name === '' || this.firstname === '' || this.role === 0) {
                alert('Please provide all the information needed');
            } else {
                axios.post(path, this.user, {
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
            }
            if (error === true) {
                alert(err.response.data.message);
            }
        }
    }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.input {
    $input-radius: 4px;
}
</style>
