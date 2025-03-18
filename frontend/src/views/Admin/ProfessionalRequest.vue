<script setup lang="js">
import NavBar from '@/components/navbar/NavBar.vue';
import axios from 'axios';
import { computed,ref,watch} from 'vue';
import { useStore } from 'vuex';
import { handleTokenRefresh } from '@/utility/refreshtoken';
import SuccessRegister from '@/components/popup/SuccessRegister.vue';
const store = useStore();
const professional_request = computed(()=> store.state.professionals.professional_request)
const create=ref(null)
const message=ref('')
const reject= async (username)=>{

    try {
        const response= await axios.delete(`http://127.0.0.1:5000/professional/reject/${username}`,{
            headers:{
                Authorization:`Bearer ${sessionStorage.getItem('access_token')}`
            }
        })
        if( response.status===200 ){
            create.value=false
            message.value=response.data.message
            store.dispatch('professionals/fetchProfessionals')
        } 
    }catch(error){
        if (error.response && (error.response.status === 401 || error.response.status === 422)) {
        const newToken = await handleTokenRefresh()
        if (newToken) {
        await reject(username) // Retry with the new token
        }
    }
    }

}
const accept= async (username)=>{

try {
    const response= await axios.post(`http://127.0.0.1:5000/professional/accept/${username}`,{},{
        headers:{
            Authorization:`Bearer ${sessionStorage.getItem('access_token')}`
        }
    })
    if( response.status===201 ){
        create.value=true
        message.value=response.data.message
        store.dispatch('professionals/fetchProfessionals')
    } 
}catch(error){
    if (error.response && (error.response.status === 401 || error.response.status === 422)) {
    const newToken = await handleTokenRefresh()
    if (newToken) {
    await accept(username) // Retry with the new token
    }
}
}

}
watch(create, (newValue) => {
  if (newValue===true) {
    setTimeout(() => {
      create.value=null
    }, 4000)
  } else if (newValue === false) {
    setTimeout(()=> {
      create.value=null
    }, 4000)
  }
})
</script>


<template>
    <div><NavBar></NavBar></div>

    <div class="container mt-5">
    <h2 class="text-center mb-4 text-dark fw-bold">Professional Request</h2>
    
    <div class="table-responsive">
        
        <table class="table table-bordered table-striped table-hover text-center align-middle">
            <SuccessRegister :created="create" :message="message"></SuccessRegister>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Image</th>
                    <th>Name</th>
                    <th>Profession</th>
                    <th>Experience</th>
                    <th>Pincode</th>
                    <th>Accept/Reject</th>
                    
                </tr>
            </thead>
            <tbody>

                <tr v-for="(profession,index) in professional_request" :key="profession.id">
                    <td>{{index+1 }}</td>
                    <td class="img-thumbnail">
                        <img :src="profession.image_url" alt="Product 1" style="width: 100px; height: 100px;" >
                    </td>
                    <td>{{ profession.name }}</td>
                    <td>{{ profession.profession }}</td>
                    <td>{{ profession.experience }}</td>
                    <td>{{ profession.pincode }}</td>
                    <td> <button @click="accept(profession.username)" class="btn btn-success btn-lg me-2" >Accept </button>
                        <button @click="reject(profession.username)" class="btn btn-danger btn-lg"> Reject</button>
                    </td>
                </tr>
            </tbody>
        </table>
        
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

