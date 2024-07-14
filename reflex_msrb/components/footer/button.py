import reflex as rx
from ..common import button
from reflex_msrb.styles import footer as style_lib


def icon_button(
        _icon: rx.icon,
        _on_click,
) -> rx.Component:
    return button(
        _icon=_icon,
        _on_click=_on_click,
        _props=style_lib.icon_button,
    )
