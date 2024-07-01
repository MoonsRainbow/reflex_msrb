from typing import Callable
from reflex_msrb.components import header, footer

import reflex as rx


META = [
    {
        'name': 'viewport',
        'content': 'width=device-width, shrink-to-fit=no, initial-scale=1',
    },
]


def wrap_template(_content: Callable[[], rx.Component]) -> rx.Component:
    return rx.vstack(
        header(),
        _content(),
        footer(),
        align='center',
        justify='between',
        width='100%',
        height='120vh',
        background='blue',
        spacing='0',
    )
