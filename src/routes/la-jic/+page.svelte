<script lang="ts">
    import Hero from "$lib/components/hero.svelte";
    import Concept from "$lib/components/jic/concept.svelte";
    import Background from "$lib/components/jic/background.svelte";
    import Categories from "$lib/components/jic/categories.svelte";
</script>

<svelte:head>
    <title>La JIC</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<Hero
    color="bg-cobalt-700/90"
    titulo="La JIC"
    descripcion="Conoce todo sobre la Jornada de Iniciación Cienífica, su
                historia y estructura."
/>
<Concept />
<Background />
<Categories />
