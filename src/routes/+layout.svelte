<script lang="ts">
  import "./layout.css";
  import Header from "../components/header.svelte";
  import Footer from "../components/footer.svelte";

  let { children } = $props();
</script>

<div class="app">
  <Header />
  <main>
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
