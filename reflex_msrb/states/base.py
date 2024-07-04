import reflex as rx


class BaseState(rx.State):
    language: int = 0
    language_list: list[str] = ['kor', 'eng']

    def change_language(self):
        self.language += 1
        if len(self.language_list) <= self.language:
            self.language = 0
