<template>
    <div class="box">
        <div>
            <div class="userData">
                <div class="lineItem">
                    <span class="userNameList" v-if="edit === false">
                      <div class="UserNameListTag">
                        {{ userName }}
                      </div>
                      <div class="UserNameListTag">
                        {{ userLastName }}
                      </div>
                    </span>
                    <span class="userNameList" v-else>
                      <input type="text" :value="userName" class="input" />
                        <input type="text" :value="userLastName" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ userDetails[0] }}
                    </span>
                    <span class="UserNameList" v-else>
                        <input type="text" :value="userDetails[0]" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span v-if="edit === false">
                        {{ userDetails[1] }}
                    </span>
                    <span class="UserNameList" v-else>
                        <input type="text" :value="userDetails[1]" class="input" />
                    </span>
                </div>
                <div class="lineItem">
                    <span class="UserNameList button-wrapper" v-if="edit === true">
                        <button class="button is-success is-rounded" @click="update">Update</button>
                        <button class="button is-danger is-rounded" @click="cancel" buttonText="Cancel">Cancel</button>
                    </span>
                    <span v-else>
                        <button class="button is-link is-rounded" @click="editing">Edit</button>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    props: {
        userName: {
            type: String,
            default: () => "Place",
        },
        userLastName: {
            type: String,
            default: () => "Holder"
        },
        userDetails: {
            type: Array,
            default: () => []
        },
    },
    data() {
        return {
            edit: false
        }
    },
    methods: {
        editing() {
            this.edit = !this.edit
        },
        update() {
            this.edit = false
        },
        cancel() {
            this.edit = false
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

.UserNameListTag{
  margin-right: 2rem;
  margin-left: 2rem;
}

.userData {
  vertical-align: top;
  flex-direction: row;
  display: grid;
  align-items: center;
  grid-template-columns: 25% 10% 10% 10%;
  justify-content: space-around;
  width: 55vw;
  flex-wrap: nowrap;
}

.userNameList{
  width: 100%;
  margin-right: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  
}

.lineItem {
  margin-right: 1rem;
}

.button{
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.userName .input{
  margin-right: 1rem;
}

.input{
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
    padding-top:0px;
    padding-bottom:0px;
    
}

</style>
