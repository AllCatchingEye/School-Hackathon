<template>
  <div id="app">
    <div class="fontHeadline">
      <b><u>Benutzerübersicht</u></b>
    </div>
    <div class="box">
      <UserList></UserList>
    </div>
  </div>
  <label>© 2022 wirfuerschule.de</label><br>
  <img alt="wir für schule logo" src="./assets/wirfuerschuleLogoSmall.png" />
</template>

<script>
import UserList from './components/UserList.vue'
export default {
  name: 'App',
  components: {
    UserList
  },
}
</script>

<style lang="scss">
.box {
  box-shadow: 0px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 100px;
  margin-right: 100px;
}

.fontHeadline {
  font-size: xx-large;
}

#app {
  text-align: center;
  margin-top: 60px;
}
</style>
