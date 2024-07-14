"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .pages import *
from .states import *
from rxconfig import config


import reflex as rx


app = rx.App(
    theme=rx.theme(
        appearance='light',
        has_background=True,
        accent_color='gold',
        color_scheme='yellow',
        radius='large',
    )
)
