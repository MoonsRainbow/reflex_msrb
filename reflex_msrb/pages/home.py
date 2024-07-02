from .template import wrap_template
from reflex_msrb.states import State
from reflex_msrb.routes import HOME_ROUTE

import reflex as rx


class HomeState(State):
    pass


@rx.page(
    route=HOME_ROUTE,
    title='Home | MoonsRainbow'
)
@wrap_template
def home() -> rx.Component:
    return rx.flex(
        width='100%',
        height='100%',
        background='orange',
    )
