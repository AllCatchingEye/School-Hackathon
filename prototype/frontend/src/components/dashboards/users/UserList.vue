<template>

    <div class="OuterBox">
        <div class="innerBox" v-if="isLoaded === true">
            <div class="list-wrapper" v-for="user in response" :key="user.email">
                <User :userName="user.firstname" :userLastName="user.name"
                    :userDetails="[user.email, user.organisations, user.roles, user.userid]"/>
            </div> <br>
        </div>
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

.OuterBox{
  height:75vh;
}

.innerBox{
    position:relative;
}
.list-wrapper{
    width:100%;
}
</style>
