<script setup>
import { computed, watch, ref } from "vue";
import { useStore } from "vuex";


const store = useStore();

// Modal open state
const isModalOpen = computed(() => store.getters["servicemodal/isModalOpen"]);

// Get selected service from Vuex
const selectedService = computed(() => store.getters["servicemodal/selectedService"] || {});

// Local reactive state
const serviceData = ref({});

// Watch Vuex selectedService and update local state
watch(selectedService, (newVal) => {
    console.log("Selected Service Data:", newVal); 
    serviceData.value = { ...newVal }; 
}, { immediate: true });

// Close modal function
const closeModal = () => {
  store.dispatch("servicemodal/closeModal");
};

// Handle file upload


// Update service function
const updateService = () => {
  store.dispatch("services/updateService", serviceData.value);
  closeModal();
};
</script>

<template>
  <div v-if="isModalOpen" class="modal-backdrop">
    <div class="modal fade show d-block">
      <div class="modal-dialog modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Update Service</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="updateService">
              
              <div class="mb-3">
                <label class="form-label">Service Name</label>
                <input v-model="serviceData.servicename" type="text" class="form-control" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Profession</label>
                <input v-model="serviceData.profession" type="text" class="form-control" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Base Price</label>
                <input v-model="serviceData.base_price" type="number" class="form-control" required>
              </div>
              <button type="submit" class="btn btn-success w-100">Update Service</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import '/src/assets/css/profileimage.css';

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
