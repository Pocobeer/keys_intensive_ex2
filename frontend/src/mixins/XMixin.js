export default {
    data() {
        return {
            xvall: 'Владимир'
        }
    },
    mounted() {
        console.log('Я использую миксин')
    },
    methods: {
        hello() {
            console.log(`Привет меня зовут ${this.xvall}`)
        }
    }
}
