<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>{{testVariable}}</h2>
    <br></br>
    <h2>{{number}}</h2>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    align-items: center;
  }
}
</style>


<script>
  import axios from 'axios'
  export default {
    data: function() {
      return {
        testVariable: this.testGet(),
        number: this.testGet2(),
      }
    },
    methods: {
      testGet() {
        axios.get("http://127.0.0.1:8000/test/", {headers: {'Content-Type': 'application/json'}}).then(response => {
          this.testVariable = response.data.response
          console.log(response.data)
        })
      },
      testGet2() {
        axios.post("http://127.0.0.1:8000/test2/", {val1: 10298, val2: 10}, {headers: {'Content-Type': 'application/json'}}).then(response => {
          this.number = response.data.answer
        })
      }
    }
  }
</script>