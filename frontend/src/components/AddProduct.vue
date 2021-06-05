<template>
  <div>
    <div class="field">
      <label class="label">Todo Task</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="Product Name"
          v-model="title"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">Todo Date</label>
      <div class="control">
        <input
          class="input"
          type="date"
          placeholder="mm/dd/yyyy"
          v-model="todoDate"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Todo Users</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="John Doe"
          v-model="users"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Description</label>
      <div class="control">
        <textarea
          class="input"
          placeholder="Todo description"
          v-model="content"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Importance</label>
      <div class="control">
        <input
          class="input"
          type="number"
          placeholder="0-5"
          v-model="importance"
        />
      </div>
    </div>
    <div class="control">
      <button class="button is-success" @click="addTodo">ADD</button>
    </div>
  </div>
</template>
 
<script>
// import axios
import axios from "axios";

export default {
  name: "AddProduct",
  data() {
    return {
      title: "",
      todoDate: "",
      users: "",
      content: "",
      importance: 0,
    };
  },
  methods: {
    // Create New product
    async addTodo() {
      try {
        await axios.post("http://localhost:8000/api/v1/todos/", {
          title: this.title,
          date: this.todoDate,
          users: this.users,
          content: this.content,
          importance: this.importance,
        });

        this.title = "";
        this.todoDate = "";
        this.users = "";
        this.content = "";
        this.importance = "";

        this.$router.push("/");
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>
 
<style>
</style>