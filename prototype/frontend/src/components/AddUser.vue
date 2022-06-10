<template>
    <div v-if="isLoadedRole === true">
        <div class="field">
            <label class="label">Vorname</label>
            <div class="control">
                <input v-model="firstname" class="input" type="text" placeholder="e.g. Merlinöse" required>
            </div>
        </div>
        <div class="field">
            <label class="label">Nachname</label>
            <div class="control">
                <input v-model="name" class="input" type="text" placeholder="e.g. Scammerino" required>
            </div>
        </div>
        <div class="field">
            <label class="label">Email</label>
            <div class="control">
                <input v-model="email" class="input" type="email" placeholder="e.g. test@mail.de" required>
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
        <div v-if="userRole == 420 && isLoadedRole === true">
            <div class="field">
                <label class="label">Organisation</label>
                <div class="control">
                    <input v-model="organisation" class="input" type="number" placeholder="Schule XY" required>
                </div>
            </div>
        </div>
        <div>
            <button class="button is-success is-rounded" @click="addNewUser">Submit</button>
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
    data() {
        return {
            isLoadedRole: false,
            choosenRole: 'none',
            role: 0,
            name: '',
            firstname: '',
            organisation: 0,
            roles: {},
            userRole: 0,
        }
    },
    mounted() {
        this.getRoleInfo();
        this.getCurrentRole();
    },
    methods: {
        changeRole(text, id) {
            this.choosenRole = text;
            this.role = id;
        },
        getRoleInfo() {
            const path = '/api/role/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    console.log('Recieved Data for Role as:');
                    console.log(response.data);
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
                        alert(err.response.data.message);
                    });
            }
        }
    }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
</style>
