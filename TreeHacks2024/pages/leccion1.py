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
        rx.chakra.link(rx.chakra.button("Next"), href="/leccion1/discusion1", align='end'),
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