export default {
    namespaced:true,
    state: {
        professions:[]
    },
    mutations: {
        SET_PROFESSION(state,professions) {
            state.professions=professions
        }
    }
}