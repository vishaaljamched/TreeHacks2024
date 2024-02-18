import reflex as rx
from TreeHacks2024.chat_state import ChatState, QA
from TreeHacks2024.backend.speechToText import main
def message(qa: QA) -> rx.Component:
    """A single question/answer message.

    Args:
        qa: The question/answer pair.

    Returns:
        A component displaying the question/answer pair.
    """
    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.text(
                qa.question,
                class_name="text-white shadow",
            ),
            text_align="right",
            class_name="shadow bg-gray-500 rounded-md mt-2 px-2",
        ),
        rx.chakra.box(
            rx.chakra.text(
                qa.answer,
                class_name="text-white shadow",
            ),
            text_align="left",
            class_name="shadow bg-gray-800 rounded-md mt-2 px-2",
        ),
        width="100%",
        class_name="shrink",
    )

def chat() -> rx.Component:
    """List all the messages in a single conversation."""
    return rx.chakra.vstack(
        rx.chakra.box(rx.foreach(ChatState.chats[ChatState.current_chat], message)),
        py="8",
        flex="1",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
        class_name="shadow-lg",
    )

def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.form(
                rx.chakra.form_control(
                    rx.chakra.hstack(
                        rx.chakra.input(
                            placeholder="Type something...",
                            id="question",
                            _placeholder={"color": "#fffa"},
                        ),
                        rx.chakra.button(
                            rx.chakra.image(
                                src='/send.svg',
                                height="2.5em",
                                padding="0.5em",
                            ),
                            rx.cond(
                                ChatState.processing,
                                rx.chakra.text("Sending"),
                                rx.chakra.text("Send"),
                            ),
                            type_="submit",
                            color_scheme="blue",
                            class_name="hover:scale-105 duration-300",
                        ),
                    ),
                    is_disabled=ChatState.processing,
                ),
                on_submit=ChatState.process_question,
                reset_on_submit=True,
                width="100%",
            ),
            rx.chakra.text(
                "Polyglot.AI may return factually incorrect or misleading responses. Use discretion.",
                font_size="xs",
                color="#e2f4e9",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
            backdrop_filter="auto",
            backdrop_blur="sm",
        ),
        position="sticky",
        bottom="0",
        left="0",
        py="4",
        align_items="stretch",
        width="100%",
    )

def transcribe_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.form(
                rx.chakra.form_control(
                        rx.chakra.button(
                            rx.chakra.image(
                                src='/send.svg',
                                height="2.5em",
                                padding="0.5em",
                            ),
                            rx.cond(
                                ChatState.processing,
                                rx.chakra.text("Sending"),
                                rx.chakra.text("Send"),
                            ),
                            type_="submit",
                            color_scheme="blue",
                            class_name="hover:scale-105 duration-300",
                        ),
                    is_disabled=ChatState.processing,
                ),
                on_submit= ChatState.transcribe_question,
                reset_on_submit=True,
                width="100%",
            ),
            rx.chakra.text(
                "Polyglot.AI may return factually incorrect or misleading responses. Use discretion.",
                font_size="xs",
                color="#e2f4e9",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
            backdrop_filter="auto",
            backdrop_blur="sm",
        ),
        position="sticky",
        bottom="0",
        left="0",
        py="4",
        align_items="stretch",
        width="100%",
    )