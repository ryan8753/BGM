<template>
  <div>
    <div :style="{'backgroundImage':'url('+ tmdb + movie.poster_path +')',
          'backgroundSize':'cover',
          'filter':'brightness(88%)'}"
          id="backgrounds"
          class="justify-content-center d-flex">
        <h1 class="mt-5">TOP 5 BACK GROUND MOVIE</h1>  
        <div class="card mb-3 row-2 homeback" id="extra" style="max-width: 540px;">
          <div class="row g-0">
          <div class="col-md-4">
            <img :src="tmdb+movie.poster_path" class="img-fluid rounded-start" alt="...">
          </div>
        <div class="col-md-8 homeback">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{movie.overview }}</p>
            <router-link 
              :to="{ name: 'detail', params: { movieId: movie.movie_id } }"
              class="btn btn-primary">
              GO TO DETAIL
            </router-link>
          </div>
        </div>
        </div>
        </div>
    <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeMovie',
  props:{
    movie: Object,
  },
  data(){
        return {
          tmdb:'https://image.tmdb.org/t/p/w500/',
        }
      },
    computed: {
      posterUrl (poster_path){
        return `https://image.tmdb.org/t/p/w500`+ poster_path
      }
      
    },
}

</script>

<style>
#backgrounds{
  background: linear-gradient(to top, black, rgb(10, 28, 38));
  height: 100vh;
}

#extra{
  height: 37vh;
  position: relative;
  top: 13em; 
}

.card-text{
  -webkit-line-clamp: 5;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}

.homeback{
  background-color: rgb(10, 28, 38);
}
</style>