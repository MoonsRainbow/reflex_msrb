import reflex as rx
from reflex.style import toggle_color_mode

from reflex_msrb.states import BaseState
from reflex_msrb.routes import (
    HOME_ROUTE,
    ABOUT_ME_ROUTE,
)

from .logo import header_logo
from .icon_button import header_icon_button


def header_bar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.hstack(
                header_icon_button(
                    _icon=rx.icon('align-justify'),
                    _on_click=rx.redirect(ABOUT_ME_ROUTE),
                ),
                header_logo(
                    _on_click=rx.redirect(HOME_ROUTE)
                ),
                align='center',
                justify='start',
            ),
            rx.hstack(
                header_icon_button(
                    _icon=rx.icon('languages'),
                    _on_click=BaseState.change_language,
                ),
                header_icon_button(
                    _icon=rx.color_mode_cond(
                        light=rx.icon('sun'),
                        dark=rx.icon('moon'),
                    ),
                    _on_click=toggle_color_mode,
                ),
                align='center',
                justify='end',
            ),
            align='center',
            justify='between',
            width='100%',
            spacing='0',
            padding='12px',
        ),
        position='fixed',
        align='center',
        justify='center',
        width='100%',
        height='68px',
        top='0px',
        left='0px',
        # TODO light mode color choice
        background=rx.color_mode_cond(
            light='#444',
            dark='#444',
        ),
        box_shadow='rgba(0, 0, 0, 0.2) 0 4px 8px 4px',
    )
