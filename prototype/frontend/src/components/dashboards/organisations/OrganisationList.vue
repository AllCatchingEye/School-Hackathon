<template>
    <div class="OuterBox">
        <span class="innerBox" v-if="isLoaded === true">
            <h3 v-for="organisation in response" :key="organisation.orgaid">
                <OrganisationElement :OrganisationName="organisation.name"
                    :OrganisationID="organisation.orgaid"/>
            </h3> <br>
        </span>
    </div>
</template>

<script>
import axios from 'axios';
import { useCookies } from 'vue3-cookies';
import OrganisationElement from './OrganisationElement.vue';

export default {
    setup() {
        const { cookies } = useCookies();
        return { cookies };
    },
    components: {
        OrganisationElement,
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
            const path = '/api/organisation/'
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
