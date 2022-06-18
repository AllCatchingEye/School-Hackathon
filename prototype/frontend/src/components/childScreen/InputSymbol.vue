<template>
  <div class="OuterSymbol" @click="() => TogglePopup()">
    <div class="InnerSymbol">
      <div class="headline">
        <h2>Dein Vorschlag</h2>
        <div class="biggerButton">
          <i class="fa-solid fa-up-right-and-down-left-from-center"></i>
        </div>
      </div>
      <div class="textBox">
        <div class="textarea">
          <div v-if="modelValue.length > 0">
            {{ this.modelValue }}
          </div>
          <div v-else>
            Tippe hier um zu schreiben
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InputSymbol",
  props: ['TogglePopup', 'modelValue'],
  emits: ['update:modelValue'],
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800&family=Roboto&display=swap');

.OuterSymbol{
  color: white;
  font-family: inter, san-serif, serif;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #1ABC9C;
  width: 100%;
  height: 40%;
  margin-bottom: 5%;
  border-radius: 30px;

}

.InnerSymbol{
  position: relative;
  display: flex;
  align-content: center;
  width: 95%;
  height: 95%;
  flex-direction: column;
  align-items: center;
}

.headline{
  padding-right: 2%;
  padding-left: 5%;
  width: 95%;
  height: 25%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.headline h2{
  font-size: 5vw;
  font-weight: 600;
  margin-bottom: 5%;
}

.biggerButton{
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

.textBox{
  position: relative;
  display: flex;
  justify-content: center;
  align-content: center;
  width: 95%;
  height: 70%;
  font-size: 5vw;
  font-weight: 500;
  letter-spacing: 1.25px;
}

.textarea {
  font-size: 5vw;
  font-weight: 600;
  letter-spacing: 0.5px;
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


 @media only screen and (min-width: 600px) {
 .readMore{
    padding: 10px;
  font-size: 20px;
  }

.textarea {

  font-size: 20px;
}
 
.headline h2{
    font-size: 35px;
}

.OuterSymbol{
  min-height:400px;
  max-width:600px;
  margin: 30px auto;
}
.InnerSymbol{
  max-width:80%;
}

.biggerButton{
  max-height:60px;
  max-width:60px;
  font-size:35px;

}
 }
</style>
