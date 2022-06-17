<template>
<form @submit.prevent="onSubmit">
    <label for="name">
        name
</label>
    <input type="text" id="name" v-model="User['name']" />
    <label for="firstname">
        Firstname
    </label>
    <input type="text" id="firstname" v-model="User['firstname']" />
    <label for="email">
        Email
    </label>
    <input type="text" id="email" v-model="User['email']" />
      <label for="organisation">
        Organisation
    </label>
    <input type="number" id="organisation" v-model="User['organisation']" />
       <label for="role">
        Role
    </label>
    <input type="number" id="role" v-model="User['role']" />
    <button type="submit">
      Add
    </button>
  </form>
</template>
<script>
export default {
  methods: {
    onSubmit() {
        console.log(this.User);
        
        this.$emit("user-added", this.User);
    }
  },
  data() {
    return {
      User: {"name": "", "firstname":"", "email":"", "role":0, "organisation": 0}
    };
  }
};

</script>