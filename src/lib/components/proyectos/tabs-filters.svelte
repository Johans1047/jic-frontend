<script lang="ts">
    let { 
        tab = $bindable(), 
        yearFilter = $bindable(), 
        categoryFilter = $bindable(), 
        search = $bindable(),
        years = [],
        categoriesOptions = []
    } = $props();

    function handleYearChange(e: Event) {
        const val = (e.target as HTMLSelectElement).value;
        yearFilter = val === "all" ? "all" : Number(val);
    }
</script>

<section class="border-b border-border bg-card">
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <!-- Tabs -->
        <div class="flex gap-0 border-b border-border">
            <button
                onclick={() => (tab = "all")}
                class="cursor-pointer flex items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {tab ===
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
                class="cursor-pointer flex items-center gap-2 border-b-2 px-4 py-3 text-sm font-medium transition-colors {tab ===
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

        <div
            class="flex basis-96 flex-col gap-3 py-4 sm:flex-row sm:items-center"
        >
            <div class="relative w-full flex-1 sm:max-w-200">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground"
                    aria-hidden="true"
                >
                    <path d="m21 21-4.34-4.34"></path>
                    <circle cx="11" cy="11" r="8"></circle>
                </svg>

                <input
                    type="text"
                    placeholder="Buscar por título o universidad..."
                    bind:value={search}
                    class="w-full rounded-lg border border-input bg-stone-50 py-2 pl-10 pr-4 text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring"
                />
            </div>

            <!-- Filters -->
            <div class="flex items-center gap-2">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="h-7 w-7 text-muted-foreground"
                    aria-hidden="true"
                >
                    <path
                        d="M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z"
                    ></path>
                </svg>

                <div class="relative w-full max-w-37.5">
                    <select
                        value={yearFilter}
                        onchange={handleYearChange}
                        class="cursor-pointer w-full appearance-none rounded-lg border border-input bg-stone-50 px-3 py-2 pr-10 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-ring"
                    >
                        <option value="all">Todos los años</option>
                        {#each years as y}
                            <option value={y}>{y}</option>
                        {/each}
                    </select>
                </div>

                <div class="relative w-full max-w-70">
                    <select
                        bind:value={categoryFilter}
                        class="cursor-pointer w-full appearance-none rounded-lg border border-input bg-stone-50 px-3 py-2 pr-10 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-ring"
                    >
                        {#each categoriesOptions as c}
                            <option value={c.value}>{c.label}</option>
                        {/each}
                    </select>
                </div>
            </div>
        </div>
    </div>
</section>