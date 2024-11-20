<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
        <RouterLink :to="{ name: 'signup' }">Signup</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
