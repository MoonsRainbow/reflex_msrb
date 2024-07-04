import reflex as rx


def header_logo(
        _on_click
) -> rx.Component:
    return rx.button(
        rx.image(
            src='/msrb_logo.png',
            width='180px',
        ),
        # width='30px',
        height='30px',
        variant='ghost',
        radius='none',
        color='white',
        size='2',
        color_schema=None,
        on_click=_on_click
    )
