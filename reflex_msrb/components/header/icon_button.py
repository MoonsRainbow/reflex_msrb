import reflex as rx


def header_icon_button(
        _icon: str,
        _on_click,
) -> rx.Component:
    return rx.button(
        rx.icon(
            _icon
        ),
        width='30px',
        height='30px',
        variant='ghost',
        radius='none',
        color='white',
        size='2',
        color_schema=None,
        on_click=_on_click
    )
