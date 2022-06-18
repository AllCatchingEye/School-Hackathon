<template>
  <div class="base">
    <div class="middleAlign">
      <div class="Symbols">
        <TextSymbol :TogglePopup="() => TogglePopup('Text')"></TextSymbol>
        <InputSymbol v-model="entry[0]" :TogglePopup="() => TogglePopup('popup0')"></InputSymbol>
        <transition name="fade">
        <InputSymbol v-model="entry[1]" :TogglePopup="() => TogglePopup('popup1')" v-if="amountEntries >= 2"></InputSymbol>
        </transition>
        <transition name="fade">
        <InputSymbol v-model="entry[2]" :TogglePopup="() => TogglePopup('popup2')" v-if="amountEntries >= 3"></InputSymbol>
        </transition>
      </div>
      <div class="buttons">
        <div v-if="amountEntries < 3" class="addButton childButton" @click="addInput()">
          <i class="fa-solid fa-plus"></i>
        </div>
        <div v-if="amountEntries > 1" class="substractButton childButton" @click="substractInput()">
          <i class="fa-solid fa-minus"></i>
        </div>
        <div class="sendButton childButton" @click="() => TogglePopup('Send')">
          <i class="fa-solid fa-paper-plane"></i>
        </div>
      </div>
    </div>
  </div>
  <div class="popups">
    <transition name="fade">
    <SendPop :amount="amountEntries" :entrys="entry" :hackathonSlug="hackathonSlug" :uuid="uuid" v-if="popupTriggers.Send"
             :TogglePopup="() => TogglePopup('Send')"></SendPop>
    </transition>
    <transition name="fade">
    <TextSymbolPop
      v-if="popupTriggers.Text"
      :TogglePopup="() => TogglePopup('Text')">
    </TextSymbolPop>
    </transition>
    <transition name="fade">
    <InputSymbolPop v-model="entry[0]"
      v-if="popupTriggers.popup0"
      :TogglePopup="() => TogglePopup('popup0')">
    </InputSymbolPop>
    </transition>
    <transition name="fade">
    <InputSymbolPop v-model="entry[1]"
                    v-if="popupTriggers.popup1 && amountEntries >= 2"
                    :TogglePopup="() => TogglePopup('popup1', 2)">
    </InputSymbolPop>
    </transition>
    <transition name="fade">
    <InputSymbolPop v-model="entry[2]"
                    v-if="popupTriggers.popup2 && amountEntries >= 3"
                    :TogglePopup="() => TogglePopup('popup2', 3)">
    </InputSymbolPop>
    </transition>
  </div>
</template>

<script>
import {ref} from "vue";
import TextSymbolPop from "./popups/TextSymbolPop";
import InputSymbolPop from "./popups/InputSymbolPop";
import TextSymbol from "./TextSymbol";
import InputSymbol from "./InputSymbol";
import SendPop from "./popups/SendPopup";
export default {
  name: "BaseScreen",
  components: {SendPop, InputSymbol, TextSymbol, TextSymbolPop, InputSymbolPop},
  mounted(){
    this.hackathonSlug=this.$route.params.hackathonSlug;
    this.uuid=this.$route.params.uuid;
    console.log(this.hackathonSlug, this.uuid);
  },
  data() {
    return {
      hackathonSlug: null,
      uuid: null,
      amountEntries: 1,
      entry: ["","", ""],
    }
  },
  setup () {
    const popupTriggers = ref({
      Text: false,
      Send: false,
      popup0: false,
      popup1: false,
      popup2: false
    });
    const TogglePopup = (trigger) => {
      popupTriggers.value[trigger] = !popupTriggers.value[trigger]
    }
    return {
      TogglePopup,
      popupTriggers,
      TextSymbolPop,
      InputSymbolPop,
    }
  },
  methods:{
    addInput(){
      if (this.amountEntries < 3){
        this.amountEntries += 1;
      }
    },
    substractInput(){
      if (this.amountEntries > 1){
        this.amountEntries -= 1;
      }
      if (this.amountEntries === 2){
        this.entry[2] = "";
      }
      if (this.amountEntries === 1){
        this.entry[1] = "";
      }
    }
  }
}
</script>

<style scoped lang="scss">

.base{
  position: fixed;
  width: 100vw;
  height: 100vh;
}

.middleAlign{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.addButton{
  background-color: #48C78E;
}
.substractButton{
  background-color: #CD3B59;
}

.sendButton{
  background-color: #8188a6;
}

.Symbols{
  margin-top: 10%;
  overflow: scroll;
  width: 90%;
  height: 100%;
  margin-bottom: 60%;
  padding-bottom: 60%;
}

.buttons{
  background-color: #ffffff9c;
  backdrop-filter: blur(10px);
  padding: 5vw;
  border-radius: 80px;
  display: flex;
  justify-content: space-around;
  position: fixed;
  bottom: 5%;
  width: 80%;
}

.childButton{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20vw;
  height: 20vw;
  border-radius: 60px;
  font-size: 10vw;
  color: white;
}

.fade-enter-from{
  opacity: 0;
}
.fade-enter-to{
  opacity: 1;
}
.fade-enter-active{
  transition: all 0.5s ease;
}
.fade-leave-from{
  opacity: 1;
}
.fade-leave-to{
  opacity: 0;
}
.fade-leave-active{
  transition: all 0.5s ease;
}
 @media only screen and (min-width: 600px) {
 .buttons{
   padding:20px;
   width:40%;
 }
 .Symbols{
   margin-top:30px;

 }
 
 .childButton{
   max-width:100px;
   max-height:100px;
   font-size:60px;
 }
 }
</style>
