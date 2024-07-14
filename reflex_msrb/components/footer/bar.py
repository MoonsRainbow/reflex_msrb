import reflex as rx
from reflex_msrb.routes import *
from reflex_msrb.states import BaseState
from .button import (
    icon_button
)
from .link import (
    text_link
)
from .divider import (
    link_divider
)


class FooterBaseState(BaseState):
    pass


def footer_bar() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.vstack(
                        rx.image(
                            src='/logo.png',
                            height='56px',
                        ),
                        rx.text(
                            rx.cond(
                                BaseState.language,
                                'Software Engineer & Software Designer',
                                '소프트웨어 엔지니어 & 소프트웨어 기획자'
                            ),
                            color='#BBB',
                        ),
                        align='center',
                        justify='center',
                        spacing='0',
                    ),
                    width='30%',
                ),
                rx.hstack(
                    text_link(
                        _text=rx.cond(
                            BaseState.language,
                            'Welcome',
                            '환영합니다'
                        ),
                        _route=HOME_ROUTE,
                    ),
                    link_divider(),
                    text_link(
                        _text=rx.cond(
                            BaseState.language,
                            'About Me',
                            '소개'
                        ),
                        _route=ABOUT_ME_ROUTE,
                    ),
                    link_divider(),
                    text_link(
                        _text=rx.cond(
                            BaseState.language,
                            'Skill Stack',
                            '기술 스택'
                        ),
                        _route=SKILL_STACK_ROUTE,
                    ),
                    link_divider(),
                    text_link(
                        _text=rx.cond(
                            BaseState.language,
                            'Gallery',
                            '갤러리'
                        ),
                        _route=GALLERY_ROUTE,
                    ),
                    link_divider(),
                    text_link(
                        _text=rx.cond(
                            BaseState.language,
                            'Contact',
                            '연락처'
                        ),
                        _route=CONTACT_ROUTE,
                    ),
                    width='40%',
                    align='center',
                    justify='center',
                    spacing='4',
                ),
                rx.vstack(
                    rx.hstack(
                        icon_button(
                            _icon=rx.icon('github'),
                            _on_click=rx.redirect(
                                'https://github.com/MoonsRainbow',
                                external=True
                            ),
                        ),
                    ),
                    align='end',
                    justify='center',
                    width='30%',
                ),
                width='100%',
                align='center',
                justify='between'
            ),
            rx.hstack(
                rx.vstack(
                    rx.divider(
                        width='80%',
                        margin='8px 0 8px 0',
                        color_scheme='yellow',
                        decorative=True,
                    ),
                    rx.text(
                        'ⓒ 2024. MoonsRainbow All rights reserved.',
                        color='#BBB',
                    ),
                    width='30%',
                    align='end',
                    justify='center'
                ),
                width='100%',
                align='center',
                justify='end',
            ),
            width='100%',
            align='center',
            justify='center',
        ),
        align='end',
        justify='start',
        width='100%',
        padding='24px',
        background='#444',
        box_shadow='rgba(0, 0, 0, 0.2) 0 -4px 8px 4px',
    )
