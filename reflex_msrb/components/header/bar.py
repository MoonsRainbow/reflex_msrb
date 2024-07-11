import reflex as rx
from reflex.style import toggle_color_mode
from reflex_msrb.states import BaseState
from reflex_msrb.routes import *

from .button import (
    logo_button,
    icon_button,
    menu_button,
)


def header_bar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.hstack(
                logo_button(
                    _on_click=rx.redirect(HOME_ROUTE)
                ),
                width='20%',
                align='center',
                justify='start',
                spacing='4',
            ),
            rx.hstack(
                menu_button(
                    _text=rx.cond(
                        BaseState.language,
                        'Welcome',
                        '환영합니다'
                    ),
                    _highlight=rx.cond(
                        BaseState.router.page.path == HOME_ROUTE,
                        True,
                        False
                    ),
                    _on_click=rx.redirect(HOME_ROUTE),
                ),
                menu_button(
                    _text=rx.cond(
                        BaseState.language,
                        'About Me',
                        '소개'
                    ),
                    _highlight=rx.cond(
                        BaseState.router.page.path == ABOUT_ME_ROUTE,
                        True,
                        False
                    ),
                    _on_click=rx.redirect(ABOUT_ME_ROUTE),
                ),
                menu_button(
                    _text=rx.cond(
                        BaseState.language,
                        'Skill Stack',
                        '기술 스택'
                    ),
                    _highlight=rx.cond(
                        BaseState.router.page.path == SKILL_STACK_ROUTE,
                        True,
                        False
                    ),
                    _on_click=rx.redirect(SKILL_STACK_ROUTE),
                ),
                menu_button(
                    _text=rx.cond(
                        BaseState.language,
                        'Gallery',
                        '갤러리'
                    ),
                    _highlight=rx.cond(
                        BaseState.router.page.path == GALLERY_ROUTE,
                        True,
                        False
                    ),
                    _on_click=rx.redirect(GALLERY_ROUTE),
                ),
                menu_button(
                    _text=rx.cond(
                        BaseState.language,
                        'Contact',
                        '연락처'
                    ),
                    _highlight=rx.cond(
                        BaseState.router.page.path == CONTACT_ROUTE,
                        True,
                        False
                    ),
                    _on_click=rx.redirect(CONTACT_ROUTE),
                ),
                width='60%',
                align='center',
                justify='center',
                spacing='4',
            ),
            rx.hstack(
                icon_button(
                    _icon=rx.icon('languages'),
                    _on_click=BaseState.change_language,
                ),
                icon_button(
                    _icon=rx.color_mode_cond(
                        light=rx.icon('sun'),
                        dark=rx.icon('moon'),
                    ),
                    _on_click=toggle_color_mode,
                ),
                width='20%',
                align='center',
                justify='end',
                spacing='4',
            ),
            align='center',
            justify='between',
            width='100%',
            spacing='0',
            padding='24px',
        ),
        position='fixed',
        align='center',
        justify='center',
        width='100%',
        height='68px',
        top='0px',
        left='0px',
        background='#444',
        box_shadow='rgba(0, 0, 0, 0.2) 0 4px 8px 4px',
    )
