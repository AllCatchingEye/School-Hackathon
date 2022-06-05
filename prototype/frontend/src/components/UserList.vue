<template>
    <div class="OuterBox">
        <h3 v-for="name in fullNames" :key="name.last">
            <User :userName="name.first" :userLastName="name.last"
                :userDetails="[name.email, name.password, name.organization, name.role]" />
        </h3> <br>
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
    props: {
        buttonText: {
            type: String,
            default: () => "Label",
        },
    },
    data() {
        return {
            fullNames: [
                { first: 'Anton', last: 'Aloah', email: 'anton@aloah.de', password: 'xyz', organization: 'Schule ABC', role: 'admin' },
                { first: 'Bernd', last: 'Birne', email: 'bernd@birne.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
                { first: 'Caesar', last: 'Couch', email: 'caesar@couch.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
                { first: 'Dirk', last: 'Dentist', email: 'dirk@dentist.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
                { first: 'Egon', last: 'Epsilon', email: 'egon@e.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
                { first: 'Ferdinand', last: 'Fahrradreifen', email: 'ferdi@freifen.de', password: 'xyz', organization: 'Schule ABC', role: 'admin' },
                { first: 'Gerhald', last: 'Gehörsturz', email: 'gerhald@gsturz.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
                { first: 'Heinrich', last: 'Halligalli', email: 'heini@galli.de', password: 'xyz', organization: 'Schule ABC', role: 'lehrer' },
                { first: 'Imbissbude', last: 'Am Eck', email: 'imbissbude-am-eck@essen.to', password: 'xyz', organization: 'Schule ABC', role: 'superadmin' },
            ],
            isLoaded: false,
            response: {},
            showAll: false,
        }
    },
    mounted() {
        this.getUserInfo();
    },
    methods: {
        getUserInfo() {
            const path = '/api/user/'
            axios.get(path, {
                headers: {
                    Cookie: this.cookies
                }
            })
                .then((response) => {
                    this.isLoaded = true;
                    console.log(response);
                    this.response = response.data;
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
.OuterBox{
  overflow: scroll;
}

#Box {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>