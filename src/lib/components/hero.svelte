<script>
    let {
        titulo = "La JIC",
        descripcion = "Descripción por defecto",
        color = "bg-primary",
    } = $props();
</script>

<section class={color + " py-16 lg:py-20"}>
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <div class="max-w-2xl">
            <h1 class="font-serif text-4xl text-primary-foreground md:text-5xl">
                {titulo}
            </h1>
            <p class="mt-4 text-lg leading-relaxed text-primary-foreground/70">
                {descripcion}
            </p>
        </div>
    </div>
</section>
