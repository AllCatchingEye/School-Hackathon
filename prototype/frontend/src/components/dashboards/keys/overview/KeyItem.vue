<template>
    <div class="box">
        <div class="entry-wrapper">
            <div class="data-wrapper">
                <div class="entry">
                    <p>{{ tokenValue }}</p>
                </div>
            </div>
            <div class="lineItem buttons">
                <button class="button is-danger is-rounded is-outlined" @click="askDeleteItem">
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
    props: ['token', 'hackathonid', 'deleteApproval'],
    data() {
        return {
            tokenValue: this.token,
            hackathonID: this.hackathonid,
            WantDelete: -1,
        }
    },
    methods: {
        askDeleteItem() {
            this.WantDelete = this.tokenValue;
            const tokenID = this.tokenValue;
            this.$emit('item-delete-approve', tokenID);
        },
        deleteItem() {
            const path = '/api/token/' + this.tokenValue + '/';
            axios.delete(path, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            }).then((response) => {
                this.$emit('delete-item', this.tokenValue);
                this.$emit('success', response.data.message);

            }).catch((err) => {
                this.$emit('error', err.response.data.message);
            });
        },
    },
    watch: {
        deleteApproval(newVal, oldVal) {
            if (this.WantDelete == oldVal && newVal === true) {
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
    justify-content: end;
    align-content: space-between;
    flex-wrap: nowrap;
}

.entry-wrapper {
    width: 100%;
    display: flex;

    .data-wrapper {
        width: 80%;
        display:grid;
        grid-template-columns: 95% 5%;
        height:80px;
        align-items:center;
        grid-column-gap:10px;

        .entry {
            input {
                font-size: 1em;
            }
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
