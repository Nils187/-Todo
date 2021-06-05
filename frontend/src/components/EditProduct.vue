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
      <button class="button is-success" @click="updateTodoByID">UPDATE</button>
    </div>
  </div>
</template>
 
<script>
// import axios
import axios from "axios";

export default {
  name: "EditProduct",
  data() {
    return {
      title: "",
      todoDate: "",
      users: "",
      content: "",
      importance: 0,
    };
  },
  created: function () {
    this.getTodoByID();
  },
  methods: {
    // Get Product By Id
    async getTodoByID() {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/v1/todos/${this.$route.params.id}/`
        );
        this.title = response.data.title;
        this.todoDate = response.data.date;
        this.users = response.data.users;
        this.content = response.data.content;
        this.importance = response.data.importance;
      } catch (err) {
        console.log(err);
      }
    },

    // Update product
    async updateTodoByID() {
      try {
        await axios.put(
          `http://localhost:8000/api/v1/todos/${this.$route.params.id}/`,
          {
            title: this.title,
            date: this.todoDate,
            users: this.users,
            content: this.content,
            importance: this.importance,
          }
        );

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
