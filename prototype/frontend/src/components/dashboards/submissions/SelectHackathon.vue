<template>
    <div class="data">
        <sidebarDash :currentpage="this.currentpage"></sidebarDash>
        <div class="outerBoxOverview">
            <div class="headlineItems">
                <p>Einreichungsübersicht: Hackathonauswahl</p>
            </div>
            <div class="scrollable-items-outer">
                <div class="scrollable-items">
                    <ul>
                        <li v-for="item in Data" :key="item.hackathonid">
                            <hackathon-item :hackathonname="item.title" :hackathonid="item.hackathonid"></hackathon-item>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import HackathonItem from './HackathonItem.vue';
import sidebarDash from "../sidebar/sidebarDash";

export default {
    components: {
        HackathonItem,
        sidebarDash
    },
    data() {
        return {
            Data: [],
            accessAllowed: false,
            currentpage: "submissions",
            error: "",
        };
    },
    mounted() {
        this.getData();
    },
    methods: {
        getData() {
            const path = '/api/hackathon/';
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.accessAllowed = true;
                    this.Data = response.data;
                }).catch((err) => {
                    if (err.response.status == 401) {
                        this.$router.push({ name: "Login", params: { message: "You have to be logged in" } });
                    } else {
                        this.error = err.response.data.message;
                        console.log(this.error);
                    }
                })
        },
    }

}

</script>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.delete-model {
    display: flex;
}

.data {
    display: grid;
    grid-template-columns: 30% 70%;
    height: 100vh;
    width: 100%;
    overflow: hidden;

}

.firstItem {
    margin-left: 2%;
}

.lineItem {
    padding-left: 1rem;
    flex-direction: row;
    display: flex;
    justify-content: space-around;
}

.lineItem p {
    margin-right: 2rem;
}

.headlineItems {
    width: 59vw;
    text-align: left;
    align-items: flex-start;
    margin-bottom: 2rem;
    margin-top: 2rem;
    padding-bottom: 1rem;
    border-bottom: rgba(109, 105, 114, 0.46) 1px solid;
}

.scrollable-items-outer {
    position: relative;
    height: 100%;
}

.scrollable-items {
    overflow: scroll;
    width: 64vw;
    height: 100%;
    max-height: 80vh;
    margin-top: 1%;
    margin-bottom: 2%;
}

.wirfuerschuleimg {
    align-items: center;
    width: 60%;
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.headline {
    margin: 1rem;
    padding-bottom: 1rem;
    width: 80%;
    text-align: left;
    border-bottom: #d9d9d9 1px solid;
}

.message {
    width: 80%;
}

.outerBoxOverview {
    align-items: center;
    grid-template-columns: 20% 10% 10% 10%;
    justify-content: space-between;
    flex-wrap: nowrap;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
    padding-bottom: 5%;
}

.fontHeadline {
    font-size: 20px;
    letter-spacing: 0.05em;
    font-family: 'Roboto', sans-serif;
    align-content: center;
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
    text-align: center;
    color: #d9d9d9;
    align-items: center;
}



.label {
    color: white;
    margin-top: 2vh;
}


::-webkit-scrollbar {
    width: 10px;
    height: 5px;
}

::-webkit-scrollbar-track {
    background: white;
}

::-webkit-scrollbar-thumb {
    background-color: grey;
    border-radius: 10px;
}

a {
    color: #d9d9d9;
}

.button-wrapper {
    width: 84%;
    text-align: right;
}

/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
    transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
    transition: all 0.8s cubic-bezier(0.5, 1, 1, 0.8);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
    transform: translateY(20px);
    opacity: 0;
}
</style>
