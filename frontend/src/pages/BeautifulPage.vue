<template>
    <v-app>
        <v-app-bar app>
            <vue-app-header></vue-app-header>
        </v-app-bar>
        <v-main>
            <v-container>
                <v-layout justify-center>
                <v-flex xs9>
                    <v-layout row class="mt-1">
                    <v-flex xs3>
                        <v-text-field label="Поиск" placeholder="Что ищем?" rounded outlined></v-text-field>
                    </v-flex>
                    <v-flex class="ml-2" grow>
                        <v-select :items="items" label="Outlined style" outlined></v-select>
                    </v-flex>
                    <v-flex class="ml-2" shrink>
                        <v-btn outlined color="primary">Добавить</v-btn>
                    </v-flex>
                    </v-layout>
        
                    <v-layout row class="mt-5" justify-space-between>
                    <template v-if="povars && povars.length">
                        <v-card max-width="344" outlined v-for="povar in povars" :key="`povar-${povar.id}`" elevation="2">
                        <v-list-item three-line>
                            <v-list-item-content>
                            <div class="text-overline mb-4">
                                Карточка повара № {{ povar.id }}
                            </div>
        
                            <v-list-item-subtitle>Имя: {{ povar.name }}</v-list-item-subtitle>
                            <v-list-item-subtitle>Возраст: {{ povar.age }}</v-list-item-subtitle>
                            <v-list-item-subtitle>Описание: {{ povar.description }}</v-list-item-subtitle>
                            <v-list-item-subtitle>Курс: {{ povar.course }}</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
        
                        <v-card-actions>
                            <v-btn outlined rounded color="success">
                            Изменить
                            </v-btn>
                            <v-btn outlined rounded color="error">
                            Удалить
                            </v-btn>
                        </v-card-actions>
                        </v-card>
                    </template>
                    <template v-else>
                        <v-card>
                        <v-list-item>
                            <v-list-item-content>
                            <v-list-item-subtitle>Нет данных</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                        </v-card>
                    </template>
                    </v-layout>
                </v-flex>
                </v-layout>
            </v-container>
        </v-main>
    </v-app>
  </template>
  
  <script>
  import axios from 'axios';
  import VueAppHeader from '@/components/VueAppHeader.vue';
  
  export default {
    name: "BeautifulPage",
    components: { VueAppHeader },
    data() {
      return {
        items: ['Foo', 'Bar', 'Fizz'],
        povars: [],
      }
    },
    mounted() {
      axios.get('api/povars/').then((response) => {
        this.povars = response.data;
      }).catch(error => {
        console.error("Error loading povars:", error);
        this.povars = [];
      });
    }
  }
  </script>
  
  <style scoped>
  </style>