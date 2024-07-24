import PovarPage from "@/pages/PovarPage.vue";
import DishPage from "@/pages/DishPage.vue";
import IngredientPage from "@/pages/IngredientPage.vue";
import LoginForm from "@/components/LoginForm.vue";
import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: PovarPage,
        meta: {requiresAuth: true}
    },
    {
        path: '/login',
        component: LoginForm,
        meta: {requiresAuth: false}
    },
    {
        path: '/PovarPage',
        component: PovarPage,
        meta: {requiresAuth: true}
    },
    {
        path: '/DishPage',
        component: DishPage,
        meta: {requiresAuth: true}
    },
    {
        path: '/IngredientPage',
        component: IngredientPage,
        meta: {requiresAuth: true}
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, form, next) => {
    const token = store.state.auth.token
    console.log(token)
    if (to.meta.requiresAuth && !token) {
        next('/login')
    } else {
        next();
    }
})

export default router;
