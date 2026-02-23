<script lang="ts">
	import Title from "$lib/components/home/title-section.svelte";
	import Dates from "$lib/components/home/dates-section.svelte";
	import Quick from "$lib/components/home/quick-section.svelte";
	import Winners from "$lib/components/home/winners-section.svelte";
</script>

<svelte:head>
  <title>Inicio</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<Title />
<Dates />
<Quick />
<Winners />