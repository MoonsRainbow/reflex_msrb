"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .pages import *
from .states import *
from rxconfig import config


import reflex as rx


app = rx.App(
    theme=rx.theme(
        radius='large'
    )
)
