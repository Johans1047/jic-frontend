<script lang="ts">
    const schedule = [
        ['Apertura de inscripciones', 'Mayo 2025'],
        ['Cierre de inscripciones', 'Julio 2025'],
        ['Seleccion institucional', 'Agosto 2025'],
        ['Seleccion nacional', 'Septiembre - Octubre 2025'],
        ['JIC Nacional 2025', 'Octubre 2025'],
    ];
</script>

<section class="bg-card py-16 lg:py-24">
    <div class="mx-auto max-w-4xl px-4 lg:px-8">
        <h2
            class="mb-8 text-center font-serif text-2xl text-foreground md:text-3xl"
        >
            Cronograma resumido
        </h2>
        <div class="overflow-hidden rounded-xl border border-border">
            <table class="w-full text-sm">
                <thead>
                    <tr class="bg-secondary/45">
                        <th
                            class="px-6 py-3 text-left font-semibold text-foreground"
                            >Actividad</th
                        >
                        <th
                            class="px-6 py-3 text-left font-semibold text-foreground"
                            >Periodo</th
                        >
                    </tr>
                </thead>
                <tbody>
                    {#each schedule as [activity, period]}
                        <tr class="border-t border-border">
                            <td class="px-6 py-3 text-foreground">{activity}</td
                            >
                            <td class="px-6 py-3 text-muted-foreground"
                                >{period}</td
                            >
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    </div>
</section>
