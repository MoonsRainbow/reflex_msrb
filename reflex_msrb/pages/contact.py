from .template import wrap_template
from reflex_msrb.states import BaseState
from reflex_msrb.routes import CONTACT_ROUTE

import reflex as rx


class ContactState(BaseState):
    page_title: list[str] = ['연락처', 'Contact']


@rx.page(
    route=CONTACT_ROUTE,
    title=f"{ContactState.page_title[ContactState.language]} | MoonsRainbow"
)
@wrap_template
def contact() -> rx.Component:
    return rx.flex(
        rx.text(
            'Contact World!',
        ),
        align='center',
        justify='center',
        width='100%',
        height='100%',
    )
