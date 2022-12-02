<template>
  <div class="home">
    <div class="container-fluid">
      <div class="row text-center py-2">
        <h2>Pagina de Administracion de la Empresa F&F</h2>
      </div>
      <div class="text-center row">
        <div class="col">
          <h3>Productos</h3>
          <button class="btn btn-primary" @click="activo() ">Ir pagina Productos</button>
        </div>
        <div class="col">
          <h3>Areas</h3>
          <button class="btn btn-primary" @click="area() ">Ir pagina Areas</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'HomeView',
  components: {

  },
  methods:
  {
    activo() 
    {
      this.$router.push({ name: 'activos' });
    },
    area() 
    {
      this.$router.push({ name: 'areas' });
    }
  }
}
</script>
