<template>
  
    <div id="app">
      <nav-bar
        v-if="partnerLoggedIn&&userLoggedIn">
      </nav-bar>
      
      <router-view
        :key="$route.fullPath">
      </router-view>
    
    </div>
 
</template>


<script>
import { mapGetters } from 'vuex'
import NavBar from './components/NavBar.vue'

export default {
  name : "App",
  components:{
    NavBar

  },
  computed:{
    ...mapGetters(['partnerLoggedIn', 'userLoggedIn'])
  }
    
  
}
</script>





<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
#app {
  font-family: 'Black Han Sans', sans-serif, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color : #BEB9B9  ;
  /* color: #2c3e50; */
  height: 100vh;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

  @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
body{
  
  background:rgb(10, 28, 38);
}

body,body*{
  
  font-family: 'Black Han Sans', sans-serif;
}

</style>
