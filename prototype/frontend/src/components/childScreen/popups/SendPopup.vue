<template>
  <div class="FullScreen">
    <div class="OuterSymbol">
      <div class="InnerSymbol">
        <div class="headline">
          <h2>Möchtest du deine Ergebinsse abschicken?</h2>
        </div>
        <div class="textBox">
          <p>Nach dem Abschicken kannst du deine Vorschläge nicht mehr ändern.</p>
          <p class="statusMessage">{{this.status}}</p>
        </div>
      </div>
    </div>
    <div class="buttons">
      <div class="returnButton childButton" @click="() => TogglePopup('buttonTrigger')">
        <i class="fa-solid fa-minus"></i>
      </div>
      <div class="sendButton childButton" @click="send_submissions()">
        <i class="fa-solid fa-paper-plane"></i>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "SendPop",
  props: ['TogglePopup', 'amount', 'entrys', 'hackathonSlug', 'uuid'],
  data(){
    return{
      status: ""
    }
  },
  methods: {
    send_submissions(){
      const path = '/api/submission/'.concat(this.hackathonSlug, "/", this.uuid);
      console.log(path);
      let entries = [];

      this.entrys.forEach(element => {
        if (element !== '') {
          entries.push(element);
        }
      })

      if (entries.length > 0 && entries[0].length > 5) {
        axios.post(path, entries, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(() => {
            this.displayApproved = true;
            setTimeout(() => {
              this.status = "worked";
            }, 1000);
          }).catch(() => {
          this.displayDisapproved = true;
          setTimeout(() => {this.status ="Deine Anfrage konnte vom Server nicht verabeitet werden, wurde dein Code schon verwendet?"}, 10);
        });
      }else{
        this.status = "Bitte überprüfe ob du etwas eingetragen hast und probiere es erneut"
      }
    },
  }
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
  justify-content: flex-start;
  align-items: center;
  padding-top: 10%;
  flex-direction: column;
}
.OuterSymbol{
  color: white;
  font-family: inter, san-serif, serif;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  background-color: #1ABC9C;
  width: 90%;
  height: 70%;
  margin-bottom: 5%;
  border-radius: 30px;
}

.InnerSymbol{
  position: relative;
  display: flex;
  align-items: flex-start;
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
  padding-left: 5%;
  font-size: 5vw;
  font-weight: 500;
  letter-spacing: 1.25px;
  overflow: hidden;
}

.textBox p{
  overflow: scroll;
}


.buttons{
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

.returnButton{
  background-color: #CD3B59;
}

.sendButton{
  background-color: #1ABC9C;
}

.statusMessage{
  font-weight: 700;
  margin-top: 5%;
  color: #CD3B59;
}


</style>

