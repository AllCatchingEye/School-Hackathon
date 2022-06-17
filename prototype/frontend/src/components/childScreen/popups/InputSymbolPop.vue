<template>
  <div class="FullScreen">
    <div class="OuterSymbol">
      <div class="InnerSymbol">
        <div class="headline">
          <h2>Dein Vorschlag</h2>
          <div class="smallerButton"  @click="() => TogglePopup()">
            <i class="fa-solid fa-down-left-and-up-right-to-center"></i>
          </div>
        </div>
        <div class="textBox">
          <textarea placeholder="Tippe hier um zu schreiben" :value="modelValue"
                    @input="$emit('update:modelValue', $event.target.value)"></textarea>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InputSymbolPop",
  props: ['TogglePopup', 'modelValue'],
  emits: ['update:modelValue']
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800&family=Roboto&display=swap');


.FullScreen{
  position: fixed;
  width: 100vw;
  height: 100vh;
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
}
.OuterSymbol{
  color: white;
  font-family: inter, san-serif, serif;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  background-color: #1ABC9C;
  width: 90%;
  height: 90%;
  margin-bottom: 5%;
  border-radius: 30px;
}

.InnerSymbol{
  position: relative;
  display: flex;
  align-items: center;
  width: 90%;
  height: 95%;
  justify-content: center;
  flex-direction: column;
}

.headline h2{
  font-size: 5vw;
  font-weight: 600;
  margin-bottom: 5%;
}


.smallerButton{
  display: flex;
  align-content: center;
  align-items: center;
  justify-content: center;
  font-size: 7vw;
  color: #ffffffb8;
  height: 12vw;
  width: 12vw;
  background-color: #0000003b;
  border-radius: 30px;

}

.headline{
  padding-right: 2%;
  padding-left: 5%;
  width: 95%;
  height: 15%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.headline h2{
  font-size: 5vw;
  font-weight: 600;
  margin-bottom: 5%;
}

.textBox{
  position: relative;
  display: flex;
  justify-content: center;
  align-content: center;
  width: 95%;
  height: 90%;
  font-size: 5vw;
  font-weight: 500;
  letter-spacing: 1.25px;
}

textarea {
  font-size: 5vw;
  font-weight: 500;
  color: white;
  padding: 5%;
  width: 100%;
  height: 100%;
  max-width: 100%;
  max-height: 100%;
  line-height: 1.5;
  border: none;
  border-radius: 30px;
  background-color: #ffffff3d;
}

textarea::-webkit-input-placeholder {
  color: white;
  font-size: 5vw;
  font-weight: 600;
}

textarea:-moz-placeholder { /* Firefox 18- */
  color: white;
  font-size: 5vw;
  font-weight: 600;
}

textarea::-moz-placeholder {  /* Firefox 19+ */
  color: white;
  font-size: 5vw;
  font-weight: 600;
}

textarea:-ms-input-placeholder {
  color: white;
  font-size: 5vw;
  font-weight: 600;
}

textarea::placeholder {
  color: white;
  font-size: 5vw;
  font-weight: 600;
}

textarea:focus { outline: none; }

</style>

