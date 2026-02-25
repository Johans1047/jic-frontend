<script lang="ts">
    import Hero from "$lib/components/hero.svelte";
    import TabsFilters from "$lib/components/proyectos/tabs-filters.svelte";
    import Results from "$lib/components/proyectos/results.svelte";

    const years = [2024, 2023, 2022];
    const categoriesOptions = [
        { label: "Todas las categorías", value: "Todas" },
        { label: "Ingeniería", value: "Ingenieria" },
        { label: "Ciencias de la Salud", value: "Ciencias de la Salud" },
        { label: "Ciencias Naturales y Exactas", value: "Ciencias Naturales y Exactas" },
        { label: "Ciencias Sociales y Humanísticas", value: "Ciencias Sociales y Humanisticas" },
    ];

    type Project = {
        title: string;
        university: string;
        category: string;
        year: number;
        contact: string;
        winner: boolean;
    };

    const allProjects: Project[] = [
        {
            title: "Sistema de monitoreo ambiental con IoT",
            university: "UTP",
            category: "Ingenieria",
            year: 2024,
            contact: "jperez@utp.ac.pa",
            winner: true,
        },
        {
            title: "Analisis de biomarcadores en diabetes tipo 2",
            university: "UP",
            category: "Ciencias de la Salud",
            year: 2024,
            contact: "mgarcia@up.ac.pa",
            winner: true,
        },
        {
            title: "Modelado matematico de ecosistemas costeros",
            university: "UTP",
            category: "Ciencias Naturales y Exactas",
            year: 2024,
            contact: "alopez@utp.ac.pa",
            winner: true,
        },
        {
            title: "Impacto de redes sociales en la educacion superior",
            university: "USMA",
            category: "Ciencias Sociales y Humanisticas",
            year: 2024,
            contact: "lrodriguez@usma.ac.pa",
            winner: true,
        },
        {
            title: "Desarrollo de materiales biodegradables a partir de almidon",
            university: "UTP",
            category: "Ingenieria",
            year: 2024,
            contact: "csmith@utp.ac.pa",
            winner: false,
        },
        {
            title: "Aplicacion movil para la deteccion temprana de plagas",
            university: "UNACHI",
            category: "Ciencias Naturales y Exactas",
            year: 2023,
            contact: "rmartinez@unachi.ac.pa",
            winner: true,
        },
        {
            title: "Evaluacion de la calidad del agua en rios urbanos",
            university: "UTP",
            category: "Ciencias Naturales y Exactas",
            year: 2023,
            contact: "ddiaz@utp.ac.pa",
            winner: true,
        },
        {
            title: "Inteligencia artificial aplicada a diagnostico medico",
            university: "UP",
            category: "Ciencias de la Salud",
            year: 2023,
            contact: "fhernandez@up.ac.pa",
            winner: false,
        },
        {
            title: "Diseno de protesis de bajo costo con impresion 3D",
            university: "UTP",
            category: "Ingenieria",
            year: 2023,
            contact: "jcastro@utp.ac.pa",
            winner: true,
        },
        {
            title: "Percepcion ciudadana de la seguridad publica",
            university: "ULAT",
            category: "Ciencias Sociales y Humanisticas",
            year: 2022,
            contact: "mflores@ulat.ac.pa",
            winner: true,
        },
        {
            title: "Robot autonomo para agricultura de precision",
            university: "UTP",
            category: "Ingenieria",
            year: 2022,
            contact: "ktorres@utp.ac.pa",
            winner: true,
        },
        {
            title: "Estudio de la biodiversidad en manglares panamenos",
            university: "UP",
            category: "Ciencias Naturales y Exactas",
            year: 2022,
            contact: "pvargas@up.ac.pa",
            winner: false,
        },
    ];

    let tab = $state<"all" | "winners">("all");
    let yearFilter = $state<number | "all">("all");
    let categoryFilter = $state("Todas");
    let search = $state("");

    const filtered = $derived(
        allProjects.filter((p) => {
            if (tab === "winners" && !p.winner) return false;
            if (yearFilter !== "all" && p.year !== yearFilter) return false;
            if (categoryFilter !== "Todas" && p.category !== categoryFilter) return false;
            if (search && 
                !p.title.toLowerCase().includes(search.toLowerCase()) && 
                !p.university.toLowerCase().includes(search.toLowerCase())) return false;
            return true;
        })
    );
</script>

<svelte:head>
    <title>Proyectos</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<Hero
    color="bg-cobalt-700/90"
    titulo="Proyectos"
    descripcion="Repositorio histórico de proyectos de investigación presentados en la JIC."
/>

<TabsFilters 
    bind:tab={tab}
    bind:yearFilter={yearFilter}
    bind:categoryFilter={categoryFilter}
    bind:search={search}
    {years}
    {categoriesOptions}
/>

<Results {filtered} />