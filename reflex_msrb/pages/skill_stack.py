from .template import wrap_template
from reflex_msrb.states import BaseState
from reflex_msrb.routes import SKILL_STACK_ROUTE

import reflex as rx


class SkillStackState(BaseState):
    page_title: list[str] = ['기술 스택', 'Skill Stack']


@rx.page(
    route=SKILL_STACK_ROUTE,
    title=f"{SkillStackState.page_title[SkillStackState.language]} | MoonsRainbow"
)
@wrap_template
def skill_stack() -> rx.Component:
    return rx.flex(
        rx.text(
            'Skill Stack World!',
        ),
        align='center',
        justify='center',
        width='100%',
        height='100%',
    )
