<script lang="ts">
    import Hero from "$lib/components/hero.svelte";
    import Tabs from "$lib/components/recursos/tabs.svelte";
</script>

<svelte:head>
    <title>Resultados</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<Hero
    color="bg-muted-foreground/70"
    titulo="Recursos"
    descripcion="Documentos, boletines, memorias, galeria de fotos y videos de la JIC."
/>
<Tabs />