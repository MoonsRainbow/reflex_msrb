from .template import wrap_template
from reflex_msrb.states import BaseState
from reflex_msrb.routes import GALLERY_ROUTE
from reflex_msrb.styles import (
    pages_style
)

import reflex as rx


class GalleryState(BaseState):
    page_title: list[str] = ['갤러리', 'Gallery']


@rx.page(
    route=GALLERY_ROUTE,
    title=f"{GalleryState.page_title[GalleryState.language]} | MoonsRainbow"
)
@wrap_template
def gallery() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading(
                rx.cond(
                    GalleryState.language,
                    GalleryState.page_title[1],
                    GalleryState.page_title[0]
                ),
                width='100%',
                size='9',
                text_align='center',
            ),
            rx.input(
                rx.input.slot(
                    rx.icon(
                        'search',
                        size=20,
                    )
                ),
                width='60%',
                variant='soft',
                radius='full',
                size='3',
            ),
            width='100%',
            align='center',
            justify='center',
            spacing='6',
        ),
        **pages_style,
    )
