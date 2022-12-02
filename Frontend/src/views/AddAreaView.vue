
<template>
    <div class="areas">
     
            <div class="container-fluid">
                <div class="container">
                    <div class="row py-4">
                        <div class="col">
                            <h2 class="text-center">Agregar Area</h2>
                        </div>
                    </div>
                    <div class="row g-3 align-items-center py-2">
                        <div class="col-auto">
                            <label for="Nombre" class="form-label">Nombre:</label>
                        </div>
                        <div class="col-auto">
                            <input type="text" class="form-control" id="Nombre" v-model="area.nombre">
                        </div>
                    </div>

                    <div class="row g-3 align-items-center py-2">
                        <div class="col-auto">
                            <label for="Encargado" class="form-label">Encargado de Area:</label>
                        </div>
                        <div class="col-auto">
                            <input type="text" class="form-control" id="Encargado" v-model="area.Encargado">
                        </div>
                    </div>

                    <div class="row g-3 align-items-center py-2">
                        <div class="col-auto">
                            <label for="Funcionarios" class="form-label">Nro Funcionarios:</label>
                        </div>
                        <div class="col-auto">
                            <input type="number" class="form-control" id="Funcionarios" v-model="area.Funcionarios">
                        </div>
                    </div>

                    <div class="row py-2">
                        <div class="col-4">
                            <button class="btn btn-primary" @click="addarea()">Agregar Area</button>
                        </div>
                    </div>
                </div>
            </div>
        
    </div>
</template>


<script>


export default ({
    name: "#AddareasView",
    data() {
        return {
            area: {
                nombre: null,
                Encargado: null,
                Funcionarios: null
            },
        }
    },
    methods: {
        addarea() {
            axios({
                method: "post",
                url: process.env.VUE_APP_RUTA_API+"/area",
                data: this.area
            })
            .then(response =>{
                console.log(response);
            })
            .catch(e => console.log(e)) 
            this.$router.push({name: 'areas'});           
        },
    }
});
</script>
