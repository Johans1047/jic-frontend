<script lang="ts">
  import "../layout.css"
  import Header from "$lib/components/header.svelte";
  import Footer from "$lib/components/footer.svelte";

  let { children } = $props();
</script>

<div class="app">
  <Header />
  <main class="pt-18 overflow-x-hidden">
    {@render children()}
  </main>
  <Footer />
</div>

<style>
  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
</style>
