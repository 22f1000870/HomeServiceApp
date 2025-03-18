import axios from "axios"
import { handleTokenRefresh } from "@/utility/refreshtoken"
export default {
    namespaced:true,

    state:{
        professionals:[],
        professional_count:0,
        professional_request:[],
        professional_request_count:0,
        searchQuery:''
        },
    mutations:{
        SET_PROFESSIONAL(state,professionals){
            state.professionals=professionals
        },
        SET_PROFESSIONAL_COUNT(state,professionalcount){
            state.professional_count=professionalcount
        },
        SET_PROFESSIONAL_REQUEST(state,professional_request){
            state.professional_request=professional_request
        },
        SET_PROFESSIONAL_REQUEST_COUNT(state,professional_request_count){
            state.professional_request_count=professional_request_count
        },
        SET_SEARCH_QUERY(state,searchQuery){
            state.searchQuery=searchQuery
        }
    },
    actions:{
        async fetchProfessionals({commit}) {
            try {
                const response = await axios.get('http://127.0.0.1:5000/professionals',{
                    headers:{
                        Authorization:`Bearer ${sessionStorage.getItem('access_token')}`
                    }
                })

                if(response.status===200){
                    commit('SET_PROFESSIONAL',response.data.professionals)
                    commit('SET_PROFESSIONAL_COUNT',response.data.professionalcount)
                    commit('SET_PROFESSIONAL_REQUEST',response.data.professional_request)
                    commit('SET_PROFESSIONAL_REQUEST_COUNT',response.data.professional_request_count)
                }
            } catch(error){
                if (error.response && (error.response.status === 401 || error.response.status === 422)) {
                    const newToken = await handleTokenRefresh()
                    if (newToken) {
                      await this.fetchProfessionals() // Retry with the new token
                    }
                  }
                console.error(error)
            }
        }
    },
    getters:{
        filteredData: (state) => (viewType) => {
            if (!state.searchQuery) {
              return viewType === "professionals" ? state.professionals : state.professional_request;
            }
      
            return viewType === "professionals"
              ? state.professionals.filter((professional) =>
                professional.name.toLowerCase().includes(state.searchQuery.toLowerCase()) ||
                professional.profession.toLowerCase().includes(state.searchQuery.toLowerCase()) || 
                String(professional.pincode).includes(state.searchQuery))
                
                : state.professional_request.filter((request) =>
                    request.name.toLowerCase().includes(state.searchQuery.toLowerCase()) ||
                    request.profession.toLowerCase().includes(state.searchQuery.toLowerCase()) || 
                    String(request.pincode).includes(state.searchQuery) //
                );
          }
    }
}