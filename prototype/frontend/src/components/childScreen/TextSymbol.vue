<template>
  <div class="OuterSymbol">
    <div class="InnerSymbol">
      <div class="headline">
        <h2>So geht's:</h2>
     </div>
      <div class="textBox">
        <p>Schreibe deinen Vorschlag in die Textbox unten. Wenn du fertig mit allen Vorschlägen bist klicke auf den Papierflieger.</p>
      </div>
      <div class="readMore" @click="() => TogglePopup()">
        <p>mehr lesen</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: ['TogglePopup']
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800&family=Roboto&display=swap');

.FullSize{
  position: fixed;
  width: 100vw;
  height: 100vh;
}
.OuterSymbol{
  color: white;
  font-family: inter, san-serif, serif;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #3498DB;
  width: 100%;
  height: 40%;
  min-height: 40vh;
  margin-bottom: 5%;
  border-radius: 30px;


}

.InnerSymbol{
  position: relative;
  width: 90%;
  height: 90%;
}

.headline h2{
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

 @media only screen and (min-width: 600px) {
 .readMore{
    padding: 10px;

  font-size: 20px;
  }

.textBox{
  font-size: 20px;
}

.headline h2{
    font-size: 20px;
}

.OuterSymbol{
  min-height:200px;
  max-width:600px;
  margin:auto;
}
.InnerSymbol{
  max-width:600px;
}
 }
</style>
