<script lang="ts">
    import ResourceCard from "$lib/components/participar/ui/resource-card.svelte";

    const studentResources = [
        {
            label: "Lineamientos de participacion 2025",
            href: "https://iniciacioncientifica.utp.ac.pa/subida-de-documentos-para-docentes/",
            icon: "file",
        },
        {
            label: "Plantilla para articulos",
            href: "https://iniciacioncientifica.utp.ac.pa/instructivos-y-ejemplos-para-estudiantes/",
            icon: "download",
        },
        { label: "Manual de usuario: Estudiante", href: "#", icon: "book" },
        {
            label: "Recursos digitales",
            href: "https://iniciacioncientifica.utp.ac.pa/subida-de-documentos-para-docentes/",
            icon: "external-link",
        },
    ];

    const advisorResources = [
        { label: "Lineamientos para asesores", href: "#", icon: "file" },
        {
            label: "Rubricas de evaluacion",
            href: "https://iniciacioncientifica.utp.ac.pa/wp-content/uploads/2024/05/manual-proce-JIC.pdf",
            icon: "clipboard",
        },
        { label: "Manual de usuario: Asesor", href: "#", icon: "book" },
    ];

    const evaluatorResources = [
        {
            label: "Rubricas de evaluacion",
            href: "https://iniciacioncientifica.utp.ac.pa/wp-content/uploads/2024/05/manual-proce-JIC.pdf",
            icon: "clipboard",
        },
        { label: "Procedimiento de evaluacion", href: "#", icon: "file" },
        { label: "Documentos de induccion", href: "#", icon: "book" },
    ];
</script>

<section class="py-16 lg:py-24 bg-stone-50">
    <div class="mx-auto max-w-7xl px-4 lg:px-8">
        <div class="grid gap-6 lg:grid-cols-3">
            <ResourceCard
                title="Estudiantes"
                description="Informacion para participantes"
                accent="bg-primary/90 text-primary-foreground"
                resources={studentResources}
            />

            <ResourceCard
                title="Asesores"
                description="Informacion para asesores"
                accent="bg-secondary-foreground/65 text-primary-foreground"
                resources={advisorResources}
            />

            <ResourceCard
                title="Evaluadores"
                description="Informacion para evaluadores"
                accent="bg-amber-400 text-secondary-foreground"
                resources={evaluatorResources}
            />
        </div>
    </div>
</section>
