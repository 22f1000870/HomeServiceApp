<script lang="js" setup>
import NavBar from '@/components/navbar/NavBar.vue';
import {  onMounted } from 'vue';
import { useStore } from 'vuex';

import DashboardCard from '@/components/cards/DashboardCard.vue'
const store=useStore();



onMounted (()=>{
    
        store.dispatch('services/fetchServices')
        store.dispatch('professionals/fetchProfessionals')
})


</script>

<template>
    
    <div>
        <NavBar></NavBar>
        
    </div>
    <div>
        <DashboardCard ></DashboardCard>
    </div>

</template>