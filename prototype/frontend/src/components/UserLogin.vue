<template>
<div class="control">
  <form>
    <label for="username" class="label">Benutzername: </label>
    <input type="text" id="username" class="input is-large" placeholder="Benutzername..." required><br><br>
    
    <label for="password" class="label">Passwort: </label>
    <input type="password" id="password" class="input is-large" placeholder="Passwort..." required><br><br>

    <button class="button is-primary" type="submit">Anmelden</button>
  </form>
</div>

</template>

<script>
/* eslint-disable */
export default {
    name: 'UserLogin',
    data() {
  },
  methods: {
    }
};
</script>

<style>
</style>