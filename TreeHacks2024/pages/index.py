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
    header = rx.container(
                rx.hstack(
                    rx.heading("Hola", class_name= "text-black-600"),
                    rx.heading("Vishaal Jamched", class_name="text-xl"),
                    class_name="justify-center flex-auto"
                ),
                rx.spacer(class_name="p-1"),
                rx.divider(),
                rx.spacer(class_name="p-2"),
                rx.link(
                    rx.chakra.box(
                        rx.text("Lección 1", class_name="font-bold text-lg"),
                        rx.hstack(
                            rx.text("Progress:", class_name=""),
                            rx.progress(value = 37, width="100%"),
                            rx.text("37%"),
                    ), 
                    class_name="shadow p-5 rounded-md hover:scale-105 hover:cursor-pointer duration-300"),
                    href="/leccion1/intro", class_name="decoration-black hover:no-underline"
                ),

                rx.chakra.box(
                        rx.text("Lección 2", class_name="font-bold text-lg"),
                        rx.hstack(
                            rx.text("Progress:", class_name=""),
                            rx.progress(value = 0, width="100%"),
                            rx.text("0"),
                    ), 
                    class_name="shadow p-5 rounded-md hover:scale-105 duration-300 my-4"
                ),

                rx.chakra.box(
                        rx.text("Lección 3", class_name="font-bold text-lg"),
                        rx.hstack(
                            rx.text("Progress:", class_name=""),
                            rx.progress(value = 0, width="100%"),
                            rx.text("0"),
                    ), 
                    class_name="shadow p-5 rounded-md hover:scale-105 duration-300"
                )
                
        )
        
    return rx.hstack(header)

