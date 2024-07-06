import reflex as rx


def header_icon_button(
        _icon: rx.icon,
        _on_click,
) -> rx.Component:
    return rx.button(
        _icon,
        width='44px',
        height='44px',
        variant='ghost',
        color='white',
        cursor='pointer',
        on_click=_on_click
    )
