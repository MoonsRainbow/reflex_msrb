import reflex as rx


def text_link(
        _text: str | rx.Var,
        _route: str,
) -> rx.Component:
    return rx.link(
        _text,
        href=_route,
        color='#AAA',
        underline='none',
        color_scheme='yellow',
    )
