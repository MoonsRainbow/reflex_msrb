import reflex as rx
from reflex_msrb.styles import header as style_lib


def button(
        _props: dict[str, str | rx.Var],
        _on_click,
        _icon=None,
        _image=None,
        _text=None,
        _highlight: bool = False
) -> rx.Component:
    _children = []
    if _icon is not None:
        _children.append(_icon)
    if _image is not None:
        _children.append(_image)
    if _text is not None:
        _children.append(_text)
    return rx.button(
        *_children,
        on_click=_on_click,
        **_props,
    )


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
            src='/msrb_logo.png',
            width='180px',
        ),
        _on_click=_on_click,
        _props=style_lib.logo_button,
    )


def menu_button(
        _text: rx.Var,
        _on_click,
        _highlight
) -> rx.Component:
    return button(
        _text=_text,
        _on_click=_on_click,
        _highlight=_highlight,
        _props={
            **style_lib.logo_button,
            'width': '80px',
            'color': rx.cond(
                _highlight,
                '#FFF',
                '#AAA'
            ),
            'fontWeight': rx.cond(
                _highlight,
                'bold',
                'normal'
            )
        },
    )
