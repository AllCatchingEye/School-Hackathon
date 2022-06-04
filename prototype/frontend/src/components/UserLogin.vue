<template>
  <section class="hero is-primary is-fullheight" id="login-form">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <img src="../assets/wirfuerschuleLogo.png" alt="wirfuerschule logo"/>
            <div class="box">
              <div class="field">
                <label for="" class="label">Email</label>
                <div class="control has-icons-left">
                  <input v-model="email" type="email" placeholder="e.g. bobsmith@gmail.com" class="input" required>
                  <span class="icon is-small is-left">
                    <i class="fa fa-envelope"></i>
                  </span>
                </div>
              </div>
              <div class="field">
                <label for="" class="label">Password</label>
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
        password: ''
      }
  },
  methods: {
    verifyLogin(){
      const path = 'http://project.flask/api/login/';
      this.test = JSON.stringify({email: this.email, password: this.password});
      const cookies = useCookies();
      axios.post(path, this.test, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then((result) => {        
        this.cookies.set("access_token_cookie", result.data.access_token);

      }).catch((err) => {
        console.log(err);
      });;
      }
  }
}
</script>

<style>
#login-form {
  background-color: whitesmoke;
}
</style>