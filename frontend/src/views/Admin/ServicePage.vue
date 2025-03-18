<script setup lang="js">
import NavBar from '@/components/navbar/NavBar.vue';
import { computed} from 'vue';
import { useStore } from 'vuex';
import SearchBar from '@/components/searchbar/SearchBar.vue';
const store = useStore();


// Correct way to use getters from Vuex
const services = computed(() => store.getters["services/filterservices"]);

</script>


<template>
    <div><NavBar></NavBar></div>

    <div><SearchBar module="services"></SearchBar></div>


    <div class="container mt-3">
    <h2 class="text-center mb-4 text-dark fw-bold">Services</h2>
    
    <div class="table-responsive">
        <table class="table table-bordered table-striped table-hover text-center align-middle">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Image</th>
                    <th>Service Name</th>
                    <th>Profession</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(service,index) in services" :key="service.id">
                    <td>{{index+1 }}</td>
                    <td class="img-thumbnail">
                        <img :src="service.image_url" alt="Product 1" style="width: 100px; height: 100px;" >
                    </td>
                    <td>{{ service.servicename }}</td>
                    <td>{{ service.profession }}</td>
                    <td>{{ service.base_price }}</td>
                </tr>
            </tbody>
        </table>
        <div>
            <RouterLink class="btn btn-secondary btn-lg" to="/create-service">Create Service</RouterLink>
        </div>
    </div>
</div>
</template>

<style scoped>
@import '/src/assets/css/searchbar.css';

.table thead th {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    color: white;
    text-align: center;
    font-size: 18px;
}
.table tbody tr:hover {
    background-color: #ffe8e8;
}
.img-column img {
    width: 60px;
    height: 60px;
    border-radius: 10px;
    object-fit: cover;
}


</style>

