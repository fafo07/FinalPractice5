<template>
  <Navbar></Navbar>
  <router-view/>
</template>



<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue';
export default {
  components: {
    Navbar,
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #c6c6c6;
}

nav a.router-link-exact-active {
  color: #ffffff;
}
</style>
