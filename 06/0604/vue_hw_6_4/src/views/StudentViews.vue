<template>
    
    <h1>학생 상세 정보 목록입니다.</h1>
    <div v-for="student in students" :key="student.name">
        <p @click="goToDetail(student.name)">{{ student.name }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const goToDetail = (studentName) => {
    router.push({
        name: 'studentDetail',
        params: { name: studentName }
    })
}
const students = ref([
    { name: '김하나'},
    { name: '김두리'},
    { name: '김서이'},
])
</script>

<style scoped>

</style>