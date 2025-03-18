import {ref} from 'vue'
export const ImageLoad = ref(null)
export const SelectedFile = ref(null)
export const fileName = ref('')

export const handleImage = (event) => {
  const file = event.target.files[0]
  if(file && file.type.startsWith('image/')) {
    SelectedFile.value=file
    fileName.value=file.name
    const reader = new FileReader()
    reader.onload = (e)=> {
      ImageLoad.value=e.target.result
    }
    reader.readAsDataURL(file)
  } else {
    ImageLoad.value = null
    alert('Please select a valid image file.')
  }
}