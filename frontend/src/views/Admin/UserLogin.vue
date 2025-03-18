<script lang="js" setup>
import { computed, ref, watch } from 'vue'
import axios from 'axios'
import router from '@/router'
import { useStore } from 'vuex'
import { handleImage, ImageLoad, SelectedFile, fileName } from '@/utility/imageLoad'
import SuccessRegister from '@/components/popup/SuccessRegister.vue'
const error = ref(null)
const success = ref(null)
const username = ref('')
const password = ref('')
const fullname=ref('')
const experience = ref(0)
const pincode = ref(0)
const skill=ref('')
const store = useStore()
const profession = computed(()=> store.state.profInfo.professions)
const create=ref(null)
const message=ref('')

const professions = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/prof_info')
    store.commit('profInfo/SET_PROFESSION',response.data.professions)
    console.log(response.data.professions)
  } catch(err) {
    error.value='No professionals created'
  } finally {
    console.log('professionals')
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

const CustomerCreate = async () => {
  if (pincode.value) {
    let formData = new FormData()
    formData.append('username',username.value)
    formData.append('password',password.value)
    formData.append('name',fullname.value)
    formData.append('pincode',pincode.value)
    formData.append('image',fileName.value)

    try {
      const response= await axios.post('http://127.0.0.1:5000/createcustomer',formData)
      if(response.status===201){
        create.value=true
        message.value=response.data.message
      }
    } catch(err) {
      console.error('Error',err)
    } finally {
      ImageLoad.value=null
      username.value=''
      password.value=''
      SelectedFile.value=null
      document.getElementById('imageUpload').value=''
      pincode.value=0
      fileName.value=''
      fullname.value=''
      
    }

  } else {
    alert('Invalid Pincode')
  }
}
const profReq = async () => {
  if (pincode.value > 0) {
    let formData = new FormData()
    formData.append('username',username.value)
    formData.append('password',password.value)
    formData.append('name',fullname.value)
    formData.append('experience',experience.value)
    formData.append('pincode',pincode.value)
    formData.append('profession',skill.value)
    formData.append('image',fileName.value)
    formData.append('file',SelectedFile.value)
    try {
      const response= await axios.post('http://127.0.0.1:5000/prof_info',formData)
      if (response.status===201){
        create.value=true
        message.value=response.data.message

      }
    } catch(err) {
      console.error('Error submitting form:', err)
    } finally {
      ImageLoad.value=null
      username.value=''
      password.value=''
      SelectedFile.value=null
      document.getElementById('imageUpload').value=''
      fullname.value=''
      pincode.value=0
      skill.value=''
      experience.value=0
    }
  } else {
    alert('Invalid Pincode')
  }
}
const login = async () => {
  error.value = null
  success.value = null

  try {
    const response = await axios.post('http://127.0.0.1:5000/login', {
      username: username.value,
      password: password.value
    })
    success.value = 'Login Successfull'
    console.log('Tokens', response.data.access_token)
    const access_token = response.data.access_token
    const refresh_token = response.data.refresh_token
    store.commit('userstate/SetuserType', response.data.role)
    sessionStorage.setItem('access_token', access_token)
    localStorage.setItem('refresh_token', refresh_token)
    router.push({ name: 'Dashboard' })
  } catch (err) {
    error.value = 'Invalid Credentials'
    console.log('error', err)
  } finally {
    console.log('Login attempt successfull')
  }
}
</script>

<template>
  <!-- Login 4 - Bootstrap Brain Component -->
  <!-- <link rel="stylesheet" href="https://unpkg.com/bootstrap@5.3.3/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="https://unpkg.com/bs-brain@2.0.4/components/logins/login-4/assets/css/login-4.css"> -->
  <!-- Bootstrap Icons CDN -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">

  <section class="p-3 p-md-4 p-xl-5">
    <div class="container">
      <div class="card border-light-subtle shadow-sm">
        <h1 style="text-align: center">Home Service Application</h1>
        <div class="row g-0">
          <div class="col-12 col-md-6">
            <img
              class="img-fluid rounded-start w-100 h-100 object-fit-cover"
              loading="lazy"
              src="@/assets/logo.jpg"
              alt="BootstrapBrain Logo"
            />
          </div>
          <div class="col-12 col-md-6">
            <div class="card-body p-3 p-md-4 p-xl-5">
              <div class="row">
                <div class="col-12">
                  <div class="mb-5">
                    <h3>Log in</h3>
                  </div>
                </div>
              </div>
              <form @submit.prevent="login">
                <div class="row gy-3 gy-md-4 overflow-hidden">
                  <div class="col-12">
                    <label for="username" class="form-label"
                      >Username <span class="text-danger">*</span></label
                    >
                    <input
                      type="text"
                      class="form-control"
                      name="username"
                      id="username"
                      v-model="username"
                      required
                    />
                  </div>
                  <div class="col-12">
                    <label for="password" class="form-label"
                      >Password <span class="text-danger">*</span></label
                    >
                    <input
                      type="password"
                      class="form-control"
                      name="password"
                      id="password"
                      v-model="password"
                      required
                    />
                  </div>

                  <div class="col-12">
                    <div class="d-grid">
                      <button class="btn bsb-btn-xl btn-primary" type="submit">Log in</button>
                    </div>
                  </div>
                </div>
              </form>
              <div class="row">
                <div class="col-12">
                  <hr class="mt-5 mb-4 border-secondary-subtle" />
                  <div class="d-flex gap-2 gap-md-4 flex-column flex-md-row justify-content-md-end">
                    <!-- <a href="#!" class="link-primary text-decoration-underline">Create new account</a> -->
                    <!-- Button to Open Modal -->
                    <button type="button"  class="btn btn-link text-primary" data-bs-toggle="modal" data-bs-target="#authModal">
                      Create Account
                    </button>

                    <!-- Modal -->
                    <div class="modal fade" id="authModal" tabindex="-1" aria-labelledby="authModalLabel" aria-hidden="true">
                      <div class="modal-dialog modal-dialog-scrollable">  <!-- ✅ Make modal scrollable -->
                        <div class="modal-content">
                          <div class="modal-header">
                            <ul class="nav nav-tabs card-header-tabs" id="authTab" role="tablist">
                              <li class="nav-item" role="presentation">
                                <button class="nav-link active text-dark " id="customer-tab" data-bs-toggle="tab" data-bs-target="#customer" type="button" role="tab">Customer Registration</button>
                              </li>
                              <li class="nav-item" role="presentation">
                                <button class="nav-link text-dark" id="register-tab" data-bs-toggle="tab" data-bs-target="#register" type="button" role="tab">Professional Registration</button>
                              </li>
                            </ul>
                            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                          </div>
                          <div class="modal-body">
                            <div class="tab-content">
                            
                              <div class="tab-pane fade show active" id="customer" role="tabpanel">
                                <h5 class="text-center">Customer Register</h5>
                                <form @submit.prevent="CustomerCreate">
                                  <div class="mb-3 d-flex justify-content-center align-items-center">
                                    <label for="imageUpload" class="image-container">
                                      <i v-if="!ImageLoad" class="bi bi-person-plus-fill fs-2"></i>
                                      <img v-if="ImageLoad" :src="ImageLoad" alt="Profile Image" class="profile-image" />
                                      <!-- <img :src="imageUrl || 'https://via.placeholder.com/150'" alt="Profile Image" class="profile-image" /> -->
                                      <input type="file" id="imageUpload" @change="handleImage" accept="image/*" class="file-input"  required/>
                                    </label>
                                  </div>

                                  <div class="mb-3">
                                    <label for="registerName" class="form-label">Full Name</label>
                                    <input v-model="fullname" type="text" class="form-control" id="registerName" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="registerUser" class="form-label">Username</label>
                                    <input v-model="username" type="text" class="form-control" id="registerUser" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="registerPassword" class="form-label">Password</label>
                                    <input  v-model="password" type="password" class="form-control" id="registerPassword" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="registerCode" class="form-label">Pincode</label>
                                    <input v-model="pincode" type="number" class="form-control" id="registerCode" required>
                                  </div>

                                  <button type="submit" class="btn btn-success w-100">Register</button>
                                </form>
                              </div>

                              <!-- Register Section -->
                              <SuccessRegister :created="create" :message="message"></SuccessRegister>
                              <div class="tab-pane fade" @click="professions" id="register" role="tabpanel">
                                <h5 class="text-center"> Professional Register</h5>
                                <form @submit.prevent="profReq">
                                  <div class="mb-3 d-flex justify-content-center align-items-center">
                                    <label for="imageUpload" class="image-container">
                                      <i v-if="!ImageLoad" class="bi bi-person-plus-fill fs-2"></i>
                                      <img v-if="ImageLoad" :src="ImageLoad" alt="Profile Image" class="profile-image" />
                                      <!-- <img :src="imageUrl || 'https://via.placeholder.com/150'" alt="Profile Image" class="profile-image" /> -->
                                      <input type="file" id="imageUpload" @change="handleImage" accept="image/*" class="file-input"  required/>
                                    </label>
                                  </div>
                                  
                                  <div class="mb-3">
                                    <label for="registerName" class="form-label">Full Name</label>
                                    <input v-model="fullname" type="text" class="form-control" id="registerName" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="registerUser" class="form-label">Username</label>
                                    <input v-model="username" type="text" class="form-control" id="registerUser" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="registerPassword" class="form-label">Password</label>
                                    <input  v-model="password" type="password" class="form-control" id="registerPassword" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="registerCode" class="form-label">Pincode</label>
                                    <input v-model="pincode" type="number" class="form-control" id="registerCode" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="registerExp" class="form-label">Experience</label>
                                    <input v-model="experience" type="number" class="form-control" id="registerExp" required>
                                  </div>
                                  <div class="mb-3">
                                    <label for="profession" class="form-label">Select Profession</label>
                                    <select v-model="skill" class="form-control" id="profession" required>
                                      <option value="" disabled selected>Choose your profession</option>
                                      <option v-for="prof in profession" :key="prof" :value="prof">
                                        {{ prof }}
                                      </option>
                                      
                                    </select>
                                  </div>
                                  <button type="submit" class="btn btn-success w-100">Register</button>
                                </form>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="css" scoped>
 @import '/src/assets/css/profileimage.css'
</style>

