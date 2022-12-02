<template>
    <div class="areas">
        <div class="container-fluid">
            <div class="container">
                <div class="row py-4">
                    <div class="col">
                        <h2 class="text-center">Administracion de Areas</h2>
                    </div>
                    <div class="col">
                        <button @click="irA('Agregar', 0)" class="btn btn-dark">Crear Area</button>
                    </div>
                </div>
                <div class="row my-2 justify-content-center">
                    <h4>Buscador de Areas</h4>
                    <div class="col-4 my-2">
                        <form action="">
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" v-model="textoABuscar"
                                    placeholder="Buscar Areas" />
                                <button class="btn btn-outline-secondary" @click.prevent="getAreas()">Buscar</button>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="row my-2 justify-content-center">
                    <div class="col-4">
                        <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" :checked="control" v-on:input="control=$event.target.checked">
                        <label class="form-check-label" for="flexSwitchCheckDefault">Mostrar Areas con Nro de Empleados > 3</label>
                    </div>
                    </div>
                </div>
                <div class="row py-2">
                    <div class="col">
                        <div class="row">
                            <h3 class="text-center">Lista de Areas</h3>
                            <div class="col-12">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th scope="col">Id</th>
                                            <th scope="col">Area</th>
                                            <th scope="col">Encargado</th>
                                            <th scope="col">Nro Empleados</th>
                                            <th scope="col">Acciones</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(area, index) of lista">
                                            <td>{{ area.id }}</td>
                                            <td>{{ area.nombre }}</td>
                                            <td>{{ area.Encargado }}</td>
                                            <td>{{ area.Funcionarios }}</td>
                                            <td><button class="btn btn-success"
                                                    @click="irA('Editar', area.id)">Editar</button> <button
                                                    class="btn btn-danger"
                                                    @click="irA('Eliminar', area.id)">Eliminar</button></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default ({
    name: "#AreasView",
    data() {
        return {
            control:false,
            textoABuscar: '',
            lista_areas: [],
        }
    },
    methods: {
        getAreas() {
            axios
                .get(process.env.VUE_APP_RUTA_API + "/area?q=" + this.textoABuscar)

                .then(response => {
                    this.lista_areas = response.data
                    console.log(response)
                })
                .catch(e => console.log(e))
        },
        irA(opcion, id_area) {
            if (opcion == 'Agregar') {
                this.$router.push({ name: 'addarea' });
            }
            if (opcion == 'Editar') {
                this.$router.push({ name: 'editarea', params: { id: id_area } });
            }
            if (opcion == 'Eliminar') {
                if (confirm("Esta seguro de eliminar el Area?")) {
                    axios({
                        method: "delete",
                        url: process.env.VUE_APP_RUTA_API + "/area/" + id_area,
                    })
                        .then(response => {
                            this.getAreas();
                            console.log(response);
                        })
                        .catch(e => console.log(e))
                }
            }
        }
    },
    computed:{
        lista(){
            if(this.control)
            {
                return this.lista_areas.filter(item=>
                {
                    if(item.Funcionarios>5)
                    {
                        return item.Funcionarios;
                    }
                })
            }
            return this.lista_areas;
        }

    },
    mounted() {
        this.getAreas()
    },
});
</script>

  
  