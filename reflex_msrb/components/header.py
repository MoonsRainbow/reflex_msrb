from reflex_msrb.states import State

import reflex as rx


class HeaderState(State):

    def change_language(self):
        self.language += 1
        if len(self.language_list) <= self.language:
            self.language = 0


def header() -> rx.Component:
    _header_props = {
        'position': 'fixed',
        'align': 'center',
        'justify': 'center',
        'width': '100%',
        'height': '66px',
        'top': '0px',
        'left': '0px',
        'background': '#444',
    }

    _header_group_props = {
        'align': 'center',
        'justify': 'between',
        'width': '100%',
        'spacing': '0',
        'padding': '24px',
    }

    _header_icon_button_props = {
        'variant': 'ghost',
        'radius': 'none',
        'color': 'white',
        'size': '2',
        'color-schema': None,
    }

    return rx.flex(
        rx.hstack(
            rx.icon_button(
                'align-justify',
                on_click=rx.redirect('/home'),
            ),
            rx.hstack(
                rx.icon_button(
                    'align-justify',
                    **_header_icon_button_props,
                    on_click=rx.redirect('/about-me'),
                ),
                rx.icon_button(
                    'languages',
                    **_header_icon_button_props,
                    on_click=HeaderState.change_language
                )
            ),
            **_header_group_props,
        ),
        **_header_props,
    )
