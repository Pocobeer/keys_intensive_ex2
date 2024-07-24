<template>
  <v-container>
    <v-dialog v-model="showCreateForm">
      <create-form @create="createPovar"></create-form>
    </v-dialog>
    <v-row align="center" no-gutters>
      <v-col cols="12" sm="4">
        <v-select :items="sortOptions" v-model="selectSort" label="Сортировать по"></v-select>
      </v-col>
      <v-col cols="12" sm="4">
        <v-text-field v-model="searchText" label="Поиск"></v-text-field>
      </v-col>
      <v-col cols="12" sm="4" class="text-right">
        <v-btn @click="showCreateForm = true">Добавить повара</v-btn>
      </v-col>
    </v-row>
    <v-list>
      <v-list-item-group v-if="sortedAndSearched.length">
        <v-list-item v-for="povar in sortedAndSearched" :key="povar.id">
          <v-list-item-content>
            <v-list-item-title>{{ povar.name }}</v-list-item-title>
            <v-list-item-subtitle>Возраст: {{ povar.age }}</v-list-item-subtitle>
            <v-list-item-subtitle>Опыт: {{ povar.experience }}</v-list-item-subtitle>
            <v-list-item-subtitle>Рейтинг: {{ povar.rating }}</v-list-item-subtitle>
            <v-list-item-actions>
              <v-btn @click="removePovar(povar)" color="red">Удалить</v-btn>
            </v-list-item-actions>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
      <v-card v-else>
        <v-card-text>Нет данных</v-card-text>
      </v-card>
    </v-list>
  </v-container>
</template>

<script>
import axios from 'axios';
import CreateForm from "@/components/CreateForm.vue";

export default {
  name: "AppContent",
  components: { CreateForm },
  data() {
    return {
      povars: [],
      showCreateForm: false,
      selectSort: '',
      sortOptions: [
        { value: 'name', name: 'По имени' },
        { value: 'experience', name: 'По опыту' },
      ],
      searchText: ''
    }
  },
  mounted() {
    axios.get('api/povars/')
      .then(response => {
        console.log('API Response:', response.data);
        const results = response.data.results;
        console.log('Extracted Results:', results);

        if (Array.isArray(results)) {
          this.povars = results.map(povar => ({
            id: povar.id,
            name: povar.Povar_name,
            experience: povar.Povar_experience,
            rating: povar.Povar_rating,
            age: povar.Povar_age
          }));
          console.log('Transformed Povars:', this.povars);
        } else {
          console.error('Expected array but got:', results);
          this.povars = [];
        }
      })
      .catch(error => {
        console.error('Error fetching povars:', error);
        this.povars = [];
      });
  },
  methods: {
    createPovar(data) {
      console.log(data)
      this.povars.push(data)
    },
    removePovar(povar) {
      const url = `api/povars/${povar.id}`;
      console.log('Deleting Povar URL:', url);

      axios.delete(url)
        .then(() => {
          this.povars = this.povars.filter(elem => elem.id !== povar.id);
        })
        .catch(error => {
          console.error('Error removing povar:', error.response ? error.response.data : error.message);
        });
    }
  },
  computed: {
    sortedPovars() {
      return [...this.povars].sort((pov1, pov2) => {
        const value1 = pov1[this.selectSort];
        const value2 = pov2[this.selectSort];
        if (typeof value1 === 'string' && typeof value2 === 'string') {
          return value1.localeCompare(value2);
        }
        return (value1 > value2) ? 1 : (value1 < value2) ? -1 : 0;
      });
    },
    sortedAndSearched() {
      return this.sortedPovars.filter(povar => povar.name.toLowerCase().includes(this.searchText.toLowerCase()))
    }
  }
}
</script>

<style scoped>
.text-right {
  text-align: right;
}
</style>
