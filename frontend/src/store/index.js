import { createStore } from 'vuex'
import userstate from './modules/userstate'
import profInfo from './modules/profInfo'
import image from './modules/image'
import services from './modules/services'
import professionals from './modules/professionals'
const CreateStore= createStore ({
    modules: {
        userstate,
        profInfo,
        image,
        services,
        professionals
    }
})

export default CreateStore