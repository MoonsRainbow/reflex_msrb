from typing import Callable
from reflex_msrb.components import (
    header_bar,
    footer_bar,
)

import reflex as rx

META = [
    {
        'name': 'viewport',
        'content': 'width=device-width, shrink-to-fit=no, initial-scale=1',
        'charset': 'UTF-8',
        'http-equiv': 'refresh',
    },
]


def wrap_template(_content: Callable[[], rx.Component]) -> rx.Component:
    return rx.theme(
        rx.vstack(
            header_bar(),
            _content(),
            footer_bar(),
            align='center',
            justify='between',
            width='100%',
            height='120vh',
            spacing='0',
        ),
    )
