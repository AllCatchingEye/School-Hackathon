<template>
    <div class="modal delete-model">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Schlüsselgenerierung</p>
                <button class="delete" aria-label="close" @click="cancel"></button>
            </header>
            <section class="modal-card-body">
                <article class="message is-danger" v-if="Errormessage.length">
                    <div class="message-header">
                        <p>Error</p>
                    </div>
                    <div class="message-body">
                        {{ Errormessage }}
                    </div>
                </article>
                <form class="add-item">
                    <label for="name">Menge</label>
                    <input type="number" id="name" required="required" v-model="Amount" />
                </form>
            </section>
            <footer class="modal-card-foot">
                <button class="button is-danger is-rounded" @click="cancel">Abbrechen</button>
                <button class="button is-success is-rounded" @click="onSubmit">Generieren</button>
            </footer>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    props: ['hackathonid'],
    data() {
        return {
            HackathonID: parseInt(this.hackathonid),
            Amount: 0,
            Errormessage: ""
        };
    },
    methods: {
        onError(message) {
            this.Errormessage = message;
            setTimeout(() => this.Errormessage = "", 2000);

        },
        onSubmit() {
            const path = '/api/token/';
            const dataJson = JSON.stringify({ hackathon: this.HackathonID, count: this.Amount });
            let error = false;
            if (this.Amount < 1 || this.Amount > 1000) {
                error = true;
            }
            if (error) {
                this.Errormessage = "Bitte eine Zahl zwischen 1 und 1000 eingeben";
            } else {
                axios.post(path, dataJson, {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    withCredentials: true
                })
                    .then((response) => {
                        this.$emit("item-added", true);
                        this.$emit("success", response.data.message);
                        this.$emit("close-pop-up");

                    }).catch((err) => {
                        this.onError(err.response.data.message);
                        // this.$emit("close-pop-up");
                    })
            }
        },
        cancel() {
            this.$emit("close-pop-up");
        }
    }
};

</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.delete-model {
    display: flex;

    .add-item {
        display: flex;
        flex-direction: column;
        width: 100%;
        margin: 0% 0 2%;
        padding: 0px 8%;

        label {
            font-family: 'Roboto';
            font-weight: bold;
        }

        input,
        select {
            height: 40px;
            font-size: 1.2em;
            margin-bottom: 5%;
        }
    }
}
</style>


