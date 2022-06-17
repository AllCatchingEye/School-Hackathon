<template>
  <div class="FullScreen">
    <div class="OuterSymbol">
      <div class="InnerSymbol">
        <div class="headline">
          <h2>Dein Vorschlag</h2>
          <div class="smallerButton" @click="TogglePopup()">
            <i class="fa-solid fa-down-left-and-up-right-to-center"></i>
          </div>
        </div>
        <div class="textBox">
          <p>Schreibe deinen Vorschlag in die Textbox unten. Wenn du fertig mit allen Vorschlägen bist klicke auf den Papierflieger.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TextSymbolPop",
  props: ['TogglePopup']
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
  align-items: center;
  background-color: #3498DB;
  width: 90%;
  height: 90%;
  margin-bottom: 5%;
  border-radius: 30px;
}

.InnerSymbol{
  position: relative;
  width: 90%;
  height: 90%;
}

.headline h2{
  font-size: 5vw;
  font-weight: 600;
  margin-bottom: 5%;
}

.textBox{
  font-size: 5vw;
  font-weight: 500;
  letter-spacing: 1.25px;
  overflow: hidden;
}

.textBox p{
  overflow: scroll;
}

.readMore{
  position: absolute;
  bottom: 5%;
  right: 5%;
  background-color: #0000003b;
  padding: 1vw 5vw;
  border-radius: 30px;

  font-size: 5vw;
  font-weight: 500;
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


</style>

