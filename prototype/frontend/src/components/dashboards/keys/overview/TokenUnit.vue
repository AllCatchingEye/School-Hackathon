<template>
    <div class="box">
        <div>
            <div class="HackathonData">

                <div class="lineItem">
                    <span class="HackathonNameList">
                        {{ token }}
                    </span>
                </div>
                <div class="lineItem">
                    <span class="HackathonNameList">
                        <buttom class="button is-rounded is-danger" @click="deleteToken">Delete</buttom>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    props: {
        tokenID: {
            default: () => -1,
        },
    },
    data() {
        return {
            token: this.tokenID,
        }
    },
    methods: {
        async deleteToken() {
            const path = '/api/token/' + this.token + '/';
            await axios.delete(path)
                .catch((err) => {
                    console.log(err);
                });
            location.reload();
        }
    }
}
</script>


<style scoped>
.buttonUser {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
    margin-right: 1rem;
}

.buttonUser:hover {
    background-color: rgba(130, 0, 205, 0.83);
    color: white;
}

.buttonUser:active {
    color: white;
}

.HackathonNameListTag {
    margin-right: 2rem;
    margin-left: 2rem;
}

.HackathonData {
    vertical-align: top;
    flex-direction: row;
    display: grid;
    align-items: center;
    grid-template-columns: 25% 10% 10% 10%;
    justify-content: space-around;
    width: 55vw;
    height: auto;
    flex-wrap: nowrap;
}

.HackathonNameList {
    width: 100%;
    margin-right: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.lineItem {
    margin-right: 1rem;
    height: auto;
    width: 100%;


}

::-webkit-scrollbar {
    width: 5px;
    height: 5px;
}

::-webkit-scrollbar-track {
    background: white;
}

::-webkit-scrollbar-thumb {
    background-color: #0D2385;
    border-radius: 10px;
}



.button {
    margin-top: 1rem;
    margin-bottom: 1rem;
}

.HackathonName .input {
    margin-right: 1rem;
}

.input {
    width: 10vw;
    margin-left: 1rem;
}

.box {
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 56vw;
    margin: 0.5rem 1%;
    vertical-align: middle;
    padding-top: 0px;
    padding-bottom: 0px;

}
</style>
