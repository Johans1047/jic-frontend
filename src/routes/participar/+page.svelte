<script lang="ts">
    import Hero from "$lib/components/hero.svelte";
    import CTA from "$lib/components/participar/call-to-action.svelte";
    import Resources from "$lib/components/participar/resources.svelte";
    import Schedule from "$lib/components/participar/schedule.svelte";
</script>

<svelte:head>
    <title>Participar</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<Hero
    color="bg-cobalt-700/90"
    titulo="Participar"
    descripcion="Toda la información, documentos y recursos necesarios para participar en la JIC según tu rol."
/>
<CTA />
<Resources />
<Schedule />

