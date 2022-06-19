<template>
    <div class="modal delete-model">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Einreichunngsgenerierung</p>
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
                    <label for="entry">Deine Einreichung:</label>
                    <textarea id="entry" placeholder="Tippe hier um zu schreiben" v-model="entry"></textarea>
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
            Data: {},
            HackathonID: parseInt(this.hackathonid),
            Amount: 1,
            entry: "",
            Errormessage: "",
            hackathonslug: "",
            uuid: ""
        };
    },
    methods: {
        onError(message) {
            this.Errormessage = message;
            setTimeout(() => this.Errormessage = "", 2000);

        },
        onSubmit() {

          let path = '/api/token/';
          const dataJson = JSON.stringify({ hackathon: this.HackathonID, count: 1 });
          axios.post(path, dataJson, {
            headers: {
              'Content-Type': 'application/json'
            },
            withCredentials: true
          })
            .then((response) => {
              let Data = response.data.dataobj[0];

              const uuid = Data.tokenid;
              const hackathonslug = Data.hackathon.slug;


              path = ('/api/submission/').concat(hackathonslug, "/", uuid, "/");
              let result = this.entry;
              let request = {};
              request = JSON.stringify({ "result" : [{"description": result}]});

              if (this.entry.length > 1) {
                axios.post(path, request, {
                  headers: {
                    'Content-Type': 'application/json'
                  }
                })
                  .then(() => {
                    this.$emit("item-added");
                    this.$emit("success", ("Einreichung: ".concat(this.entry, " erfolgreich")));
                    this.$emit("close-pop-up");
                  }).catch(() => {
                  setTimeout(() => {this.Errormessage ="Deine Anfrage konnte vom Server nicht verabeitet werden, wurde dein Code schon verwendet?"}, 10);
                });
              }else{
                this.Errormessage = "Bitte überprüfe ob du etwas eingetragen hast und probiere es erneut"
              }

            }).catch((err) => {
            this.onError(err.response.data.message);
            // this.$emit("close-pop-up");
          })
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

.add-item textarea{
  margin-top: 5%;
  border: #817a7a30 1px solid;
  padding: 1rem;
  max-width: 100%;
  max-height: 40vh;
  min-height: 20vh;
  min-width: 50%;
}

textarea:focus { outline: none; }
</style>


