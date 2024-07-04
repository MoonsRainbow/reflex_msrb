from reflex_msrb.states import BaseState

import reflex as rx


class FooterBaseState(BaseState):
    pass


def footer_bar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.text(
                'This is the footer',
                color='white'
            ),
        ),
        align='end',
        justify='center',
        width='100%',
        padding='50px',
        background='#444',
        box_shadow='rgba(0, 0, 0, 0.2) 0 -4px 8px 4px',
    )
