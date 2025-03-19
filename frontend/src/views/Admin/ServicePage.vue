<script setup lang="js">
import NavBar from '@/components/navbar/NavBar.vue';
import { computed,watch} from 'vue';
import { useStore } from 'vuex';
import SearchBar from '@/components/searchbar/SearchBar.vue';
import ServiceUpdate from '@/components/update/ServiceUpdate.vue';
import SuccessRegister from '@/components/popup/SuccessRegister.vue';
const store = useStore();


// Correct way to use getters from Vuex
const services = computed(() => store.getters["services/filterservices"]);
const create= computed(()=>store.state.services.create)
const message=computed(()=>store.state.services.message)
const openUpdateModal = (service) => {
  console.log("Opening modal for:", service.service_id); // Debugging log
  store.dispatch("servicemodal/openModal", service);

};
watch(create, (newValue) => {
  if (newValue === true || newValue===false) {
    setTimeout(() => {
      store.commit("services/UPDATE_CREATE"); // Reset after 3 seconds
    }, 3000);
  }
});
</script>


<template>
    <div><NavBar></NavBar></div>

    <div><SearchBar module="services"></SearchBar></div>


    <div class="container mt-3">
    <h2 class="text-center mb-4 text-dark fw-bold">Services</h2>
    <SuccessRegister :created="create" :message="message"></SuccessRegister>
    <div class="table-responsive">
        <table class="table table-bordered table-striped table-hover text-center align-middle">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Image</th>
                    <th>Service Name</th>
                    <th>Profession</th>
                    <th>Price</th>
                    <th>Update/Delete</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(service,index) in services" :key="service.service_id">
                    <td>{{index+1 }}</td>
                    <td class="img-thumbnail">
                        <img :src="service.image_url" alt="Product 1" style="width: 100px; height: 100px;" >
                    </td>
                    <td>{{ service.servicename }}</td>
                    <td>{{ service.profession }}</td>
                    <td>{{ service.base_price }}</td>
                    <td>
                        <button class="btn btn-secondary btn-lg me-2" @click="openUpdateModal(service)" >Update </button>
                        <button  class="btn btn-danger btn-lg"> Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div>
            <RouterLink class="btn btn-secondary btn-lg" to="/create-service">Create Service</RouterLink>
        </div>
    </div>
</div>
<ServiceUpdate></ServiceUpdate>
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

