import axios from "axios";

export const loginStore = {
    namespaced: true,
    state: () => ({
        token: localStorage.getItem('token') || ''
    }),
    getters: {
        isLoggedIn: state => !!state.token
    },
    mutations: {
        setToken(state, token) {
            state.token = token
        },
        removeToken(state) {
            state.token = ''
            localStorage.setItem('token', '')
        }
    },
    actions: {
        async login({commit}, {username, password, router}) {
            try {
                const response = await axios.post('http://pocobor.pythonanywhere.com/api-token-auth/', {
                    'username': username,
                    'password': password
                })
                const token = response.data.token
                await commit('setToken', token)
                router.push('/')
            } catch (e) {
                if (e.response.status === 400) {
                    console.log('Неправильные данные')
                } else {
                    console.log('Ошибка')
                    console.log(e)
                }
            }
        }
    }
}
