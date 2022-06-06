<template>
    <div class="OuterBox">
        <span class="innerBox" v-if="isLoaded === true">
            <h3 v-for="user in response" :key="user.email">
                <User :userName="user.firstname" :userLastName="user.name"
                    :userDetails="[user.email, user.organisations.name, user.roles.description]"/>
            </h3> <br>
        </span>
    </div>
</template>

<script>
import axios from 'axios';
import { useCookies } from 'vue3-cookies';
import User from './UserElement.vue'
export default {
    setup() {
        const { cookies } = useCookies();
        return { cookies };
    },
    components: {
        User,
    },
    data() {
        return {
            // fullNames: [
            //     { first: 'Anton', last: 'Aloah', email: 'anton@aloah.de', password: 'xyz', organization: 'Schule ABC', role: 'admin' },
            //     { first: 'Bernd', last: 'Birne', email: 'bernd@birne.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
            //     { first: 'Caesar', last: 'Couch', email: 'caesar@couch.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
            //     { first: 'Dirk', last: 'Dentist', email: 'dirk@dentist.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
            //     { first: 'Egon', last: 'Epsilon', email: 'egon@e.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
            //     { first: 'Ferdinand', last: 'Fahrradreifen', email: 'ferdi@freifen.de', password: 'xyz', organization: 'Schule ABC', role: 'admin' },
            //     { first: 'Gerhald', last: 'Gehörsturz', email: 'gerhald@gsturz.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
            //     { first: 'Heinrich', last: 'Halligalli', email: 'heini@galli.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
            //     { first: 'Imbissbude', last: 'Am Eck', email: 'imbissbude-am-eck@essen.to', password: 'xyz', organization: 'Schule ABC', role: 'superadmin' },
            // ],
            isLoaded: false,
            response: {},
        }
    },
    mounted() {
        this.getUserInfo();
    },
    methods: {
        getUserInfo() {
            const path = '/api/user/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.response = response.data;
                    this.isLoaded = true;
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

.innerBox{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>
