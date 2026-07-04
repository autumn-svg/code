<template>
  <div>
    <MainPage />  
    <nav>
    <RouterLink to="/">Some</RouterLink> |
    <RouterLink to="/other">Other</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import MainPage from './components/MainPage.vue';



</script>

<style scoped>

</style>