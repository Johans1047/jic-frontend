<script lang="ts">
    let activeTab = $state<
        "docs" | "boletines" | "memorias" | "galeria" | "videos"
    >("docs");

    const documentsByEdition = [
        {
            year: 2025,
            docs: [
                { label: "Lineamientos JIC 2025", href: "#" },
                { label: "Informe de participacion institucional", href: "#" },
                { label: "Folleto JIC 2025", href: "#" },
            ],
        },
        {
            year: 2024,
            docs: [
                { label: "Lineamientos JIC 2024", href: "#" },
                { label: "Programa final JIC 2024", href: "#" },
                { label: "Preguntas frecuentes 2024", href: "#" },
                { label: "Folleto JIC 2024", href: "#" },
            ],
        },
        {
            year: 2023,
            docs: [
                { label: "Lineamientos JIC 2023", href: "#" },
                { label: "Programa final JIC 2023", href: "#" },
            ],
        },
    ];

    const boletines = [
        {
            title: "Boletin JIC 2024 - Momentos destacados",
            description:
                "Ganadores, pasantias otorgadas y mejores momentos de la JIC Nacional 2024.",
            href: "#",
        },
        {
            title: "Boletin JIC 2023 - Resumen anual",
            description:
                "Resumen de la edición 2023 con proyectos ganadores y estadisticas.",
            href: "#",
        },
        {
            title: "Boletin JIC 2022 - Innovacion juvenil",
            description: "Destacados y logros de la edición 2022.",
            href: "#",
        },
    ];

    const memorias = [
        {
            title: "Memorias JIC 2024",
            description:
                "Publicaciones completas y documentacion de la edición 2024.",
            href: "#",
        },
        {
            title: "Memorias JIC 2023",
            description:
                "Compendio de articulos e investigaciones presentadas en 2023.",
            href: "#",
        },
        {
            title: "Memorias JIC 2022",
            description: "Documentacion integral de la edición 2022.",
            href: "#",
        },
    ];

    const videos = [
        {
            title: "Video promocional JIC Nacional",
            thumbnail: "/images/hero-jic.jpg",
            url: "https://www.youtube.com/watch?v=example1",
        },
        {
            title: "¿Cómo preparar tu proyecto de investigación?",
            thumbnail: "/images/categories-science.jpg",
            url: "https://www.youtube.com/watch?v=example2",
        },
        {
            title: "Inducción a la JIC 2024",
            thumbnail: "/images/hero-jic.jpg",
            url: "https://www.youtube.com/watch?v=example3",
        },
    ];

    const tabs = [
        { id: "docs", label: "Documentos" },
        { id: "boletines", label: "Boletines" },
        { id: "memorias", label: "Memorias" },
        { id: "galeria", label: "Galeria" },
        { id: "videos", label: "JIC Virtual" },
    ] as const;
</script>

<!-- Tabs -->
<section class="border-b border-border bg-card">
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <div class="-mb-px flex gap-0 overflow-x-auto">
            <!-- Documentos -->
            <button
                onclick={() => (activeTab = "docs")}
                class="cursor-pointer flex shrink-0 items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {activeTab ===
                'docs'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground'}"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    aria-hidden="true"
                    ><path
                        d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"
                    ></path><path d="M14 2v5a1 1 0 0 0 1 1h5"></path><path
                        d="M10 9H8"
                    ></path><path d="M16 13H8"></path><path d="M16 17H8"
                    ></path></svg
                >
                Documentos
            </button>

            <!-- Boletines -->
            <button
                onclick={() => (activeTab = "boletines")}
                class="cursor-pointer flex shrink-0 items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {activeTab ===
                'boletines'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground'}"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    aria-hidden="true"
                    ><path d="M15 18h-5"></path><path d="M18 14h-8"></path><path
                        d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-4 0v-9a2 2 0 0 1 2-2h2"
                    ></path><rect width="8" height="4" x="10" y="6" rx="1"
                    ></rect></svg
                >
                Boletines
            </button>

            <!-- Memorias -->
            <button
                onclick={() => (activeTab = "memorias")}
                class="cursor-pointer flex shrink-0 items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {activeTab ===
                'memorias'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground'}"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    aria-hidden="true"
                    ><path d="M12 7v14"></path><path
                        d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"
                    ></path></svg
                >
                Memorias
            </button>

            <!-- Galeria -->
            <button
                onclick={() => (activeTab = "galeria")}
                class="cursor-pointer flex shrink-0 items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {activeTab ===
                'galeria'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground'}"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    aria-hidden="true"
                    ><rect width="18" height="18" x="3" y="3" rx="2" ry="2"
                    ></rect><circle cx="9" cy="9" r="2"></circle><path
                        d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"
                    ></path></svg
                >
                Galería
            </button>

            <!-- JIC Multimedia -->
            <button
                onclick={() => (activeTab = "videos")}
                class="cursor-pointer flex shrink-0 items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {activeTab ===
                'videos'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground'}"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-4 w-4"
                    aria-hidden="true"
                    ><path
                        d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"
                    ></path><rect x="2" y="6" width="14" height="12" rx="2"
                    ></rect></svg
                >
                Multimedia
            </button>
        </div>
    </div>
</section>

<!-- Tab Content -->
<section class="py-12 lg:py-20 bg-stone-50">
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <!-- Documents by Edition -->
        {#if activeTab === "docs"}
            <div class="flex flex-col gap-8">
                <h2 class="font-serif text-2xl md:text-3xl text-foreground">
                    Documentos por edición
                </h2>
                {#each documentsByEdition as edition}
                    <div>
                        <h3 class="mb-3 text-lg font-bold text-foreground">
                            JIC {edition.year}
                        </h3>
                        <div class="flex flex-col gap-2">
                            {#each edition.docs as doc}
                                <a
                                    href={doc.href}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    class="flex items-center gap-3 rounded-lg border border-border bg-card px-4 py-3 text-sm transition-colors hover:border-stone-400 hover:bg-stone-100"
                                >
                                    <!-- Download icon -->
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        width="24"
                                        height="24"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        stroke-width="2"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        class="h-4 w-4 shrink-0 text-muted-foreground"
                                        aria-hidden="true"
                                        ><path
                                            d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
                                        ></path><polyline
                                            points="7 10 12 15 17 10"
                                        ></polyline><line
                                            x1="12"
                                            y1="15"
                                            x2="12"
                                            y2="3"
                                        ></line></svg
                                    >
                                    <span class="text-foreground"
                                        >{doc.label}</span
                                    >
                                    <!-- ExternalLink icon -->
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        width="24"
                                        height="24"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        stroke-width="2"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        class="ml-auto h-3 w-3 shrink-0 text-muted-foreground"
                                        aria-hidden="true"
                                        ><path
                                            d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"
                                        ></path><polyline
                                            points="15 3 21 3 21 9"
                                        ></polyline><line
                                            x1="10"
                                            y1="14"
                                            x2="21"
                                            y2="3"
                                        ></line></svg
                                    >
                                </a>
                            {/each}
                        </div>
                    </div>
                {/each}
            </div>
        {/if}

        <!-- Boletines -->
        {#if activeTab === "boletines"}
            <div class="flex flex-col gap-6">
                <div>
                    <h2 class="font-serif text-2xl text-foreground">
                        Boletines
                    </h2>
                    <p class="mt-1 text-muted-foreground">
                        Momentos importantes, ganadores y pasantias de cada
                        edición.
                    </p>
                </div>
                <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                    {#each boletines as b}
                        <a
                            href={b.href}
                            target="_blank"
                            rel="noopener noreferrer"
                            class="group rounded-xl border border-border bg-card p-5 transition-all hover:border-primary/30 hover:shadow-md"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="24"
                                height="24"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                stroke-width="2"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                class="mb-3 h-8 w-8 text-primary"
                                aria-hidden="true"
                                ><path d="M15 18h-5"></path><path d="M18 14h-8"
                                ></path><path
                                    d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-4 0v-9a2 2 0 0 1 2-2h2"
                                ></path><rect
                                    width="8"
                                    height="4"
                                    x="10"
                                    y="6"
                                    rx="1"
                                ></rect></svg
                            >
                            <h3
                                class="font-semibold text-foreground group-hover:text-primary"
                            >
                                {b.title}
                            </h3>
                            <p
                                class="mt-2 text-sm leading-relaxed text-muted-foreground"
                            >
                                {b.description}
                            </p>
                        </a>
                    {/each}
                </div>
            </div>
        {/if}

        <!-- Memories -->
        {#if activeTab === "memorias"}
            <div class="flex flex-col gap-6">
                <div>
                    <h2 class="font-serif text-2xl text-foreground">
                        Memorias
                    </h2>
                    <p class="mt-1 text-muted-foreground">
                        Toda la informacion relacionada a las publicaciones
                        realizadas cada ano.
                    </p>
                </div>
                <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                    {#each memorias as m}
                        <a
                            href={m.href}
                            target="_blank"
                            rel="noopener noreferrer"
                            class="group rounded-xl border border-border bg-card p-5 transition-all hover:border-teal/30 hover:shadow-md"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="24"
                                height="24"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                stroke-width="2"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                class="mb-3 h-8 w-8 text-teal"
                                aria-hidden="true"
                                ><path d="M12 7v14"></path><path
                                    d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"
                                ></path></svg
                            >
                            <h3
                                class="font-semibold text-foreground group-hover:text-teal"
                            >
                                {m.title}
                            </h3>
                            <p
                                class="mt-2 text-sm leading-relaxed text-muted-foreground"
                            >
                                {m.description}
                            </p>
                        </a>
                    {/each}
                </div>
            </div>
        {/if}

        <!-- Gallery -->
        {#if activeTab === "galeria"}
            <div class="flex flex-col gap-6">
                <h2 class="font-serif text-2xl text-foreground">
                    Galería de fotos
                </h2>
                <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                    {#each [1, 2, 3, 4, 5, 6] as i}
                        <div
                            class="group relative aspect-[4/3] overflow-hidden rounded-xl border border-border bg-secondary"
                        >
                            <img
                                src={i % 2 === 0
                                    ? "/images/categories-science.jpg"
                                    : "/images/hero-jic.jpg"}
                                alt="Galeria JIC - Imagen {i}"
                                class="h-full w-full object-cover transition-transform group-hover:scale-105"
                            />
                            <div
                                class="absolute inset-0 bg-foreground/0 transition-colors group-hover:bg-foreground/20"
                            ></div>
                        </div>
                    {/each}
                </div>
            </div>
        {/if}

        <!-- Videos -->
        {#if activeTab === "videos"}
            <div class="flex flex-col gap-6">
                <div>
                    <h2 class="font-serif text-2xl text-foreground">
                        JIC Virtual
                    </h2>
                    <p class="mt-1 text-muted-foreground">
                        Videos, recursos y material audiovisual util para
                        estudiantes.
                    </p>
                </div>
                <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                    {#each videos as v}
                        <a
                            href={v.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            class="group overflow-hidden rounded-xl border border-border bg-card transition-all hover:border-primary/30 hover:shadow-md"
                        >
                            <div class="relative aspect-video bg-secondary">
                                <img
                                    src={v.thumbnail}
                                    alt={v.title}
                                    class="h-full w-full object-cover"
                                />
                                <div
                                    class="absolute inset-0 flex items-center justify-center bg-foreground/30 opacity-0 transition-opacity group-hover:opacity-100"
                                >
                                    <div
                                        class="flex h-12 w-12 items-center justify-center rounded-full bg-primary-foreground/90"
                                    >
                                        <!-- Play icon -->
                                        <svg
                                            xmlns="http://www.w3.org/2000/svg"
                                            width="24"
                                            height="24"
                                            viewBox="0 0 24 24"
                                            fill="none"
                                            stroke="currentColor"
                                            stroke-width="2"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            class="h-5 w-5 text-primary"
                                            aria-hidden="true"
                                            ><polygon
                                                points="5 3 19 12 5 21 5 3"
                                            ></polygon></svg
                                        >
                                    </div>
                                </div>
                            </div>
                            <div class="p-4">
                                <h3
                                    class="font-semibold text-foreground group-hover:text-primary"
                                >
                                    {v.title}
                                </h3>
                            </div>
                        </a>
                    {/each}
                </div>
            </div>
        {/if}
    </div>
</section>
