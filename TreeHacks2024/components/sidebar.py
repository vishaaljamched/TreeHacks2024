"""Sidebar component for the app."""

from TreeHacks2024 import styles

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.chakra.hstack(
        # The logo.
        rx.chakra.image(
            src="/LogoFinal.svg",
            height="9em",
        ),
        rx.chakra.spacer(),
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )

def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url)

    return rx.chakra.link(
        rx.chakra.hstack(
            rx.chakra.image(
                src=icon,
                height="2.5em",
                padding="0.5em",
            ),
            rx.chakra.text(
                text,
            ),
            bg=rx.cond(
                active,
                styles.accent_color,
                "transparent",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
        ),
        href=url,
        width="100%",
        class_name="hover:scale-105 hover:brightness-90 duration-300",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.chakra.box(
        rx.chakra.vstack(
            sidebar_header(),
            rx.chakra.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        icon=page.get("image", page["image"]),
                        url=page["route"],
                    )
                    for page in get_decorated_pages() if ':' not in page.get("title", page["route"].strip("/").capitalize()) 
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.chakra.spacer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
