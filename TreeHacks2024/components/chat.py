import reflex as rx
from TreeHacks2024.chat_state import ChatState, QA
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
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.chakra.box(
            rx.chakra.text(
                qa.answer),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
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
                                rx.chakra.text("Send"),
                            ),
                            type_="submit",
                        ),
                    ),
                    is_disabled=ChatState.processing,
                ),
                on_submit=ChatState.process_question,
                reset_on_submit=True,
                width="100%",
            ),
            rx.chakra.text(
                "ReflexGPT may return factually incorrect or misleading responses. Use discretion.",
                font_size="xs",
                color="#fff6",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
        ),
        position="sticky",
        bottom="0",
        left="0",
        py="4",
        backdrop_filter="auto",
        backdrop_blur="lg",
        align_items="stretch",
        width="100%",
    )