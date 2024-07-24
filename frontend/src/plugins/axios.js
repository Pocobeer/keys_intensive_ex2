import axios from 'axios'
import store from "@/store";

const instance = axios.create({
    baseURL: 'http://pocobor.pythonanywhere.com/'
})

instance.interceptors.request.use((config)=>{
    const token = store.state.auth.token;

    if(token) {
        config.headers.Authorization = `Token ${token}`
    }

    return config
}, (error) => {
    if (error.status === 401) {
        store.commit('removeToken')
    }
    return Promise.reject(error)
})

export default {
    install(Vue) {
        Vue.prototype.$ajax = instance
    }
}