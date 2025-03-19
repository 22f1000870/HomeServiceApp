import axios from "axios"
import { handleTokenRefresh } from "@/utility/refreshtoken"
export default {
    namespaced:true,

    state:{
        services:[],
        serviceCount:0,
        searchQuery:'',
        create:null,
        message:''
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
        },
        UPDATE_SERVICE(state,payload){
            const index = state.services.findIndex(service => service.service_id === payload.service_id);
            if (index !== -1) {
                state.services[index] = { ...state.services[index], ...payload};
            }
        },
        UPDATE_CREATE_TRUE(state){
            state.create=true
        },
        UPDATE_MESSAGE(state,message){
            state.message=message
        },
        UPDATE_CREATE_FALSE(state){
            state.create=false
        },
        UPDATE_CREATE(state){
            state.create=null
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
        },

        async updateService ({commit},payload){
            try{
                const response= await axios.put('http://127.0.0.1:5000/updateservice',payload,{
                    headers:{
                        Authorization:`Bearer ${sessionStorage.getItem('access_token')}`
                    }
                })
                if(response.status===201){
                    commit('UPDATE_SERVICE',payload)
                    commit('UPDATE_CREATE_TRUE')
                    commit('UPDATE_MESSAGE',response.data.message)
                }else {
                    commit('UPDATE_CREATE_FALSE')
                    commit('UPDATE_MESSAGE',response.data.message)
                  }
            } catch(error){
                if (error.response && (error.response.status === 401 || error.response.status === 422)) {
                    const newToken = await handleTokenRefresh()
                    if (newToken) {
                      await this.updateService(payload)// Retry with the new token
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