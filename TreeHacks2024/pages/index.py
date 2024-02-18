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
    header = rx.chakra.container(
        rx.chakra.hstack(
            rx.chakra.heading("Hola", class_name="text-black-600"),
            rx.chakra.heading("Vishaal Jamched", class_name="text-xl"),
            class_name="justify-center flex-auto"
        ),
        rx.chakra.spacer(class_name="p-1"),
        rx.chakra.divider(),
        rx.chakra.spacer(class_name="p-2"),
        rx.chakra.link(
            rx.chakra.box(
                rx.chakra.text("Lección 1", class_name="font-bold text-lg no-underline"),
                rx.chakra.hstack(
                    rx.chakra.text("Progress:", class_name=""),
                    rx.chakra.progress(value=37, width="100%"),
                    rx.chakra.text("37%"),
                ),
                class_name="shadow p-5 rounded-md hover:scale-105 hover:cursor-pointer duration-300"),
            href="/leccion1/intro", class_name="hover:no-underline"
        ),

        rx.chakra.box(
            rx.chakra.text("Lección 2", class_name="font-bold text-lg"),
            rx.chakra.hstack(
                rx.chakra.text("Progress:", class_name=""),
                rx.chakra.progress(value=0, width="100%"),
                rx.chakra.text("0"),
            ),
            class_name="shadow p-5 rounded-md hover:scale-105 duration-300 my-4"
        ),

        rx.chakra.box(
            rx.chakra.text("Lección 3", class_name="font-bold text-lg"),
            rx.chakra.hstack(
                rx.chakra.text("Progress:", class_name=""),
                rx.chakra.progress(value=0, width="100%"),
                rx.chakra.text("0"),
            ),
            class_name="shadow p-5 rounded-md hover:scale-105 duration-300"
        )

    )

    return rx.chakra.hstack(header)
