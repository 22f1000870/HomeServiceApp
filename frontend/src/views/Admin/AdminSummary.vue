<script lang="js" setup>
import NavBar from '@/components/navbar/NavBar.vue';
import { computed } from 'vue';
import { useStore } from 'vuex';

const store=useStore();
const user = computed(()=>store.state.userstate.user)
</script>

<template>
   <div>
    <NavBar :user="user"></NavBar>
   </div>
</template>