<script lang="ts">
    import Hero from "$lib/components/hero.svelte";
    import TabsFilters from "$lib/components/proyectos/tabs-filters.svelte";

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

    const years = [2024, 2023, 2022];
    const categoriesOptions = [
        "Todas",
        "Ingenieria",
        "Ciencias de la Salud",
        "Ciencias Naturales y Exactas",
        "Ciencias Sociales y Humanisticas",
    ];

    const universities = [
        { name: "UTP", href: "https://utp.ac.pa" },
        { name: "UP", href: "https://up.ac.pa" },
        { name: "USMA", href: "https://usma.ac.pa" },
        { name: "UNACHI", href: "https://unachi.ac.pa" },
        { name: "ULAT", href: "https://ulat.ac.pa" },
    ];

    // Svelte 5 runes
    let tab = $state<"all" | "winners">("all");
    let yearFilter = $state<number | "all">("all");
    let categoryFilter = $state("Todas");
    let search = $state("");

    const filtered = $derived(
        allProjects.filter((p) => {
            if (tab === "winners" && !p.winner) return false;
            if (yearFilter !== "all" && p.year !== yearFilter) return false;
            if (categoryFilter !== "Todas" && p.category !== categoryFilter)
                return false;
            if (
                search &&
                !p.title.toLowerCase().includes(search.toLowerCase()) &&
                !p.university.toLowerCase().includes(search.toLowerCase())
            )
                return false;
            return true;
        }),
    );

    function handleYearChange(e: Event) {
        const val = (e.target as HTMLSelectElement).value;
        yearFilter = val === "all" ? "all" : Number(val);
    }
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
<TabsFilters />

<!-- Tabs & Filters -->
<section class="border-b border-border bg-card">
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <!-- Tabs -->
        <div class="flex gap-0 border-b border-border">
            <button
                onclick={() => (tab = "all")}
                class="flex items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {tab ===
                'all'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground'}"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    aria-hidden="true"
                    ><path d="M12 7v14"></path><path
                        d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"
                    ></path></svg
                >
                Todos los proyectos
            </button>
            <button
                onclick={() => (tab = "winners")}
                class="flex items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {tab ===
                'winners'
                    ? 'border-golden text-golden-foreground'
                    : 'border-transparent text-muted-foreground hover:text-foreground'}"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    aria-hidden="true"
                    ><path
                        d="M10 14.66v1.626a2 2 0 0 1-.976 1.696A5 5 0 0 0 7 21.978"
                    ></path><path
                        d="M14 14.66v1.626a2 2 0 0 0 .976 1.696A5 5 0 0 1 17 21.978"
                    ></path><path d="M18 9h1.5a1 1 0 0 0 0-5H18"></path><path
                        d="M4 22h16"
                    ></path><path
                        d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"
                    ></path><path d="M6 9H4.5a1 1 0 0 1 0-5H6"></path></svg
                >
                Ganadores
            </button>
        </div>

        <!-- Filters -->
        <div class="flex flex-col gap-3 py-4 sm:flex-row sm:items-center">
            <div class="relative flex-1">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground"
                    aria-hidden="true"
                    ><path d="m21 21-4.34-4.34"></path><circle
                        cx="11"
                        cy="11"
                        r="8"
                    ></circle></svg
                >
                <input
                    type="text"
                    placeholder="Buscar por titulo o universidad..."
                    bind:value={search}
                    class="w-full rounded-lg border border-input bg-background py-2 pl-10 pr-4 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring"
                />
            </div>
            <div class="flex items-center gap-2">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4 text-muted-foreground"
                    aria-hidden="true"
                    ><path
                        d="M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z"
                    ></path></svg
                >
                <select
                    value={yearFilter}
                    onchange={handleYearChange}
                    class="rounded-lg border border-input bg-background px-3 py-2 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-ring"
                >
                    <option value="all">Todos los anos</option>
                    {#each years as y}
                        <option value={y}>{y}</option>
                    {/each}
                </select>
                <select
                    bind:value={categoryFilter}
                    class="rounded-lg border border-input bg-background px-3 py-2 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-ring"
                >
                    {#each categoriesOptions as c}
                        <option value={c}>{c}</option>
                    {/each}
                </select>
            </div>
        </div>
    </div>
</section>

<!-- Results Table -->
<section class="py-8 lg:py-12">
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <p class="mb-4 text-sm text-muted-foreground">
            {filtered.length} proyectos encontrados
        </p>
        <div class="overflow-x-auto rounded-xl border border-border">
            <table class="w-full text-sm">
                <thead>
                    <tr class="bg-secondary">
                        <th
                            class="px-4 py-3 text-left font-semibold text-foreground"
                            >Ano</th
                        >
                        <th
                            class="px-4 py-3 text-left font-semibold text-foreground"
                            >Titulo</th
                        >
                        <th
                            class="hidden px-4 py-3 text-left font-semibold text-foreground md:table-cell"
                            >Universidad</th
                        >
                        <th
                            class="hidden px-4 py-3 text-left font-semibold text-foreground lg:table-cell"
                            >Categoria</th
                        >
                        <th
                            class="hidden px-4 py-3 text-left font-semibold text-foreground sm:table-cell"
                            >Contacto</th
                        >
                    </tr>
                </thead>
                <tbody>
                    {#each filtered as p, i (i)}
                        <tr
                            class="border-t border-border transition-colors hover:bg-secondary/50"
                        >
                            <td class="px-4 py-3 text-foreground">
                                <div class="flex items-center gap-2">
                                    {#if p.winner}
                                        <svg
                                            xmlns="http://www.w3.org/2000/svg"
                                            width="14"
                                            height="14"
                                            viewBox="0 0 24 24"
                                            fill="none"
                                            stroke="currentColor"
                                            stroke-width="2"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            class="h-3.5 w-3.5 text-golden"
                                            aria-hidden="true"
                                            ><path
                                                d="M10 14.66v1.626a2 2 0 0 1-.976 1.696A5 5 0 0 0 7 21.978"
                                            ></path><path
                                                d="M14 14.66v1.626a2 2 0 0 0 .976 1.696A5 5 0 0 1 17 21.978"
                                            ></path><path
                                                d="M18 9h1.5a1 1 0 0 0 0-5H18"
                                            ></path><path d="M4 22h16"
                                            ></path><path
                                                d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"
                                            ></path><path
                                                d="M6 9H4.5a1 1 0 0 1 0-5H6"
                                            ></path></svg
                                        >
                                    {/if}
                                    {p.year}
                                </div>
                            </td>
                            <td
                                class="max-w-xs px-4 py-3 font-medium text-foreground"
                                >{p.title}</td
                            >
                            <td
                                class="hidden px-4 py-3 text-muted-foreground md:table-cell"
                                >{p.university}</td
                            >
                            <td class="hidden px-4 py-3 lg:table-cell">
                                <span
                                    class="rounded-full bg-primary/10 px-2.5 py-0.5 text-xs font-medium text-primary"
                                >
                                    {p.category}
                                </span>
                            </td>
                            <td class="hidden px-4 py-3 sm:table-cell">
                                <a
                                    href="mailto:{p.contact}"
                                    class="text-primary underline-offset-2 hover:underline"
                                >
                                    {p.contact}
                                </a>
                            </td>
                        </tr>
                    {:else}
                        <tr>
                            <td
                                colspan="5"
                                class="px-4 py-12 text-center text-muted-foreground"
                            >
                                No se encontraron proyectos con los filtros
                                seleccionados.
                            </td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    </div>
</section>

<!-- Institutional links -->
<section class="bg-card py-12">
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <h2 class="mb-6 font-serif text-xl text-foreground">
            Selecciones institucionales
        </h2>
        <p class="mb-4 text-sm text-muted-foreground">
            Consulta la informacion de las selecciones institucionales de las
            universidades participantes:
        </p>
        <div class="flex flex-wrap gap-3">
            {#each universities as uni}
                <a
                    href={uni.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="rounded-lg border border-border bg-background px-4 py-2 text-sm font-medium text-foreground transition-colors hover:border-primary/30 hover:bg-primary/5"
                >
                    {uni.name}
                </a>
            {/each}
        </div>
    </div>
</section>

