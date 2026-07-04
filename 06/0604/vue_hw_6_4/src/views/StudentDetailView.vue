<template>
    <div>
        <h1>학생 상세 정보 페이지입니다.</h1>
        <p>이름: {{ route.params.name }}</p>
    </div>
</template>

<script setup>
import {useRoute} from 'vue-router'

const route = useRoute()
console.log(route.params.name)
</script>

<style scoped>

</style>