<script setup lang="js">
import { RouterLink } from 'vue-router';
import { computed } from 'vue';
import { useStore } from 'vuex';
const store=useStore();
// const props= defineProps({serviceCount:Number})
const serviceCount = computed(() => store.state.services.serviceCount)
const professional_request_count = computed(()=>store.state.professionals.professional_request_count)
const professional_count = computed(()=>store.state.professionals.professional_count)
</script>
<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css" integrity="sha256-mmgLkCYLUQbXn0B1SRqzHar6dCnv9oZFPEC1g1cwlkk=" crossorigin="anonymous" />

        <div class="container">
            <div class="row ">
                <div class="col-xl-6 col-lg-6">
                    <RouterLink to="/admin/services" custom v-slot="{ navigate }">
                    <div @click="navigate" style="cursor: pointer;">
                    <div class="card l-bg-cherry">
                        
                        <div class="card-statistic-3 p-4">
                            
                            <div class="card-icon card-icon-large"><i class="fas fa-shopping-cart"></i></div>
                            <div class="mb-4">
                                
                                    
                                <h5>Services</h5>
                                    
                                
                            </div>
                            <div class="row align-items-center mb-2 d-flex">
                                <div class="col-8">
                                    <h2 class="d-flex align-items-center mb-0">
                                        {{ serviceCount }}
                                    </h2>
                                </div>
                                <!-- <div class="col-4 text-right">
                                    <span>12.5% <i class="fa fa-arrow-up"></i></span>
                                </div> -->
                            </div>
                            <!-- <div class="progress mt-1 " data-height="8" style="height: 8px;">
                                <div class="progress-bar l-bg-cyan" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" style="width: 25%;"></div>
                            </div> -->
                        </div>
                    </div> 
                    </div>
                    </RouterLink>
                </div>
                <div class="col-xl-6 col-lg-6">
                    <div class="card l-bg-blue-dark">
                        <div class="card-statistic-3 p-4">
                            <div class="card-icon card-icon-large"><i class="fas fa-users"></i></div>
                            <div class="mb-4">
                                <h5 class="card-title mb-0">Professionals</h5>
                            </div>
                            <div class="row align-items-center mb-2 d-flex">
                                <div class="col-8">
                                    <h2 class="d-flex align-items-center mb-0">
                                        {{ professional_count }}
                                    </h2>
                                </div>
                                <!-- <div class="col-4 text-right">
                                    <span>9.23% <i class="fa fa-arrow-up"></i></span>
                                </div> -->
                            </div>
                            <!-- <div class="progress mt-1 " data-height="8" style="height: 8px;">
                                <div class="progress-bar l-bg-green" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" style="width: 25%;"></div>
                            </div> -->
                        </div>
                    </div>
                </div>
                <div class="col-xl-6 col-lg-6">
                    <div class="card l-bg-green-dark">
                        <div class="card-statistic-3 p-4">
                            <div class="card-icon card-icon-large"><i class="fas fa-ticket-alt"></i></div>
                            <div class="mb-4">
                                <h5 class="card-title mb-0">Service Request</h5>
                            </div>
                            <div class="row align-items-center mb-2 d-flex">
                                <div class="col-8">
                                    <h2 class="d-flex align-items-center mb-0">
                                        0
                                    </h2>
                                </div>
                                <!-- <div class="col-4 text-right">
                                    <span>10% <i class="fa fa-arrow-up"></i></span>
                                </div> -->
                            </div>
                            <!-- <div class="progress mt-1 " data-height="8" style="height: 8px;">
                                <div class="progress-bar l-bg-orange" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" style="width: 25%;"></div>
                            </div> -->
                        </div>
                    </div>
                </div>
        
                <div class="col-xl-6 col-lg-6">
                    <div class="card l-bg-yellow-dark">
                        <div class="card-statistic-3 p-4">
                            <div class="card-icon card-icon-large"><i class="fas fa-ticket-alt"></i></div>
                            <div class="mb-4">
                                <h5 class="card-title mb-0">FeedBack</h5>
                            </div>
                            <div class="row align-items-center mb-2 d-flex">
                                <div class="col-8">
                                    <h2 class="d-flex align-items-center mb-0">
                                        0
                                    </h2>
                                </div>
                                <!-- <div class="col-4 text-right">
                                    <span>10% <i class="fa fa-arrow-up"></i></span>
                                </div> -->
                            </div>
                            <!-- <div class="progress mt-1 " data-height="8" style="height: 8px;">
                                <div class="progress-bar l-bg-orange" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" style="width: 25%;"></div>
                            </div> -->
                        </div>
                    </div>
                </div>
                <div class="col-xl-6 col-lg-6">
                    <RouterLink to="/admin/professional_request" custom v-slot="{ navigate }">
                    <div @click="navigate" style="cursor: pointer;">
                    <div class="card l-bg-green-dark">
                        <div class="card-statistic-3 p-4">
                            <div class="card-icon card-icon-large"><i class="fas fa-users"></i></div>
                            <div class="mb-4">
                                <h5 class="card-title mb-0">New Professional Request</h5>
                            </div>
                            <div class="row align-items-center mb-2 d-flex">
                                <div class="col-8">
                                    <h2 class="d-flex align-items-center mb-0">
                                        {{ professional_request_count }}
                                    </h2>
                                </div>
                                <!-- <div class="col-4 text-right">
                                    <span>9.23% <i class="fa fa-arrow-up"></i></span>
                                </div> -->
                            </div>
                            <!-- <div class="progress mt-1 " data-height="8" style="height: 8px;">
                                <div class="progress-bar l-bg-green" role="progressbar" data-width="25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" style="width: 25%;"></div>
                            </div> -->
                        </div>
                    </div>
                    </div>
                    </RouterLink>
                </div>
            </div>
        </div>
</template>

<style lang="css" scoped>
    @import '/src/assets/css/Dcard.css'
</style>