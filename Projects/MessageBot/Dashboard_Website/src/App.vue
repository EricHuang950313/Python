<template>
  <form @submit.prevent="handleSubmit">
    <label>Channel ID:</label>
    <input type="text" v-model="id">
    <label>Message:</label>
    <input type="text" v-model="message">
    <div class="btn">
      <button @click="sendMessage">Send</button>
    </div>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      message: null,
      id: null
    }
  },
  methods: {
    async sendMessage(){
      const respond = await axios({
      method: 'post',
      url: 'http://localhost:3000/sendMsgToChannel',
      data: {
        msg: this.message,
        id: this.id
      }
    })
    alert(respond.data);
    this.message = null;
    this.id = null;
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #777;
  margin-top: 60px;
}
form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
}
label {
  color: #aaa;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.6em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}
input{
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
}
.btn{
  text-align: center;
}
button {
    background: #ffffff;
    border: 4 #000;
    padding: 10px 20px;
    margin-top: 20px;
    color: black;
    border-radius: 20px;
}
button:hover{
  transform: scale(1.2)
}
</style>
