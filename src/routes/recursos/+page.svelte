<script lang="ts">
    import Hero from "$lib/components/hero.svelte";
    import Tabs from "$lib/components/recursos/tabs.svelte";
    import Pagination from "$lib/components/pagination.svelte";
</script>

<svelte:head>
    <title>Recursos</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<Hero
    color="bg-muted-foreground/70"
    titulo="Recursos"
    descripcion="Documentos, boletines, memorias, galeria de fotos y videos de la JIC."
/>
<Tabs />
<Pagination color="bg-stone-50" />