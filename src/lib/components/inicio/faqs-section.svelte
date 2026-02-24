<script lang="ts">
    import { slide } from 'svelte/transition';

    let openCategory = $state<string | null>("participacion");
    let openQuestion = $state<string | null>(null);

    const faqs = {
        participacion: {
            title: "Participación y Equipos",
            items: [
                { q: "¿Quiénes pueden participar en la JIC?", a: "Pueden participar estudiantes, docentes e investigadores de las universidades acreditadas por el CONEAUPA." },
                { q: "¿Si mi compañero es de otra facultad, puede participar en mi equipo?", a: "Sí, se permite grupos de estudiantes de diferentes facultades, pero el proyecto solo puede estar registrado en una de las facultades." },
                { q: "¿Se puede registrar una investigación individual?", a: "No. Los grupos deben ser de 2 o 3 estudiantes más el asesor." },
                { q: "¿Para participar en la final, el equipo debe registrarse en la plataforma del Congreso?", a: "Sí, todos los integrantes del grupo deben registrarse en el Congreso." },
                { q: "¿Puede mi asesor ser de otra facultad o sede?", a: "Sí, puede ser de otra facultad o sede, pero el proyecto se registra donde pertenecen los estudiantes." },
                { q: "¿Va a existir la figura de co-asesor?", a: "Sí, los equipos pueden contar con un asesor y un co-asesor." },
                { q: "¿Puedo participar si ya cuento con una licenciatura?", a: "No, el programa de la JIC es para estudiantes que no estén graduados." },
                { q: "¿Cuál es el siguiente paso para la final JIC?", a: "Luego de finalizada la JIC Interna, cada universidad debe registrar a sus participantes en la plataforma. En el caso de la UTP, solo deben actualizar los artículos." },
                { q: "¿Cuáles son los pasos para participar?", a: "Conformar un equipo de 2 o 3 estudiantes con un asesor y registrarse en la plataforma oficial." },
                { q: "¿Un estudiante podrá formar parte de más de un grupo?", a: "Sí, los estudiantes pueden participar en más de un grupo simultáneamente." },
                { q: "¿Es posible participar en la JIC siendo extranjero?", a: "Todo estudiante regular de una universidad participante que cumpla los requisitos puede participar." }
            ]
        },
        plataforma: {
            title: "Plataforma Tecnológica",
            items: [
                { q: "¿Dónde me registro para participar?", a: "Debes ingresar en el enlace oficial: jic.utp.ac.pa/login" },
                { q: "¿Cuál es el procedimiento para registrar los proyectos?", a: "El asesor registra el proyecto, los estudiantes suben documentos y el asesor aprueba finalmente." },
                { q: "¿Soy asesor y la plataforma no me permite editar datos?", a: "Solo los estudiantes cuentan con los permisos para editar los datos del proyecto." }
            ]
        },
        entregables: {
            title: "Entregables y Evaluación",
            items: [
                { q: "¿Qué documentos pide la JIC final?", a: "Todo grupo finalista debe entregar obligatoriamente su artículo, póster y video." },
                { q: "¿En cuánto tiempo se debe presentar el proyecto?", a: "Se tienen 15 minutos para exponer el trabajo y 5 minutos para preguntas y respuestas." },
                { q: "¿Se deben eliminar los nombres de los estudiantes y asesores?", a: "Sí, en la versión digital no deben estar. En el póster impreso sí se permiten." },
                { q: "¿Cómo compruebo la originalidad de mi proyecto?", a: "Debe pasarlo por un software anti-plagio; los organizadores harán una validación final." },
                { q: "¿Cuál es el tamaño y forma del póster?", a: "El tamaño requerido es A0 vertical, diseño libre." }
            ]
        }
    };

    const toggleCategory = (id: string) => {
        openCategory = openCategory === id ? null : id;
        openQuestion = null;
    };

    const toggleQuestion = (id: string) => {
        openQuestion = openQuestion === id ? null : id;
    };
</script>

<section class="bg-white dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-7xl sm:py-16 lg:px-6">
        <h2 class="font-serif mb-6 lg:mb-8 text-2xl md:text-3xl tracking-tight font-extrabold text-center text-gray-900 dark:text-white">
            Preguntas Frecuentes
        </h2>
        <p class="mb-6 lg:mb-8 text-sm sm:text-base md:text-lg tracking-tight font-normal text-center text-gray-500 dark:text-white">
            Todo lo que necesitas saber sobre la Jornada de Iniciación Científica
        </p>

        <div class="mx-auto max-w-3xl">
            <div id="accordion-flush">
                {#each Object.entries(faqs) as [key, section]}
                    {@const isCatOpen = openCategory === key}

                    <!-- Wrapper con border-b unificado para evitar el salto -->
                    <div class="border-b border-gray-200 dark:border-gray-700">

                        <h2 id="category-heading-{key}">
                            <button
                                type="button"
                                onclick={() => toggleCategory(key)}
                                class="flex justify-between items-center py-5 w-full font-bold text-left text-base md:text-lg cursor-pointer transition-colors duration-200 {isCatOpen ? 'text-gray-900 dark:text-white' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200'}"
                            >
                                <span>{section.title}</span>
                                <svg
                                    class="w-6 h-6 shrink-0 transition-transform duration-300 {isCatOpen ? 'rotate-180' : ''}"
                                    fill="currentColor"
                                    viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                                </svg>
                            </button>
                        </h2>

                        {#if isCatOpen}
                            <!-- overflow-hidden evita que el contenido "aparezca" antes de que termine la animación -->
                            <div transition:slide={{ duration: 300 }} class="overflow-hidden">
                                <div class="pl-4 border-l-2 border-gray-100 dark:border-gray-800 mb-2">
                                    {#each section.items as item, i}
                                        {@const qId = `${key}-${i}`}
                                        {@const isQOpen = openQuestion === qId}

                                        <div class="border-b border-gray-200 dark:border-gray-700 last:border-b-0">
                                            <h3>
                                                <button
                                                    type="button"
                                                    onclick={() => toggleQuestion(qId)}
                                                    class="flex justify-between items-center py-4 w-full font-medium text-left text-sm sm:text-base cursor-pointer transition-colors duration-200 {isQOpen ? 'text-primary-600 dark:text-primary-500' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200'}"
                                                >
                                                    <span class="pr-4">{item.q}</span>
                                                    <svg
                                                        class="w-5 h-5 shrink-0 transition-transform duration-200 {isQOpen ? 'rotate-180' : ''}"
                                                        fill="currentColor"
                                                        viewBox="0 0 20 20"
                                                    >
                                                        <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                                                    </svg>
                                                </button>
                                            </h3>

                                            {#if isQOpen}
                                                <div transition:slide={{ duration: 200 }} class="overflow-hidden">
                                                    <div class="pb-4">
                                                        <p class="text-gray-500 dark:text-gray-400 leading-relaxed text-sm sm:text-base">
                                                            {item.a}
                                                        </p>
                                                    </div>
                                                </div>
                                            {/if}
                                        </div>
                                    {/each}
                                </div>
                            </div>
                        {/if}

                    </div>
                {/each}
            </div>
        </div>
    </div>
</section>