<template>
    <div class="Navbar">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">F&F</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <router-link class="nav-link" to="/">Home</router-link>
                        <router-link class="nav-link" to="/activos">Activos</router-link>
                        <router-link class="nav-link" to="/Areas">Areas</router-link>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>
  
<script>
export default {
    name: 'Navbar',
}
</script>