<script setup lang="ts">
  const { data: djangoapp } = await useFetch("http://djangoapp:8000/api/post/");
  const { data: api } = await useFetch("/api");
</script>

<template>
  <div>
    <span>Response from djangoapp</span>
    <div>
      <pre>
                {{ djangoapp }}
            </pre
      >
    </div>
  </div>
  <div>
    <span>Response from api</span>
    <div>
      <pre>{{ api }}</pre>
    </div>
  </div>
</template>
