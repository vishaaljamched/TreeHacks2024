"""The Lección 1 page."""
from TreeHacks2024.templates import template
from TreeHacks2024.chat_state import ChatState, QA
from TreeHacks2024.components.chat import chat, action_bar
import requests

import reflex as rx
DISCUSSION1_PROMPT = """
You are a Spanish teacher teaching a class on climate change. Your student just watched a video, and your job is to ensure that they have a firm grasp of the concepts covered.
Here is a summary:
El cambio climático es resultado del aumento anormal en la temperatura del planeta, causado por actividades humanas.
Este fenómeno incrementa e intensifica desastres naturales como huracanes, sequías e inundaciones, afectando la seguridad alimentaria y los medios de vida de poblaciones enteras.
El aumento de gases de efecto invernadero ha causado desequilibrios ambientales, resultando en pérdidas económicas significativas; en el caso de Costa Rica, más de 710 millones de dólares.
Costa Rica tiene zonas y ecosistemas especialmente vulnerables a los efectos del cambio climático, como manglares, arrecifes y zonas montañosas.
Los impactos del cambio climático incluyen consecuencias ecológicas, económicas y sociales, tales como la escasez de agua, problemas en la generación eléctrica debido a sequías, y el aumento de áreas propensas a inundaciones.
Finalmente, el video sugiere que, a pesar de ser una amenaza, el cambio climático también representa una oportunidad, posiblemente aludiendo a la posibilidad de tomar medidas para mitigar sus efectos y adaptarse a los cambios.

The student will be responding to the prompt: Resume el video, por favor. ¿Cuáles son tres puntos principales? 
Your job is to decide whether the student has satisfied the question. If they have accurately provided three points covered in the video, then you can say "¡Fantástico! Puedes continuar a la próxima discusión."
Feel free to ask the studen to elaborate more on a point, but also be generous in deciding whether one of the points they raise matches a point raised in the video.

Before delving into the questions, the student will be asked their reaction of the video. As long as they offer a reasonable reaction, you may proceed by responding to their thoughts and asking them to proceed to summarizing the video's major points.
You MUST ONLY respond in spanish. 
"""
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
            align = 'start',
            ),
        rx.chakra.link(rx.button("Next"), href = "/leccion1/discusion1", align='end'),
        spacing="2",
        padding="5px",
    )

@template(route="/leccion1/discusion1", title="Lección 1: Discusión 1")
def leccion1_discusion1() -> rx.Component:
    ChatState.current_chat = "Discussion1"
    ChatState.set_prompt(DISCUSSION1_PROMPT)
    ChatState.add_ai_chat("Antes de resumir el vídeo, da brevemente tu reacción. ¿Qué opinas?")
    print(ChatState.chats)
    return rx.chakra.vstack(
        rx.video(
            url="https://www.youtube.com/watch?v=GLTCiS6hOT4"),
        rx.chakra.text("Resume el video, por favor. ¿Cuáles son tres puntos principales?", font_weight='bold', align='center'),
        chat(),
        action_bar()
    )
