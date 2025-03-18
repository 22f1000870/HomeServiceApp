<script setup lang="js">
import NavBar from '@/components/navbar/NavBar.vue';
import { computed} from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const services = computed(()=> store.state.services.services)
</script>


<template>
    <div><NavBar></NavBar></div>

    <div class="container mt-5">
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

<style>
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

