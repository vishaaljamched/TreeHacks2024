"""The home page of the app."""

from TreeHacks2024 import styles
from TreeHacks2024.templates import template

import reflex as rx


@template(route="/", title="Home", image="/home.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    header= rx.container(
                rx.hstack(
                    rx.heading("Hola", class_name= "text-black-600 flex-initial"),
                    rx.text("Vishaal Jamched", class_name="text-xl flex-auto")
                    # Theme and User Pin
                ),
                rx.chakra.box(
                    rx.text("Hello World"), class_name="py-3", style=styles.template_content_style,
                ),
                direction="column"
            )
    
    return rx.hstack(header)

