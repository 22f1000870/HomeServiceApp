export default {
    namespaced: true,
    state: {
      image: null, // Store base64 image or file
    },
    mutations: {
      SET_IMAGE(state, image) {
        state.image = image
      }
    },
    actions: {
      uploadImage({ commit }, file) {
        const reader = new FileReader()
        reader.onload = (event) => {
          commit('SET_IMAGE', event.target.result) // Store as base64
        }
        reader.readAsDataURL(file)
      }
    },
    getters: {
      getImage: (state) => state.image
    }
  }
  