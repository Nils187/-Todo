<template>
  <div>
    <router-link :to="{ name: 'Create' }" class="button is-success mt-5"
      >Add New</router-link
    >
    <table class="table is-striped is-bordered mt-2 is-fullwidth">
      <thead>
        <tr>
          <th>Todo title</th>
          <th>date</th>
          <th>users</th>
          <th>content</th>
          <th>importance</th>
          <th class="has-text-centered">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.title }}</td>
          <td>{{ item.date }}</td>
          <td>{{ item.users }}</td>
          <td>{{ item.content }}</td>
          <td>{{ item.importance }}</td>
          <td class="has-text-centered">
            <router-link
              :to="{ name: 'Edit', params: { id: item.id } }"
              class="button is-info is-small"
              >Edit</router-link
            >
            <a
              class="button is-danger is-small"
              @click="deleteTodo(item.id)"
              >Delete</a
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
 
<script>
// import axios
import axios from "axios";
 
export default {
  name: "ToDoslist",
  data() {
    return {
      items: [],
    };
  },
 
  created() {
    this.getToDos();
  },
 
  methods: {
    // Get All Products
    async getToDos() {
      try {
        const response = await axios.get("http://localhost:8000/api/v1/todos/");
        this.items = response.data;
      } catch (err) {
        console.log(err);
      }
    },
 
    // Delete Product
    async deleteTodo(id) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/todos/${id}`);
        this.getProducts();
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>
 
<style>
</style>