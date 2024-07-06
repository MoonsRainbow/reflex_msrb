import reflex as rx


def header_logo(
        _on_click
) -> rx.Component:
    return rx.button(
        rx.image(
            src='/msrb_logo.png',
            width='180px',
        ),
        height='44px',
        variant='ghost',
        cursor='pointer',
        on_click=_on_click
    )
