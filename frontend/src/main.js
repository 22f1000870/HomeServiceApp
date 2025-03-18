
import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootstrap/dist/js/bootstrap";
import CreateStore from './store';


// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'



const app = createApp(App)

app.use(router)
app.use(CreateStore)


app.mount('#app')
