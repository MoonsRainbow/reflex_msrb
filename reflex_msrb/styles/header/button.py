button = {
    'height': '44px',
    'variant': 'ghost',
    'cursor': 'pointer',
}

logo_button = {
    **button,
}

icon_button = {
    **button,
    'width': '44px',
    'color': '#FFF'
}

menu_button = {
    **logo_button,
    'width': '80px',
}

menu_button_highlight_on = {
    **menu_button,
    'color': 'gold',
    'fontWeight': 'bold',
}

menu_button_highlight_off = {
    **menu_button,
    'color': '#AAA',
    'fontWeight': 'normal',
}
