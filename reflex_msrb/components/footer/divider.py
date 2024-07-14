import reflex as rx


def link_divider() -> rx.Component:
    return rx.divider(
        height='10px',
        color_scheme='yellow',
        orientation='vertical',
        decorative=True
    )
