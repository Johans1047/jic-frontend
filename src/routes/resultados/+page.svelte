<script lang="ts">
    import ResultsHistory from "$lib/components/resultados/historical.svelte";
    import Results from "$lib/components/resultados/results.svelte";
    import Hero from "$lib/components/hero.svelte";

    const historicalResults = [
        {
            year: 2024,
            totalProjects: 120,
            universities: 8,
            documents: [
                { label: "Ganadores JIC 2024", href: "#", type: "PDF" },
                {
                    label: "Acta oficial de resultados 2024",
                    href: "#",
                    type: "PDF",
                },
                { label: "Programa final JIC 2024", href: "#", type: "PDF" },
            ],
        },
        {
            year: 2023,
            totalProjects: 105,
            universities: 7,
            documents: [
                { label: "Ganadores JIC 2023", href: "#", type: "PDF" },
                {
                    label: "Acta oficial de resultados 2023",
                    href: "#",
                    type: "PDF",
                },
            ],
        },
        {
            year: 2022,
            totalProjects: 95,
            universities: 6,
            documents: [
                { label: "Ganadores JIC 2022", href: "#", type: "PDF" },
                {
                    label: "Acta oficial de resultados 2022",
                    href: "#",
                    type: "PDF",
                },
            ],
        },
        {
            year: 2021,
            totalProjects: 80,
            universities: 5,
            documents: [
                { label: "Ganadores JIC 2021", href: "#", type: "PDF" },
            ],
        },
    ];
</script>

<svelte:head>
    <title>Resultados</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<Hero
    color="bg-amber-400"
    text_color="text-secondary-foreground"
    titulo="Resultados"
    descripcion="Resultados oficiales, actas y documentos de cada edición de la JIC."
/>

<Results />
<ResultsHistory {historicalResults} />
