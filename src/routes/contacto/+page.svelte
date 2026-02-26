<script lang="ts">
    import Hero from "$lib/components/hero.svelte";
    import Contact from "$lib/components/contacto/contact.svelte";
</script>

<svelte:head>
    <title>Contacto</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<Hero
    color="bg-cobalt-700/90"
    titulo="Contacto"
    descripcion="Comunícate con el equipo de la JIC para cualquier consulta o información."
/>
<Contact />

