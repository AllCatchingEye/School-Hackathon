<template>
  <div id="app">
    <h1>My To-Do List</h1>
    <to-do-form @todo-added="addToDo"></to-do-form>
    <ul>
      <li v-for="item in ToDoItems" :key="item.id">  
        <to-do-item :label="item.label" :done="item.done" :id="item.id"></to-do-item>
      </li>
    </ul>
  </div>
</template>


<script>
import ToDoForm from './ToDoForm.vue';
import ToDoItem from './ToDoItem.vue';
export default{
components:{
    ToDoForm,
    ToDoItem
},
 data() {
    return {
      ToDoItems: [
        { id: 1, label: 'Learn Vue', done: false },
        {id: 2, label: 'Create a Vue project with the CLI', done: true },
        {id: 3, label: 'Have fun', done: true },
        { id: 4,label: 'Create a to-do list', done: false }
      ]
    };
  },
methods:{
    addToDo(test){
        this.ToDoItems.push({label: test, done:true})
        console.log('To-do added' + test);
    }
}

}

</script>