<template>
  <section class="hero is-primary is-fullheight" id="login-form">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <img src="../../../assets/wirfuerschuleLogo.png" alt="wirfuerschule logo"/>
            <div class="box">
              <article class="message is-danger" v-if="error">
                <div class="message-header">
                  <p>Error</p>
                </div>
                <div class="message-body">
                  {{message}}
                </div>
              </article>

              <div class="field">
                <label for="" class="label">E-Mail</label>
                <div class="control has-icons-left">
                  <input v-model="email" type="email" placeholder="e.g. bobsmith@gmail.com" class="input" required>
                  <span class="icon is-small is-left">
                    <i class="fa fa-envelope"></i>
                  </span>
                </div>
              </div>
              <div class="field">
                <label for="" class="label">Passwort</label>
                <div class="control has-icons-left">
                  <input v-model="password" type="password" placeholder="*******" class="input" required>
                  <span class="icon is-small is-left">
                    <i class="fa fa-lock"></i>
                  </span>
                </div>
              </div>
              <div class="field">
                <button class="button is-success" @click="verifyLogin()">
                  Login
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
    </div>
  </section>

</template>

<script>
import axios from 'axios';
import {useCookies} from 'vue3-cookies';

/* eslint-disable */
export default {
    setup() {
      const { cookies } = useCookies();
      return { cookies };
    },
    name: 'UserLogin',
    data() {
      return {
        email: '',
        password: '',
        error: false,
        message: ""
      }
  },
  mounted() {
    this.checkUser();
  },
  methods: {
    async verifyLogin(){
      console.log("data" + this.email )
      const path = '/api/login/';
      this.test = JSON.stringify({email: this.email, password: this.password});
      const cookies = useCookies();
      await axios.post(path, this.test, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then((result) => {
        this.cookies.set("access_token_cookie", result.data.access_token);
        this.$router.push('/dashboard');
      }).catch((err) => {
        this.email = '';
        this.password = '';
        this.error = true;
        this.message = err.response.data.message;

      });
      },
    deleteCookie(){
      const path = '/api/logout/';
        axios.post(path, {}, {
          headers: {
            'Content-Type': 'application/json'
          }
        }).catch((e) => {    
          console.log("as");        
        })
        
    },
    checkUser() {
      const path = '/api/user/own/'
      axios.get(path, {
        withCredentials: true
      }).then((response) => {
        if(response.status == 200){  
          this.$router.push('/dashboard');
        }else{
          this.deleteCookie();                    
        }
        })
        .catch(() => {})
    },
    
  }
}
</script>

<style>
#login-form {
  background-color: whitesmoke;
}
label{
  color:black !important;
}
</style>
