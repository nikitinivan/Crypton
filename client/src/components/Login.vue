<template lang="html">
  <div class="login">
    <h1>Login</h1>
    <button v-on:click="testroute" type="button" name="button">Click</button>
  </div>
  </template>

<script>
import {testroute} from '../helpers/auth'

export default {
  name: 'login',
  data () {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    testroute: function () {
      testroute()
    }
  }
}
</script>

<style lang="css">
</style>
