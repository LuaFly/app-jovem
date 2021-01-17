<template>
  <div id="app">
    <Menu id="menu"> </Menu>
    <Corpo id="corpo"> </Corpo>
  </div>
</template>

<script>
import Menu from "./components/Menu.vue";
import Corpo from "./components/Corpo.vue";
export default {
  name: "app",
  components: {
    Menu,
    Corpo
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
