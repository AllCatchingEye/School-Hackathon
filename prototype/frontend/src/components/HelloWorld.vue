<template>
hahahas{{ping}}rer
<button type="button" @click="getBooks()">click me</button>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
    data() {
    return {
      ping: ''
      }
  },
  methods: {
      getBooks() {
        const path = '/api/ping';
        axios.get(path)
          .then((res) => {
          console.log(res);
            this.ping = res.data.ping_pong;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    }
};
</script>
