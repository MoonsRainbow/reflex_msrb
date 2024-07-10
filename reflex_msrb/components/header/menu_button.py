import reflex as rx
from reflex_msrb.states import BaseState


def header_menu_button(_text: list[str]) -> rx.Component:
    return rx.card(
        rx.button(
            _text[BaseState.language]

        ),
        as_child=True
    )
