<template>
    <div class="OuterBox">
        <span class="innerBox" v-if="isLoaded === true">
            <h3 v-for="user in response" :key="user.email">
                <User :userName="user.firstname" :userLastName="user.name"
                    :userDetails="[user.email, user.organisations, user.roles, user.userid]"/>
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
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>
