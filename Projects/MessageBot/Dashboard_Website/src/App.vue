<template>
  <div class="bg">
    <form @submit.prevent="handleSubmit">
      <label>Channel ID:</label><br>
      <input type="text" v-model="id"><br>
      <label>Message:</label><br>
      <textarea style="width: 100%" rows="5" v-model="message"></textarea><br>
      <div class="btn">
        <button @click="sendMessage">Send</button>
      </div>
    </form>
    <img src="../botpic.png">
    <label class="lab">MessageBot/ EricHuang#5343</label>
  </div>
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
      url: 'https://MessageBot.erichuang950313.repl.co/sendMsgToChannel',
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
.bg {
  background-image: url("../pic.jpg");
  border-top: solid 1em #3b2406;
  border-bottom: solid 1em #3b2406;
  margin: 0;
  width: 100%;
  height: 700px;
  overflow: hidden;
  background-repeat: no-repeat;
  background-size: cover; 
  -webkit-background-size: cover;
  position: relative;
}
img {
  clip-path: inset(0 round 100px);
  width: 10%;
  position: absolute;
  right: 10%;
  bottom: 20%;
}
form {
    max-width: 420px;
    margin: 70px 50px;
    background: #ffffff;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
    border: 10px solid;
    border-image: linear-gradient(45deg, #03cafc, #005194) 1;
    clip-path: inset(0 round 10px);
}
form label {
  color: #aaa;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.75em;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  font-weight: bold;
}
.lab{
  color: #004e8d;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 1em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
  position: absolute;
  right: 5%;
  bottom: 12%;
}
input textarea{
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
}
textarea{
  resize: none;
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
