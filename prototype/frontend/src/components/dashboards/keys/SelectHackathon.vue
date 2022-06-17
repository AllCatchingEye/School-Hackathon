<template>
    <div class="data">
        <div class="sidebar">
            <div class="fontHeadline">
                <img class="wirfuerschuleimg" alt="wir für schule logo"
                    src="../../../assets/wirfuerschuleLogoweiß.png" />
                <p class="headline">Schlüsselübersicht</p>
            </div>
            <div @click="goHome()">
                <HomeButton></HomeButton>
            </div>
            <div v-if="!openPopup" class="sidebarBottom">
                <div>
                    <LogoutButton></LogoutButton>
                </div>
                <p class="label">© 2022 wirfuerschule.de</p><br>
            </div>
        </div>
        <div class="outerBoxOverview">
            <div class="headlineUsers">
                <p>Schlüsselübersicht</p>
            </div>
            <div class="userDataHeader">
                <div class="lineItem">
                    <p>Hackathon</p>
                </div>
                <div class="lineItem">
                    <p>Schlüssel</p>
                </div>
            </div>
            <div class="scrollableUsers">
                <a v-for="unit in hackathons" :key="unit.hackathonid">
                    <HackathonUnit :hackathonName="unit.title" :hackathonID="unit.hackathonid"></HackathonUnit>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
import LogoutButton from './../../LogoutButton.vue';
import OpenPopupButton from "../OpenPopupButton";
import HomeButton from "../HomeButton";
import HackathonUnit from './HackathonUnit';

export default {
    components: { HomeButton, OpenPopupButton, LogoutButton, HackathonUnit },
    data() {
        return {
            hackathons: {},
        }
    },
    mounted() {
        this.getHackathons();
    },
    methods: {
        goHome() {
            this.$router.push('/');
        },
        getOverview() {
            this.$router.push({ path: '/keys/overview', query: { hackathon: this.hackathon } });
        },
        async getHackathons() {
            const path = '/api/hackathon/';
            await axios.get(path)
                .then((response) => {
                    this.hackathons = response.data;
                })
                .catch(() => {
                    this.displayQuestions = false;
                    this.displayDisapproved = true;
                    setTimeout(() => { location.reload(); }, 1000);
                });
        },
    }
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.data {
    display: grid;
    grid-template-columns: 30% 70%;
    height: 100vh;
    width: 100%;
    overflow: hidden;
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

.headlineUsers {
    width: 59vw;
    text-align: left;
    align-items: flex-start;
    margin-bottom: 2rem;
    margin-top: 2rem;
    padding-bottom: 1rem;
    border-bottom: rgba(109, 105, 114, 0.46) 1px solid;
}

.scrollableUsers {
    overflow-x: hidden;
    height: 75%;
    width: 63vw;
    margin-top: 5%;
    margin-bottom: 5%;
}

.sidebar {
    height: 100%;
    width: 100%;
    background-color: #000a38;
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

.outerBoxOverview {
    align-items: center;
    grid-template-columns: 15% 10% 10% 10%;
    justify-content: space-around;
    flex-wrap: nowrap;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
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

.sidebarBottom {
    position: absolute;
    bottom: 2rem;
    width: 30%;
    text-align: center;
    color: #d9d9d9;
}

.userDataHeader {
    display: grid;
    justify-content: space-evenly;
    width: 60vw;
    grid-template-columns: 25% 10% 10% 10%;

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


.label {
    color: white;
    margin-top: 2vh;
}
</style>
