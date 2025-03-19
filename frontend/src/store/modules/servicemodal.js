export default {
    namespaced: true,
  
    state: {
      isModalOpen: false,
      selectedService: null,
    },
  
    mutations: {
      OPEN_MODAL(state, service) {
        console.log("Vuex Mutation: OPEN_MODAL triggered");
        state.isModalOpen = true;
        state.selectedService = service;
      },
      CLOSE_MODAL(state) {
        console.log("Vuex Mutation: CLOSE_MODAL triggered");
        state.isModalOpen = false;
        state.selectedService = null;
      },
      UPDATE_SELECTED_SERVICE(state, updatedService) {
        console.log("UPDATE SERVICE MUTATION",updatedService.service_id)
        state.selectedService = { ...state.selectedService, ...updatedService };
      },
    },
  
    actions: {
      openModal({ commit }, service) {
        commit("OPEN_MODAL", service);
      },
      closeModal({ commit }) {
        commit("CLOSE_MODAL");
      },
      updateSelectedService({ commit }, updatedService) {
        commit("UPDATE_SELECTED_SERVICE", updatedService);
      },
    },
  
    getters: {
      isModalOpen: (state) => state.isModalOpen,
      selectedService: (state) => state.selectedService,
    },
  };
  