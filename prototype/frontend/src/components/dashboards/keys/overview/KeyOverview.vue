<template>

    <div v-if="PopUp">
        <generate-form @close-pop-up="closePopUp" @error="onError" @success="onSuccess" @item-added="addItem"
            :hackathonid="hackathonID">
        </generate-form>
    </div>

    <div v-if="DeleteModal" class="modal delete-model">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Wirklich löschen?</p>
                <button class="delete" aria-label="close" @click="cancelApproval()"></button>
            </header>

            <footer class="modal-card-foot">
                <button class="button is-danger" @click="deleteApproval()">Löschen</button>
                <button class="button" @click="cancelApproval()">Abbrechen</button>
            </footer>
        </div>
    </div>

    <div class="data">
        <sidebarDash :currentpage="this.currentpage"></sidebarDash>


        <div class="outerBoxOverview">
            <div class="headlineItems">
                <p>Schlüsselübersicht</p>
            </div>
            <Transition name="slide-fade">
                <article class="message is-danger" v-if="Errormessage.length">
                    <div class="message-header">
                        <p>Error</p>
                    </div>
                    <div class="message-body">
                        {{ Errormessage }}
                    </div>
                </article>
            </Transition>
            <Transition name="slide-fade">
                <article class="message is-success" v-if="Successmessage.length">
                    <div class="message-header">
                        <p>Success</p>
                    </div>
                    <div class="message-body">
                        {{ Successmessage }}
                    </div>
                </article>
            </Transition>
            <div class="button-wrapper">
              <div class="qrbutton is-link is-rounded" @click="downloadQR()">QR-Codes anzeigen</div>
                <button class="add-item button is-success is-rounded" @click="changePopup()">Schlüssel
                    erstellen</button>
            </div>
            <div class="scrollable-items-outer">
                <div class="scrollable-items">
                    <ul>
                        <li v-for="item in Data" :key="item.tokenid">
                            <span v-if="item.hackathon.hackathonid == this.hackathonID">
                                <key-item :token="item.tokenid" :hackathonid="this.hackathonID"
                                    :deleteApproval="DeleteApprove" @item-delete-approve="openDeleteApproval"
                                    @delete-item="deleteItem" @error="onError" @success="onSuccess"></key-item>
                            </span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import GenerateForm from './GenerateForm.vue';
import KeyItem from './KeyItem.vue';
import sidebarDash from '../../sidebar/sidebarDash.vue';

export default {
    components: {
        GenerateForm,
        KeyItem,
        sidebarDash
    },
    data() {
        return {
            hackathonName: this.$route.query.hackathon,
            hackathonID: this.$route.query.id,
            Data: [],
            accessAllowed: false,
            currentpage: "token",
            PopUp: false,
            Errormessage: "",
            Successmessage: "",
            DeleteModal: false,
            DeleteApprove: 0,
        };
    },
    mounted() {
        this.getData();
    },
    methods: {
        changePopup() {
            this.PopUp = true;
        },
        closePopUp() {
            this.PopUp = false;
        },
        cancelApproval() {
            this.DeleteModal = false;
            this.DeleteApprove = 0;
        },
        onSuccess(message) {
            this.Errormessage = "";
            this.Successmessage = message;
            setTimeout(() => this.Successmessage = "", 2000);

        },
        onError(message) {
            this.Successmessage = "";
            this.Errormessage = message;
            setTimeout(() => this.Errormessage = "", 2000);

        },
        deleteItem(id) {
            let itemIndex = this.Data.findIndex(x => x.tokenid == id);
            this.Data.splice(itemIndex, 1);
            this.DeleteApprove = 0;
            this.DeleteModal = false;
        },
        openDeleteApproval(id) {
            this.DeleteApprove = id;
            this.DeleteModal = true;
        },
        deleteApproval() {
            this.DeleteApprove = true;
            this.DeleteModal = true;
        },
        addItem(items) {
            items.forEach(elem => this.Data.push(elem))
        },
        getData() {
            const path = '/api/token/'
            axios.get(path, {
                withCredentials: true
            })
                .then((response) => {
                    this.accessAllowed = true;
                    this.Data = response.data;
                }).catch((err) => {
                    if (err.response.status == 401) {
                        this.$router.push({ name: "Login", params: { message: "Du musst eingeloggt sein!" } });
                    } else {
                        this.onError(err.response.data.message);
                    }
                })
        },
        downloadQR() {
          let path = "/api/qrcode/".concat(this.hackathonID, "/");
          let label = "wirfuerschulehack".concat(this.hackathonID);
          axios.get(path, { responseType: 'blob' })
            .then(response => {
              const blob = new Blob([response.data], { type: 'application/pdf' })
              const link = document.createElement('a')
              link.href = URL.createObjectURL(blob)
              link.download = label
              link.click()
              URL.revokeObjectURL(link.href)
            }).catch(console.error)
        }
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

.qrbutton {
  margin-right: 3%;
  background-color: #5ac6ce;;
  border-color: #dbdbdb;
  border-width: 1px;
  border-radius: 30px;
  color: white;
  cursor: pointer;
  justify-content: center;
  padding-bottom: calc(0.5em - 1px);
  padding-left: 1em;
  padding-right: 1em;
  padding-top: calc(0.5em - 1px);
  text-align: center;
  white-space: nowrap;
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
    max-height: 75vh;
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
  display: flex;
  width: 84%;
  text-align: right;
  justify-content: flex-end;
  align-items: center;
  flex-direction: row;
  align-content: center;
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
