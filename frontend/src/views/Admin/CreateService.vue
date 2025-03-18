<script lang="js" setup>
import axios from 'axios'
import { ref, watch } from 'vue'
import { onMounted, onUnmounted } from 'vue'
import SuccessRegister from '@/components/popup/SuccessRegister.vue'
import { handleTokenRefresh } from '@/utility/refreshtoken'
import navbar from '@/components/navbar/NavBar.vue'
import leafImage from '@/assets/leafs.png';
import { ImageLoad, SelectedFile, handleImage, fileName } from '@/utility/imageLoad'
onMounted(() => {
  document.body.style.color = '#000'
  document.body.style.overflowX = 'hidden'
  document.body.style.height = '100%'
  document.body.style.backgroundImage =`url(${leafImage})`
  document.body.style.backgroundRepeat = 'no-repeat'
  document.body.style.backgroundSize = '100% 100%'
})

onUnmounted(() => {
  document.body.style.backgroundImage = '' // Remove the background when leaving
})

const error = ref({
  servicename: '',
  profession: '',
  price: ''
})
const servicename = ref('')
const profession = ref('')
const price = ref(0)
const success = ref({
  servicename: false,
  profession: false,
  price: false
})
const create = ref(null)
const message = ref('')



const FieldValidation = (fieldname, value, errormessage) => {
  if (value == '' || value == 0) {
    error.value[fieldname] = errormessage
  } else {
    error.value[fieldname] = ''
    success.value[fieldname] = true
  }
}



watch(create, (newValue) => {
  if (newValue===true) {
    setTimeout(() => {
      create.value=null
    }, 4000)
  } else if (newValue === false) {
    setTimeout(()=> {
      create.value=null
    }, 4000)
  }
})

watch([servicename, profession, price], ([newservicename, newprofesssion, newprice]) => {
  FieldValidation('servicename', newservicename, 'Service Name Required')
  FieldValidation('profession', newprofesssion, 'Profession Required')
  FieldValidation('price', newprice, 'Price Required')
})



const CreateService = async () => {
  if (
    success.value.price &&
    success.value.profession &&
    success.value.servicename &&
    SelectedFile.value)
    {
    let formData = new FormData()
    formData.append('servicename', servicename.value)
    formData.append('profession', profession.value)
    formData.append('base_price', price.value)
    formData.append('image', fileName.value)
    formData.append('file', SelectedFile.value)

    try {
      const response = await axios.post('http://127.0.0.1:5000/createservice', formData, {
        headers: {
          Authorization: `Bearer ${sessionStorage.getItem('access_token')}`,
          'Content-Type': 'multipart/form-data'
        }
      })
      if (response.status === 201) {
        create.value=true
        message.value=response.data.message
        console.log(response.data.message)
      }
    } catch (error) {
      if (error.response && (error.response.status === 401 || error.response.status === 422)) {
        const newToken = await handleTokenRefresh()
        if (newToken) {
          await CreateService() // Retry with the new token
        } 
      }
      else if (error.response && error.response.status===400) {
        create.value=false
      }
      } finally {
      // Reset form and feedback
      servicename.value = ''
      profession.value = ''
      price.value = 0
      ImageLoad.value = null
      success.value = { servicename: false, profession: false, price: false }
      SelectedFile.value = null
      document.getElementById('upload').value = '';
      fileName.value=''
    }
  }
}
</script>

<template class="body">
  <navbar></navbar>
  <div class="container-fluid px-1 py-5 mx-auto">
    <div class="row d-flex justify-content-center">
      <div class="col-xl-7 col-lg-8 col-md-9 col-11 text-center">
        <div class="card">
          <SuccessRegister :created="create" :message="message"></SuccessRegister>
          <form class="form-card" @submit.prevent="CreateService">
            <h3>CREATE SERVICE</h3>
            <div class="row justify-content-between text-left">
              <div class="form-group col-sm-6 flex-column d-flex">
                <label class="form-control-label px-3">Service name</label>
                <input
                  type="text"
                  v-model="servicename"
                  id="fname"
                  name="fname"
                  placeholder="Enter Service name"
                  @input="FieldValidation"
                /><span v-if="error.servicename" class="text-danger">
                  *{{ error.servicename }}</span
                >
              </div>
              <div class="form-group col-sm-6 flex-column d-flex">
                <label class="form-control-label px-3">Profession</label>
                <input
                  type="text"
                  v-model="profession"
                  id="lname"
                  name="lname"
                  placeholder="Profession"
                  @input="FieldValidation"
                /><span v-if="error.profession" class="text-danger"> *{{ error.profession }}</span>
              </div>
            </div>
            <div class="row justify-content-between text-left">
              <div class="form-group col-sm-6 flex-column d-flex">
                <label class="form-control-label px-3"
                  >Base Price<span class="text-danger"> </span
                ></label>
                <input
                  type="number"
                  v-model="price"
                  id="price"
                  name="price"
                  placeholder="Base Price"
                  @input="FieldValidation"
                />
                <span v-if="error.price" class="text-danger"> *{{ error.price }}</span>
              </div>
              <div class="input-group mb-3 px-2 py-2 rounded-pill bg-white shadow-sm">
                <input
                  id="upload"
                  type="file"
                  @change="handleImage"
                  accept="image/*"
                  class="form-control border-0"
                />
                <!-- <label id="upload-label" for="upload" class="font-weight-light text-muted">Choose file</label> -->
                <div class="input-group-append">
                  <label for="upload" class="btn btn-dark m-0 rounded-pill px-4">
                    <i class="fa fa-cloud-upload mr-2 text-white"></i
                    ><small class="text-uppercase font-weight-bold text-white"
                      >Choose file</small
                    ></label
                  >
                </div>
              </div>
            </div>

            <div class="row justify-content-between text-left">
              <div class="input-group mb-3 px-2 py-2 rounded-pill bg-white shadow-sm"></div>

              <!-- Uploaded image area-->
              <p class="font-italic text-white text-center">
                The image uploaded will be rendered inside the box below.
              </p>
              <div class="image-area h-50 w-50 mx-auto">
                <img
                  id="imageResult"
                  :src="ImageLoad"
                  alt="No Image"
                  class="img-fluid rounded shadow-sm mx-auto h-50 w-50 d-block"
                />
              </div>
            </div>
            <div class="row justify-content-center m-4">
              <div class="form-group col-sm-6">
                <button type="submit" class="btn btn-success">Create Service</button>
              </div>
            </div>
            
              <!-- <RouterLink class="btn btn-dark btn-lg" to="/admin/services">Go Back</RouterLink> -->
            
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped>
@import '/src/assets/css/createservice.css';
</style>
