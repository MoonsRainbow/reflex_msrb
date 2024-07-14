import reflex as rx
from ..common import button
from reflex_msrb.styles import header as style_lib


def icon_button(
        _icon: rx.icon,
        _on_click,
) -> rx.Component:
    return button(
        _icon=_icon,
        _on_click=_on_click,
        _props=style_lib.icon_button,
    )


def logo_button(
        _on_click
) -> rx.Component:
    return button(
        _image=rx.image(
            src='/logo.png',
            width='180px',
        ),
        _on_click=_on_click,
        _props=style_lib.logo_button,
    )


def menu_button(
        _text: rx.Var,
        _on_click,
        _highlight: bool | rx.Var = False
) -> rx.Component:
    return rx.cond(
        _highlight,
        button(
            _text=_text,
            _on_click=_on_click,
            _props=style_lib.menu_button_highlight_on,
        ),
        button(
            _text=_text,
            _on_click=_on_click,
            _props=style_lib.menu_button_highlight_off,
        )
    )
