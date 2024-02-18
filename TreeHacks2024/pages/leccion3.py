"""The Lección 3 page."""
from TreeHacks2024.templates import template
from TreeHacks2024.components.chat import chat, action_bar
import requests

import reflex as rx
@template(route="/leccion3/intro", title="Lección 3", image="/Lock.svg")
def leccion3() -> rx.Component:
    """Lesson 3 Spanish.
    
    Returns:
        The UI for the lesson 3 page for Spanish.
    """
    return rx.chakra.vstack(
        rx.chakra.heading("Lección 3: Entendiendo el Cambio Climático", font_size="3xl", mb=4, align = 'center'),
        rx.chakra.text("Nos embarcaremos en un viaje apasionante para explorar uno de los temas más urgentes de nuestro tiempo: el cambio climático.", mb=2, align = 'start'),
        rx.chakra.text("Objetivos: ", font_size="lg", mb=4, font_weight="bold", align = 'center'),
        rx.chakra.ordered_list(
            rx.chakra.list_item("Mejorar vuestras habilidades en español."),
            rx.chakra.list_item("Profundizar en la comprensión de los desafíos ambientales, así como el papel que todos jugamos en su solución."),
            align = 'start'),
        rx.chakra.heading("Lo que Aprenderás:", font_size="lg", font_weight="bold", mb=2, align='center'),
        rx.chakra.ordered_list(
            rx.chakra.list_item("Vocabulario Clave: Aprenderás términos esenciales relacionados con el cambio climático, fenómenos meteorológicos y conservación ambiental."),
            rx.chakra.list_item("Enfoque Gramatical: Introduciremos y practicaremos el tiempo futuro en español."),
            rx.chakra.list_item("Discusión e Interacción: Después de una breve introducción al tema, con algo de vocabulario y gramática esencial, nos sumergiremos en una parte más dinámica de la lección."),
            align = 'start',
            ),
        rx.chakra.link(rx.chakra.button("Next"), href = "/leccion3/discusion1", align='end'),
        spacing="2",
        padding="5px",
    )

@template(route="/leccion3/discusion1", title="Lección 3: Discusión 1")
def leccion2_discusion1() -> rx.Component:
    return rx.chakra.vstack(
        rx.video(
            url="https://www.youtube.com/watch?v=GLTCiS6hOT4"),
        chat(),
        action_bar()
    )
