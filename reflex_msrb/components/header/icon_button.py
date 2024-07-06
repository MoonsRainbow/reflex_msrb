import reflex as rx
from reflex_msrb.styles import (
    light_mode,
    dark_mode,
)


def header_icon_button(
        _icon: rx.icon,
        _on_click,
) -> rx.Component:
    return rx.button(
        _icon,
        width='44px',
        height='44px',
        variant='ghost',
        cursor='pointer',
        color=rx.color_mode_cond(
            light=light_mode['icon_color'],
            dark=dark_mode['icon_color']
        ),
        on_click=_on_click
    )
