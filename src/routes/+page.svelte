<script lang="ts">
	import Title from "$lib/components/inicio/title-section.svelte";
	import Dates from "$lib/components/inicio/dates-section.svelte";
	import Quick from "$lib/components/inicio/quick-section.svelte";
	import Winners from "$lib/components/inicio/winners-section.svelte";
	import FAQs from "$lib/components/inicio/faqs-section.svelte";
</script>

<svelte:head>
  <title>Inicio</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<Title />
<Dates />
<Quick />
<Winners />
<FAQs />