<template>
  <div>
    <div class="field">
      <label class="label">Title</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="Todo Name"
          v-model="productName"
        />
      </div>
    </div>
 
    <div class="field">
      <label class="label">Date</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="Todo Date"
          v-model="productPrice"
        />
      </div>
    </div>

     <div class="field">
      <label class="label">users</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="users"
          v-model="productPrice"
        />
      </div>
    </div>

     <div class="field">
      <label class="label">content</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="content"
          v-model="productPrice"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">importance</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="importance"
          v-model="productPrice"
        />
      </div>
    </div>

 
    <div class="control">
      <button class="button is-success" @click="saveProduct">SAVE</button>
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
      productName: "",
      productPrice: "",
    };
  },
  methods: {
    // Create New product
    async saveProduct() {
      try {
        await axios.post("http://localhost:5000/products", {
          product_name: this.productName,
          product_price: this.productPrice,
        });
        this.productName = "";
        this.productPrice = "";
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