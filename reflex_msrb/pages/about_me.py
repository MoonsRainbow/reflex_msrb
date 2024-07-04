from .template import wrap_template
from reflex_msrb.states import BaseState
from reflex_msrb.routes import ABOUT_ME_ROUTE

import reflex as rx


class AboutMeBaseState(BaseState):
    page_title: list[str] = ['소개', 'About Me']


@rx.page(
    route=ABOUT_ME_ROUTE,
    title=f"{AboutMeBaseState.page_title[AboutMeBaseState.language]} | MoonsRainbow"
)
@wrap_template
def about_me() -> rx.Component:
    return rx.flex(
        rx.text(
            'Hello World!',
            color='white',
        ),
        align='center',
        justify='center',
        width='100%',
        height='100%',
        background='blue',
    )
