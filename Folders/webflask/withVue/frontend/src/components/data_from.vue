<template>
  <div>
    <p>Get page</p>
    <button @click="getRandom">New random number</button>
    <p>Random number from backend: {{ randomNumber }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = 'http://localhost:5000/handler'
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.r_num
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
