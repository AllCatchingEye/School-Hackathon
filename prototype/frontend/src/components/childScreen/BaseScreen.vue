<template>
  <div class="base">
    <div class="middleAlign">
      <div class="Symbols">
        <TextSymbol :TogglePopup="() => TogglePopup('buttonTrigger')"></TextSymbol>
        <InputSymbol></InputSymbol>
      </div>
      <div class="buttons">
        <div class="addButton childButton">
          <i class="fa-solid fa-plus"></i>
        </div>
        <div class="sendButton childButton">
          <i class="fa-solid fa-paper-plane"></i>
        </div>
      </div>
    </div>
  </div>
  <div class="popups">
    <TextSymbolPop
      v-if="popupTriggers.buttonTrigger"
      :TogglePopup="() => TogglePopup('buttonTrigger')">
    </TextSymbolPop>
  </div>
</template>

<script>
import {ref} from "vue";
import TextSymbolPop from "./popups/TextSymbolPop";
import TextSymbol from "./TextSymbol";
import InputSymbol from "./InputSymbol";
export default {
  name: "BaseScreen",
  components: {InputSymbol, TextSymbol, TextSymbolPop},

  setup () {
    const popupTriggers = ref({
      buttonTrigger: false,
      timedTrigger: false
    });
    const TogglePopup = (trigger) => {
      popupTriggers.value[trigger] = !popupTriggers.value[trigger]
    }
    setTimeout(() => {
      popupTriggers.value.timedTrigger = true;
    }, 3000);
    return {
      TextSymbolPop,
      popupTriggers,
      TogglePopup
    }
  }
}
</script>

<style scoped lang="scss">

.base{
  position: fixed;
  width: 100vw;
  height: 100vh;
  overflow: scroll;
}

.middleAlign{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.Symbols{
  width: 90%;
  height: 90%;
}

.buttons{
  display: flex;
  justify-content: space-around;
  position: fixed;
  bottom: 7%;
  width: 80%;
}

.childButton{
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #8188a6;
  width: 20vw;
  height: 20vw;
  border-radius: 60px;
  font-size: 10vw;
  color: white;
}
</style>
