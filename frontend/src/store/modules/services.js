import axios from "axios"
import { handleTokenRefresh } from "@/utility/refreshtoken"
export default {
    namespaced:true,

    state:{
        services:[],
        serviceCount:0,
        searchQuery:''
    },
    mutations: {
        SET_SERVICES(state,services) {
            state.services=services
        },
        SET_SERVICECOUNT(state,count){
            state.serviceCount=count
        },
        SET_SEARCH_QUERY(state,searchQuery){
            state.searchQuery=searchQuery
        }
    },
    actions : {
        async fetchServices({commit}) {
            try {
                const response= await axios.get('http://127.0.0.1:5000/getservices',{
                    headers:{
                        Authorization:`Bearer ${sessionStorage.getItem('access_token')}`
                    }
                })
                if (response.status===200){
                    commit('SET_SERVICES',response.data.services)
                    commit('SET_SERVICECOUNT',response.data.servicecount)
                }
            } catch (error) {
                if (error.response && (error.response.status === 401 || error.response.status === 422)) {
                    const newToken = await handleTokenRefresh()
                    if (newToken) {
                      await this.fetchServices() // Retry with the new token
                    }
                  }
                console.error(error)
            }
        }
    },
    getters:{
        filterservices(state){
            if(!state.searchQuery) return state.services;
            return state.services.filter(service=>
                service.servicename.toLowerCase().includes(state.searchQuery.toLowerCase()))
        }

    }
}