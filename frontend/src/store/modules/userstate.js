export default {
    namespaced:true,
    state: {
        user:""
    },
    mutations: {
        SetuserType(state,user) {
            state.user=user
        }
    },
    actions: {},
    getters: {
        user:(state)=>state.user    }
}