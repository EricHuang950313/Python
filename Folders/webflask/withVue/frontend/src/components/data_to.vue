<template>
  <div>
    <p>Send page</p>
    <input v-model="enterNumber" placeholder="Enter number to backend:" maxlength = "10">
    <button @click="enterTo">Send</button>
    <p> Enter number to backend {{ enterNumber }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      enterNumber: null
    }
  },
  methods: {
    enterTo () {
      this.enterNumber = this.enterNumberToBackend()
    },
    enterNumberToBackend () {
      this.enterNumber = Number(this.enterNumber)
      if (isNaN(this.enterNumber)) {
        console.log('Not numbers!')
      } else {
        const path = 'http://localhost:5000/handler'
        axios.post(path, { fromVue: this.enterNumber })
          .then(response => {
            this.enterNumber = null
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
}
</script>
