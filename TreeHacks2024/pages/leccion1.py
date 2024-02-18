"""The Lección 1 page."""
from TreeHacks2024.templates import template

import reflex as rx
@template(route="/leccion1/intro", title="Lección 1")
def leccion1() -> rx.Component:
    """Lesson 1 Spanish.
    
    Returns:
        The UI for the lesson 1 page for Spanish.
    """
    return rx.chakra.vstack(
        rx.chakra.heading("Lección 1: Entendiendo el Cambio Climático", font_size="3xl", mb=4, align = 'center'),
        rx.chakra.text("Nos embarcaremos en un viaje apasionante para explorar uno de los temas más urgentes de nuestro tiempo: el cambio climático.", mb=2, align = 'start'),
        rx.chakra.text("Objetivos: ", font_size="lg", mb=4, font_weight="bold", align = 'center'),
        rx.ordered_list(
            rx.list_item("Mejorar vuestras habilidades en español."),
            rx.list_item("Profundizar en la comprensión de los desafíos ambientales, así como el papel que todos jugamos en su solución."),
            align = 'start'),
        rx.chakra.heading("Lo que Aprenderás:", font_size="lg", font_weight="bold", mb=2, align='center'),
        rx.ordered_list(
            rx.list_item("Vocabulario Clave: Aprenderás términos esenciales relacionados con el cambio climático, fenómenos meteorológicos y conservación ambiental."),
            rx.list_item("Enfoque Gramatical: Introduciremos y practicaremos el tiempo futuro en español."),
            rx.list_item("Discusión e Interacción: Después de una breve introducción al tema, con algo de vocabulario y gramática esencial, nos sumergiremos en una parte más dinámica de la lección."),
            align = 'start' 
            ),
        rx.chakra.link(rx.button("Next"), href = "/leccion1/discusion1", align='end'),
        spacing="2",
        padding="5px",
    )

@template(route="/leccion1/discusion1", title="Lección 1: Discusión 1")
def leccion1_discusion1() -> rx.Component:
    
    return rx.chakra.vstack(rx.chakra.text("Discusión 1"))