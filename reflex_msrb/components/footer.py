from reflex_msrb.states import State

import reflex as rx


class FooterState(State):
    pass


def footer() -> rx.Component:
    _footer_props = {
        'align': 'end',
        'justify': 'center',
        'width': '100%',
        'padding': '50px',
        'background': '#444',
    }

    return rx.flex(
        rx.hstack(
            rx.text(
                'This is the footer',
                color='white'
            ),
        ),
        **_footer_props,
    )
