<template>
  <div class="home">
    <img alt="VueLogo" src="../assets/logo.png">
    <Data/>
  </div>
</template>

<script>
import Data from '@/components/data.vue'

export default {
  name: 'Home',
  components: {
    Data
  }
}
</script>
