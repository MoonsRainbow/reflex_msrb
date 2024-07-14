import reflex as rx


def button(
        _on_click,
        _props: dict,
        _icon=None,
        _image=None,
        _text=None,
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
