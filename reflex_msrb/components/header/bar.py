import reflex as rx
from reflex_msrb.states import BaseState
from reflex_msrb.routes import (
    HOME_ROUTE,
    ABOUT_ME_ROUTE,
)

from .logo import header_logo
from .icon_button import header_icon_button


class HeaderState(BaseState):
    language_text: list[str] = ['English (영어)', '한국어 (Korea)']


def header_bar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.hstack(
                header_icon_button(
                    _icon='align-justify',
                    _on_click=rx.redirect(ABOUT_ME_ROUTE),
                ),
                header_logo(
                    _on_click=rx.redirect(HOME_ROUTE)
                ),
                align='center',
                justify='start',
                spacing='6',
            ),
            header_icon_button(
                _icon='languages',
                _on_click=HeaderState.change_language,
            ),
            align='center',
            justify='between',
            width='100%',
            spacing='0',
            padding='24px',
        ),
        position='fixed',
        align='center',
        justify='center',
        width='100%',
        height='66px',
        top='0px',
        left='0px',
        background='#444',
        box_shadow='rgba(0, 0, 0, 0.2) 0 4px 8px 4px',
    )
