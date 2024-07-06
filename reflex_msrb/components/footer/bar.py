import reflex as rx

from reflex_msrb.states import BaseState
from reflex_msrb.styles import (
    light_mode,
    dark_mode,
)


class FooterBaseState(BaseState):
    pass


def footer_bar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.text(
                'This is the footer',
                color=rx.color_mode_cond(
                    light=light_mode['text_color'],
                    dark=dark_mode['text_color']
                )
            ),
        ),
        align='end',
        justify='center',
        width='100%',
        padding='50px',
        box_shadow='rgba(0, 0, 0, 0.2) 0 -4px 8px 4px',
        background=rx.color_mode_cond(
            light=light_mode['footer_background_color'],
            dark=dark_mode['footer_background_color'],
        ),
    )
