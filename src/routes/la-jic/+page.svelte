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
<section class="bg-card py-16 lg:py-24 border-t border-border">
    <div class="mx-auto max-w-7xl px-4 lg:px-8 flex flex-col gap-16">
        <!-- Reconocimientos -->
        <div>
            <div class="mb-8 text-center">
                <h2 class="font-serif text-2xl text-foreground md:text-3xl">
                    Reconocimientos
                </h2>
                <p class="mt-2 text-muted-foreground">
                    Premios y distinciones recibidos a lo largo de los años
                </p>
            </div>
            <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {#each [{ premio: "Premio Nacional de Innovación Juvenil", año: "2024", entidad: "SENACYT", descripcion: "Reconocimiento a la mejor iniciativa de divulgación científica estudiantil." }, { premio: "Mención de Honor APANAC", año: "2023", entidad: "APANAC", descripcion: "Distinción por fomentar la investigación en universidades públicas." }, { premio: "Premio a la Excelencia Académica", año: "2022", entidad: "Ministerio de Educación", descripcion: "Otorgado por el impacto en la formación científica de jóvenes panameños." }] as r}
                    <div
                        class="rounded-xl border border-border bg-stone-50 p-5 flex flex-col gap-3"
                    >
                        <div class="flex items-start gap-3">
                            <div
                                class="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-amber-300/20"
                            >
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="20"
                                    height="20"
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    stroke-width="2"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="text-amber-500"
                                >
                                    <path
                                        d="M7.21 15 2.66 7.14a2 2 0 0 1 .13-2.2L4.4 2.8A2 2 0 0 1 6 2h12a2 2 0 0 1 1.6.8l1.6 2.14a2 2 0 0 1 .14 2.2L16.79 15"
                                    />
                                    <path d="M11 12 5.12 2.2" /><path
                                        d="m13 12 5.88-9.8"
                                    />
                                    <path d="M8 7h8" /><circle
                                        cx="12"
                                        cy="17"
                                        r="5"
                                    />
                                    <path d="M12 18v-2h-.5" />
                                </svg>
                            </div>
                            <div>
                                <span
                                    class="inline-block rounded-full bg-amber-300/20 px-2.5 py-0.5 text-xs font-semibold text-amber-700 mb-1"
                                    >{r.año}</span
                                >
                                <h3
                                    class="font-semibold text-foreground leading-snug"
                                >
                                    {r.premio}
                                </h3>
                                <p class="text-xs text-muted-foreground mt-0.5">
                                    {r.entidad}
                                </p>
                            </div>
                        </div>
                        <p
                            class="text-sm text-muted-foreground leading-relaxed"
                        >
                            {r.descripcion}
                        </p>
                    </div>
                {/each}
            </div>
        </div>

        <!-- Organiza -->
        <div>
            <div class="mb-8 text-center">
                <h2 class="font-serif text-2xl text-foreground md:text-3xl">
                    Organiza
                </h2>
                <p class="mt-2 text-muted-foreground">
                    Instituciones responsables de la organización de la JIC
                </p>
            </div>
            <div class="flex flex-wrap items-center justify-center gap-8">
                {#each [{ nombre: "Universidad Tecnológica de Panamá", siglas: "UTP" }] as org}
                    <div class="flex flex-col items-center gap-3 group">
                        <!-- Placeholder logo -->
                        <div
                            class="flex h-24 w-48 items-center justify-center rounded-xl border-2 border-dashed border-border bg-stone-50 transition-colors group-hover:border-primary/30 group-hover:bg-primary/5"
                        >
                            <div class="text-center px-4">
                                <p
                                    class="text-lg font-bold text-muted-foreground/50"
                                >
                                    {org.siglas}
                                </p>
                                <p
                                    class="text-2xs text-muted-foreground/40 mt-0.5"
                                >
                                    Logo
                                </p>
                            </div>
                        </div>
                        <p
                            class="text-sm font-medium text-muted-foreground text-center max-w-[180px] leading-snug"
                        >
                            {org.nombre}
                        </p>
                    </div>
                {/each}
            </div>
        </div>

        <!-- Auspiciado por -->
        <div>
            <div class="mb-8 text-center">
                <h2 class="font-serif text-2xl text-foreground md:text-3xl">
                    Auspiciado por
                </h2>
                <p class="mt-2 text-muted-foreground">
                    Instituciones y empresas que apoyan la JIC Nacional
                </p>
            </div>
            <div class="flex flex-wrap items-center justify-center gap-8">
                {#each [{ nombre: "Secretaría Nacional de Ciencia, Tecnología e Innovación", siglas: "SENACYT" }] as org}
                    <div class="flex flex-col items-center gap-3 group">
                        <!-- Placeholder logo -->
                        <div
                            class="flex h-24 w-48 items-center justify-center rounded-xl border-2 border-dashed border-border bg-stone-50 transition-colors group-hover:border-primary/30 group-hover:bg-primary/5"
                        >
                            <div class="text-center px-4">
                                <p
                                    class="text-lg font-bold text-muted-foreground/50"
                                >
                                    {org.siglas}
                                </p>
                                <p
                                    class="text-2xs text-muted-foreground/40 mt-0.5"
                                >
                                    Logo
                                </p>
                            </div>
                        </div>
                        <p
                            class="text-sm font-medium text-muted-foreground text-center max-w-[180px] leading-snug"
                        >
                            {org.nombre}
                        </p>
                    </div>
                {/each}
            </div>
        </div>
    </div>
</section>
