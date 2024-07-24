import Vue from 'vue'
import App from './App.vue'
import components from '@/components/UI'
import router from "@/router/router";
import axios from "@/plugins/axios";
import store from './store'

Vue.config.productionTip = false

components.forEach(component => {
  Vue.component(component.name, component)
})

Vue.use(axios)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
