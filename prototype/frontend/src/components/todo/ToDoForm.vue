<template>
<form @submit.prevent="onSubmit">
    <label for="new-todo-input">
      What needs to be done?
    </label>
    
    <input
  type="text"
  id="new-todo-input"
  name="new-todo"
  autocomplete="off"
  v-model="inputData" />

    <button type="submit">
      Add
    </button>
  </form>
</template>
<script>
export default {
  methods: {
    onSubmit() {
        this.$emit("todo-added", this.inputData);
    }
  },
  data() {
    return {
      inputData: ""
    };
  }
};

</script>