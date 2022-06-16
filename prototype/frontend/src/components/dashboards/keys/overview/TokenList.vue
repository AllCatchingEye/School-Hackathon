<template>
    <div class="OuterBox">
        <span class="innerBox" v-if="isLoaded === true">
            <h3 v-for="token in response" :key="token.tokenid">
                <span v-if="token.hackathon.hackathonid == this.currentID">
                    <TokenUnit :tokenID="token.tokenid"></TokenUnit>
                </span>
            </h3> <br>
        </span>
    </div>
</template>

<script>
import axios from 'axios';
import { useCookies } from 'vue3-cookies';
import TokenUnit from './TokenUnit.vue'
export default {
    setup() {
        const { cookies } = useCookies();
        return { cookies };
    },
    components: {
        TokenUnit,
    },
    data() {
        return {
            isLoaded: false,
            currentID: this.$route.query.id,
            response: {},
        }
    },
    mounted() {
        this.getCodes();
    },
    methods: {
        async getCodes() {
            const path = '/api/token/';
            await axios.get(path)
                .then((response) => {
                    this.isLoaded = true;
                    this.response = response.data;
                }).catch((err) => {
                    console.log(err);
                });
        }
    }
}
</script>


<style scoped>
.OuterBox {
    height: 75vh;
}

.innerBox {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
</style>
