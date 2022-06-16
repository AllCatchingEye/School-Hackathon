<template>
    <div class="PopupOuter">
        <div class="PopupInner">
            <div class="IconApprove" v-if="displayApproved">
                <i class="fa-solid fa-check"></i>
            </div>
            <div class="IconApprove" v-if="displayDisapproved">
                <i class="fa-solid fa-xmark"></i>
            </div>
            <div v-if="displayQuestions" class="HeaderPopup">
                <p>Schlüssel generieren</p>
            </div>
            <div v-if="displayQuestions" class="BodyPopup">
                <div class="row">
                    <div class="PopupQuestion">
                        <div class="PopupInput">
                            <input v-model="amount" type="number" min=0 max=200 autocomplete="off" required />
                            <label>Menge</label>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="displayQuestions" class="PopupFooter">
                <div class="PopupFooterButton" @click="reload()">
                    <PopupButtonDisapprove></PopupButtonDisapprove>
                </div>
                <div class="PopupFooterButton" @click="generateCodes()">
                    <PopupButtonApprove></PopupButtonApprove>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import PopupButtonApprove from "../PopupButtonApprove";
import PopupButtonDisapprove from "../PopupButtonDisapprove";
import { useCookies } from 'vue3-cookies';
axios.defaults.withCredentials = true;

export default {
    name: "PopupKeysGenerating",
    components: { PopupButtonDisapprove, PopupButtonApprove },
    setup() {
        const { cookies } = useCookies();
        return { cookies };
    },
    props: {
        hackathonID: {
            type: Number,
            default: () => -1,
        },
    },
    data() {
        return {
            fullHackathon: {},
            hackathon: 'Auswählen',
            hackathonid: this.hackathonID,
            amount: 0,
            result: '',
            hackathons: {},
            displayQuestions: true,
            displayApproved: false,
            displayDisapproved: false
        }
    },
    mounted() {
        this.getHackathons();
    },

    methods: {
        async generateCodes() {
            const path = '/api/token/';
            this.test = JSON.stringify({ hackathon: this.hackathonid, count: this.amount });
            if (this.hackathon == 'Auswählen') {
                alert("Please choose a hackathon!");
            } else if (this.amount > 200 || this.amount <= 0) {
                alert("Please choose an amount between 1 and 200!");
            } else {
                await axios.post(path, this.test, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(() => {
                        this.displayQuestions = false;
                        this.displayApproved = true;
                        setTimeout(() => { location.reload(); }, 1000);
                    }).catch(() => {
                        this.displayQuestions = false;
                        this.displayDisapproved = true;
                        setTimeout(() => { location.reload(); }, 1000);
                    });
            }
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
        changeHackathon(id, title) {
            this.hackathon = title;
            this.hackathonid = id;
        },
        reload() {
            location.reload();
        }
    }
}

</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");

.PopupOuter {
    position: fixed;
    width: 100vw;
    height: 100vh;
    background-color: #ffffff57;
    backdrop-filter: blur(30px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 50;
}

.IconApprove {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.PopupInner {
    position: relative;
    background-color: #000a38;
    width: 80%;
    height: 50%;
    border-radius: 40px;
    box-shadow: 11px 11px 23px 9px rgba(0, 12, 109, 0.33);
}

.PopupFooterButton {
    cursor: pointer;
    height: 70%;
    width: 30%;
}

.row {
    margin-top: 5%;
    width: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: space-around;
}

.fa-solid {
    color: white;
    font-size: 50vh;
}

.HeaderPopup {
    width: 100%;
    height: 15%;
    padding-left: 5%;
    color: white;
    font-size: 40px;
    font-weight: normal;
    display: flex;
    align-items: center;
    justify-content: flex-start;
}

.BodyPopup {
    width: 100%;
    height: 75%;
    padding-left: 5%;
    padding-right: 5%;
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    flex-direction: column;
}

.PopupFooter {
    height: 10%;
    width: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: space-around;
}


.PopupQuestion {
    height: 5%;
    width: 30%;
}

input {
    width: 100%;
    height: 100%;
    font-family: 'Open Sans', san-serif, serif;
    border: .2rem solid #0c9bfa;
    font-size: 1.5rem;
    padding: 1rem 1rem;
    color: #fff;
    border-radius: .5rem;
    background: none;
}

input:focus {
    outline: none;
}

.PopupInput {
    position: relative;
}

label {
    position: absolute;
    top: 50%;
    left: 2rem;
    transform: translateY(-50%);
    font-size: 1.5rem;
    background: #000a38;
    color: #fff !important;
    transition: all .25s linear;
    pointer-events: none;
}

input:focus~label,
input:not(:focus):valid~label {
    transform: translateY(50%);
    top: -40%;
    left: 1rem;
    font-size: 1.25rem;
    padding: 0 .3rem;
}
</style>
