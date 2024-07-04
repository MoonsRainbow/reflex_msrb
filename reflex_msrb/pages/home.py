from .template import wrap_template
from reflex_msrb.states import BaseState
from reflex_msrb.routes import HOME_ROUTE

import reflex as rx


class HomeBaseState(BaseState):
    page_title: list[str] = ['홈', 'Home']


@rx.page(
    route=HOME_ROUTE,
    title=f"{HomeBaseState.page_title[HomeBaseState.language]} | MoonsRainbow"
)
@wrap_template
def home() -> rx.Component:
    return rx.flex(
        width='100%',
        height='100%',
        background='orange',
    )
