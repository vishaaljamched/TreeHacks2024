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
    header= rx.flex(
                rx.hstack(
                    rx.heading("WELCOME TO POLYGON.AI", class_name= "text-9x1 text-black-600 flex-initial"),
                    rx.text("Vishaal Jamched", class_name="text-md align-middle py-1 px-2 flex-auto")
                ),
                rx.text("Hello WOrld"),
                direction="column"
            )
    
    return rx.hstack(header)

