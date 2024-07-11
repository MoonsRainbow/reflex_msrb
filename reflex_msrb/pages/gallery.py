from .template import wrap_template
from reflex_msrb.states import BaseState
from reflex_msrb.routes import GALLERY_ROUTE

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
        rx.text(
            'Gallery World!',
        ),
        align='center',
        justify='center',
        width='100%',
        height='100%',
    )
