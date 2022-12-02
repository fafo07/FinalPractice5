<template>
    <div class="areas">
        <div class="container-fluid">
            <div class="container">
                <div class="row py-4">
                    <div class="col-auto">
                        <h3>Editar Activo</h3>
                    </div>
                </div>
                <div class="row g-3 align-items-center py-2">
                    <div class="col-3">
                        <input type="text" class="form-control" id="Activo" placeholder="Activo"
                            v-model="activo.Activo">
                    </div>
                </div>

                <div class="row g-3 align-items-center py-2">
                    <div class="col-3">
                        <input type="text" class="form-control" id="Marca" placeholder="Marca" v-model="activo.Marca">
                    </div>
                </div>

                <div class="row g-3 align-items-center py-2">
                    <div class="col-3">
                        <input type="text" class="form-control" id="Estado" placeholder="Estado"
                            v-model="activo.Estado">
                    </div>
                </div>

                <div class="row g-3 align-items-center py-2">
                    <div class="col-auto">
                        <label for="Areas">Area:</label>
                    </div>
                    <div class="col-3">
                        <select id="Areas" class="form-control" v-model="activo.areaId">
                            <option v-for="area in lista_areas" v-bind:key="area.id" v-bind:value="area.id"  value={{area.id}}>{{ area.nombre }}</option>
                        </select>
                    </div>
                </div>

                <div class="row py-2">
                    <div class="col-4 align-self-end">
                        <button class="btn btn-primary" @click="editactivo()">Editar Activo</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>

export default ({
    name: "#EditactivosView",
    data() {
        return {
            activo: {
                Activo: null,
                Marca: null,
                Estado: null,
                areaId: null
            },
            lista_areas: []
        }
    },
    methods: {
        getactivo() {
            axios({
                method: "get",
                url: process.env.VUE_APP_RUTA_API+"/activo/" + this.$route.params.id,
            })
                .then(response => {
                    this.activo = response.data
                    console.log(response);
                })
                .catch(e => console.log(e))
        },
        getAreas() {
            axios
                .get(process.env.VUE_APP_RUTA_API+"/area")

                .then(response => {
                    this.lista_areas = response.data
                    console.log(response)
                })
                .catch(e => console.log(e))
        },  
        editactivo() {
            axios({
                method: "patch",
                url: process.env.VUE_APP_RUTA_API+"/activo/" + this.$route.params.id,
                data: this.activo
            })
                .then(response => {
                    console.log(response);
                })
                .catch(e => console.log(e))
            this.$router.go(-1);
        },
    },
    mounted() {
        this.getAreas();
        this.getactivo();
        console.log(this.area);
    },
});
</script>