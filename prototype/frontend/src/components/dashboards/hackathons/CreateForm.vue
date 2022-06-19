<template>

<div class="modal delete-model">
    <div class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
        <p class="modal-card-title">Add Hackathon</p>
        <button class="delete" aria-label="close" @click="cancel"></button>
        </header>
        <section class="modal-card-body">
            <form class="add-item">
                <label for="title">Hackathon Title</label>
                <input type="text" id="title" required v-model="Data.title" />
                
                <label for="description">Description</label>
                <input type="text" id="description" required v-model="Data.description" />
                
                <label for="slug">Hackathon Slug</label>
                <input  type="text" id="slug" required v-model="Data.slug" />       
            </form>
        </section>
        <footer class="modal-card-foot">
            <button class="button is-danger is-rounded" @click="cancel">Cancel</button>
            <button  class="button is-success is-rounded" @click="onSubmit">Add</button>
        </footer>
    </div>       
</div>

</template>
<script>
import axios from 'axios';

export default {
    props: ['currentRole'],
  data() {
    return {
    Data: {"title": "", "description":"", "slug":""},
    };
  },
  methods: {
    onSubmit() {
        const path = '/api/hackathon/'
        const dataJson = JSON.stringify(this.Data);
        for (var key in this.Data) {
          if (this.Data[key].length < 1) {
            error = true;}
        }
        if (error){
          this.Errormessage = "Bitte fülle alle Felder aus";
        }else{
        axios.post(path, dataJson, {
          headers: {
            'Content-Type': 'application/json'
          },
          withCredentials: true
        })
        .then((response) => {
            this.$emit("item-added", response.data.dataobj);            
            this.$emit("success", response.data.message);    
            this.$emit("close-pop-up");           
       
        }).catch((err)=>{    
            this.$emit('error',err.response.data.message);                          
            this.$emit("close-pop-up");           
        })}
    },
    cancel(){
        this.$emit("close-pop-up");
    }
  }   
};

</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
.delete-model{
    display:flex;
    .add-item{
        display:flex;
        flex-direction:column;
        width:100%;
        margin:0% 0 2%;
        padding:0px 8%;
        label{
            font-family:'Roboto';
            font-weight:bold;
        }
        input,select{
            height:40px;
            font-size:1.2em;
            margin-bottom:5%;

        }
    }
  }
   

</style>