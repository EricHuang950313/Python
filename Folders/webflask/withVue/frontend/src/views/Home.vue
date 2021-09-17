<template>
  <div class="home">
    <img alt="VueLogo" src="../assets/logo.png">
    <Data/>
  </div>
</template>

<script>
import Data from '@/components/data_from.vue'

export default {
  name: 'from',
  components: {
    Data
  }
}
</script>
