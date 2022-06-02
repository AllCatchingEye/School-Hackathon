<template>
  <section class="hero is-primary is-fullheight" id="login-form">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <img src="../assets/wirfuerschuleLogo.png" alt="wirfuerschule logo"/>
            <form action="" class="box">
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
                <label for="" class="checkbox">
                  <input type="checkbox">
                Remember me
                </label>
              </div>
              <div class="field">
                <button class="button is-success" @click="verifyLogin()">
                  Login
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <p>{{this.email}}</p>
    <p>{{this.password}}</p>
  </section>
  
</template>

<script>
import axios from 'axios';

/* eslint-disable */
export default {
    name: 'UserLogin',
    data() {
      return {
        email: '',
        password: ''
      }
  },
  methods: {
    verifyLogin(){
      const path = '/api/login';

      axios(path, {
        email: this.email,
        password: this.password
        })
        .then((res) =>
          console.log(res)) 
        .catch((error) => {
          console.error(error);
        })
      }
  }
}
</script>

<style>
#login-form {
  background-color: whitesmoke;
}
</style>