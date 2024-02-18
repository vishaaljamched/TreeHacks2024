"""The Lección 1 page."""
from TreeHacks2024.templates import template
from TreeHacks2024.chat_state import ChatState, QA
from TreeHacks2024.components.chat import chat, action_bar, transcribe_bar
from TreeHacks2024.templates.template import footer
import requests

import reflex as rx


@template(route="/leccion1/intro", title="Lección 1", image="/guitar.svg")
def leccion1() -> rx.Component:
    """Lesson 1 Spanish.
    
    Returns:
        The UI for the lesson 1 page for Spanish.
    """
    return rx.chakra.vstack(
        rx.box(
            rx.chakra.heading("Lección 1: Entendiendo el Cambio Climático", text_color="white", font_size="3xl",
                              align='center'),
            background_color="gray",
            border_radius="5px",
            padding="8px",
        ),
        rx.chakra.text(
            "Nos embarcaremos en un viaje apasionante para explorar uno de los temas más urgentes de nuestro tiempo: el cambio climático.",
            mb=2, align='start'),
        rx.chakra.text("Objetivos: ", font_size="lg", mb=4, font_weight="bold", align='center'),
        rx.chakra.ordered_list(
            rx.chakra.list_item("Mejorar vuestras habilidades en español."),
            rx.chakra.list_item(
                "Profundizar en la comprensión de los desafíos ambientales, así como el papel que todos jugamos en su solución."),
            align='start'),
        rx.chakra.heading("Lo que Aprenderás:", font_size="lg", font_weight="bold", mb=2, align='center'),
        rx.chakra.ordered_list(
            rx.chakra.list_item(
                "Vocabulario Clave: Aprenderás términos esenciales relacionados con el cambio climático, fenómenos meteorológicos y conservación ambiental."),
            rx.chakra.list_item("Enfoque Gramatical: Introduciremos y practicaremos el tiempo futuro en español."),
            rx.chakra.list_item(
                "Discusión e Interacción: Después de una breve introducción al tema, con algo de vocabulario y gramática esencial, nos sumergiremos en una parte más dinámica de la lección."),
            align='start',
        ),
        rx.chakra.link(rx.chakra.button("Siguiente Lección"), href="/leccion1/gramatica", align='end'),
        footer(),
        spacing="2",
        padding="5px",
    )

@template(route="/leccion1/gramatica", title="Lección 1: Gramática")
def leccion1_gramatica() -> rx.Component:
    """Lesson 1 Spanish Grammar and Vocabulary.

    Returns:
        The UI for the lesson focusing on the future tense in Spanish and Vocabulary dealing with climate change to help students discuss this pressing issue.
    """
    return rx.chakra.vstack(
        rx.box(
            rx.chakra.heading("Lección 1: La Gramática del Tiempo Futuro", text_color="white", font_size="3xl", align='center'),
            background_color="gray",
            border_radius="5px",
            padding="8px",
        ),
        rx.chakra.text("Nos embarcaremos en un viaje apasionante para explorar uno de los temas más urgentes de nuestro tiempo: el cambio climático.", mb=2, align='start'),
        rx.chakra.text("Objetivos: ", font_size="lg", mb=4, font_weight="bold", align='center'),
        rx.chakra.ordered_list(
            rx.chakra.list_item("Mejorar vuestras habilidades en español."),
            rx.chakra.list_item(
                "Profundizar en la comprensión de los desafíos ambientales, así como el papel que todos jugamos en su solución."),
            align='start'),
        rx.chakra.heading("Lo que Aprenderás:", font_size="lg", font_weight="bold", mb=2, align='center'),
        rx.chakra.ordered_list(
            rx.chakra.list_item(
                "Vocabulario Clave: Aprenderás términos esenciales relacionados con el cambio climático, fenómenos meteorológicos y conservación ambiental."),
            rx.chakra.list_item("Enfoque Gramatical: Introduciremos y practicaremos el tiempo futuro en español."),
            rx.chakra.list_item("Discusión e Interacción: Después de una breve introducción al tema, con algo de vocabulario y gramática esencial, nos sumergiremos en una parte más dinámica de la lección."),
            align='start',
        ),
        rx.chakra.heading("Conjugación en Futuro", font_size="2xl", font_weight="bold", mb=2, align='center'),
        rx.chakra.text("Para formar el futuro en español, se añade las terminaciones -é, -ás, -á, -emos, -éis, -án directamente al infinitivo del verbo. Esto aplica para todos los verbos, regulares e irregulares.", mb=4, align='start'),
        rx.chakra.unordered_list(
            rx.chakra.list_item("Hablar: hablaré, hablarás, hablará, hablaremos, hablaréis, hablarán"),
            rx.chakra.list_item("Comer: comeré, comerás, comerá, comeremos, comeréis, comerán"),
            rx.chakra.list_item("Vivir: viviré, vivirás, vivirá, viviremos, viviréis, vivirán"),
            align='start',
        ),
        rx.chakra.heading("Vocabulario sobre Cambio Climático", font_size="2xl", font_weight="bold", mb=2, align='center'),
        rx.chakra.unordered_list(
            rx.chakra.list_item("Cambio climático: Climate change"),
            rx.chakra.list_item("Calentamiento global: Global warming"),
            rx.chakra.list_item("Efecto invernadero: Greenhouse effect"),
            rx.chakra.list_item("Desglaciación: Ice melt / Glacier melt"),
            rx.chakra.list_item("Energías renovables: Renewable energies"),
            rx.chakra.list_item("Conservación ambiental: Environmental conservation"),
            align='start',
        ),
        rx.chakra.link(rx.chakra.button("Siguiente Lección"), href="/leccion1/discusion1", align='end'),
        footer(),
        spacing="2",
        padding="5px",
    )
@template(route="/leccion1/discusion1", title="Lección 1: Discusión 1", on_load=ChatState.set_discussion1)
def leccion1_discusion1() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.heading("Lección 1: Discusión 1", font_size="3xl", mb=4, align='center'),
        rx.video(
            url="https://www.youtube.com/watch?v=GLTCiS6hOT4"),
        rx.chakra.text("Resume el video, por favor. ¿Cuáles son tres puntos principales?", font_weight='bold',
                       align='center'),
        chat(),
        rx.chakra.hstack(action_bar(),
                         transcribe_bar()),
        rx.chakra.link(rx.chakra.button("Next"), href="/leccion1/discusion2", align='end'),
    )


@template(route="/leccion1/discusion2", title="Lección 1: Discusión 2", on_load=ChatState.set_discussion2)
def leccion1_discusion2() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.heading("Lección 1: Discusión 2", font_size="3xl", mb=4, align='center'),
        rx.video(
            url="https://www.youtube.com/watch?v=GLTCiS6hOT4"),
        rx.chakra.text("Resume el video, por favor. ¿Cuáles son tres puntos principales?", font_weight='bold',
                       align='center'),
        chat(),
        action_bar(),
    )