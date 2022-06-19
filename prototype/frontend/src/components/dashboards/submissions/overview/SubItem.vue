<template>
    <div class="box">
        <div class="entry-wrapper">
            <div class="data-wrapper">
                <div class="entry">
                    <p>{{ subID }}</p>
                </div>
              <div class="entry" v-if="!edit">
                <p>{{updatedData}}</p>
              </div>
              <div class="entry" v-if="edit">
                          <textarea v-model="updatedData"></textarea>
              </div>
            </div>
            <div class="lineItem buttons">
              <div  class="editbutton is-link is-rounded" @click="edit = !edit" v-if="!edit">Bearbeiten</div>
              <div  class="editbutton is-link is-rounded" @click="updateValue()" v-if="edit">Speichern</div>
              <div  class="button is-danger is-rounded is-link" @click="edit = !edit" v-if="edit">Abbrechen</div>
                <button class="button is-danger is-rounded is-outlined" @click="askDeleteItem" v-if="!edit">
                    <span>Löschen</span>
                    <span class="icon is-small">
                        <i class="fas fa-times"></i>
                    </span>
                </button>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
export default {
    props: ['token', 'subname', 'deleteApproval'],
    data() {
        return {
            subID: this.token,
            edit: false,
            updatedData: this.subname,
            WantDelete: -1,
        }
    },mounted(){
      console.log(this.updatedData);
  },
    methods: {
        askDeleteItem() {
            this.WantDelete = this.subID;
            const subID = this.subID;
            this.$emit('item-delete-approve', subID);
        },
        deleteItem() {
            const path = '/api/submission/' + this.subID + '/';
            axios.delete(path, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            }).then((response) => {
                this.$emit('delete-item', this.subID);
                this.$emit('success', response.data.message);

            }).catch((err) => {
                this.$emit('error', err.response.data.message);
            });
        }, updateValue(){
          console.log(this.updatedData);
          const request = JSON.stringify({ subid: this.subID, description: this.updatedData });
          const path = '/api/submission/' + this.subID + '/';
          axios.patch(path, request, {
            headers: {
              'Content-Type': 'application/json'
            },
            withCredentials: true
          }).then((response) => {
            this.$emit('update-item', this.subID);
            this.$emit('success', response.data.message);

          }).catch((err) => {
            this.updatedData = this.subname;
            this.$emit('error', err.response.data.message);
          });
        this.edit = false;
      }
    },
    watch: {
        deleteApproval(newVal, oldVal) {
            if (this.WantDelete === oldVal && newVal === true) {
                this.deleteItem();
            }
        }
    }
}
</script>


<style  lang="scss" scoped>
.buttons {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-content: space-between;
    flex-wrap: nowrap;
}


.editbutton{
  margin-right: 3%;
  background-color: #1ABC9C;
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

.entry-wrapper {
    width: 100%;
    display: flex;

    .data-wrapper {
        width: 80%;
        display:grid;
      justify-content: center;
        grid-template-columns: 1fr 6fr 1fr;
        align-items:center;
        grid-column-gap:10px;

        .entry {
          margin-top: 5%;
          margin-bottom: 5%;
          overflow: scroll;
          position: relative;
          display: flex;
          align-items: center;
          min-height: 10vh;

            textarea{
              min-width: 80%;
              max-width:30vw;
              min-height: 10vh;
              max-height: 50vh;
              padding: 0.5rem;
              font-size: 1rem;
              border: solid #0000001c 1px;
            }

          textarea:focus { outline: none; }
        }
    }
}



.buttonItem {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
    margin-right: 1rem;
}

.buttonItem:hover {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
}

.buttonItem:active {
    color: white;
}

.button {
    margin-top: 1rem;
    margin-bottom: 1rem;
}

.buttonItemAction {
    display: flex;
    justify-content: space-around;
}

.box {
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin: 0.5rem 1%;
    vertical-align: middle;
    padding-top: 0px;
    padding-bottom: 0px;

}

select {
    /* Reset Select */
    appearance: none;
    outline: 0;
    border: 0;
    box-shadow: none;
    /* Personalize */
    flex: 1;
    padding: 0 1em;
    background-color: none;

    background-image: none;
    width: 100%;
    cursor: pointer;
}

/* Remove IE arrow */
select::-ms-expand {
    display: none;
}
</style>
