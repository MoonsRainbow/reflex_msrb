import calendar
from datetime import datetime
from .template import wrap_template
from reflex_msrb.states import BaseState
from reflex_msrb.routes import GALLERY_ROUTE
from reflex_msrb.styles import (
    pages_style
)

import reflex as rx


class Project(rx.Base):
    attr_str_names: list[str] = [
        'kor_title', 'eng_title', 'kor_describe', 'eng_describe'
    ]

    attr_date_names: list[str] = [
        'start_month', 'end_month',
    ]

    attr_list_names: list[str] = [
        'sub_tags'
    ]

    kor_title: str
    eng_title: str
    start_month: str
    end_month: str
    sub_tags: list[str]
    kor_describe: str
    eng_describe: str
    is_show: bool = True


class GalleryState(BaseState):
    page_title: list[str] = ['갤러리', 'Gallery']

    keyword: str = ''

    contents: list[list[str]] = [
        ['Project Saturn', '토성 프로젝트', '2019.1', '2022.2'],
        ['Project Unipass', '유니패스 업무 자동화 프로젝트', '2019.3', '2021.12'],
        ['Project Winsabis', '윈서비스 업무 자동화 프로젝트', '2019.3', '2019.12'],
        ['Project Yarding', '야딩 프로젝트', '2019.6', '2020.6'],
        ['Carbay Korea', '카베이 코리아', '2019.9', '2022.2'],
        ['Unipass Program', '유니패스 프로그램', '2022.5', '2022.11']
        # ['PF with Bank', 'PF 대출과 재무건전성', '2022.9', '2022.10'],
        # ['Predicting the spread of forest fires', '산불의 확산 규모 예측', '2022.9', '2022.10'],
    ]

    sub_tags: list[list[str]] = [
        ['Python 3.x', 'SQL', 'Maria DB', 'Multi-Processing', 'Selenium', 'Chrome Driver', 'RESTful API'],
        ['Python 3.x', 'SQL', 'Maria DB', 'UI Design', 'Selenium', 'Chrome Driver'],
        ['Python 3.x', 'SQL', 'Maria DB', 'UI Design', 'WinAPI'],
        ['Android', 'Java', 'SQL', 'PHP', 'Tomcat Apache', 'Mysql DB', 'Application'],
        ['Team Lead', 'Policy Design', 'UI/UX Design', 'Structure', 'Axure 9', 'Adobe XD', 'AWS', 'SQL', 'VUE2', 'JavaScript', 'Jira'],
        ['Freelancer', 'Python 3.11', 'AWS', 'pyinstaller', 'exe', 'UI/UX Design', 'Adobe XD', 'SQL', 'WinAPI', 'Open API', 'Maria DB']
    ]

    describe: list[list[str]] = [
        ['ENG', 'KOR'],
        ['ENG', 'KOR'],
        ['ENG', 'KOR'],
        ['ENG', 'KOR'],
        ['ENG', 'KOR'],
        ['ENG', 'KOR'],
    ]

    projects: list[Project] = []

    def initial(self):
        self.keyword = ''

        if not self.projects:
            for c, s, d in zip(self.contents, self.sub_tags, self.describe):
                self.projects.append(
                    Project(
                        eng_title=c[0],
                        kor_title=c[1],
                        start_month=c[2],
                        end_month=c[3],
                        sub_tags=s,
                        eng_describe=d[0],
                        kor_describe=d[1],
                    )
                )

    def searching(self, text: str):
        self.keyword = text.lower()

        if text != '':
            for project in self.projects:
                if any(self.keyword in sub_tag.lower() for sub_tag in project.sub_tags):
                    project.is_show = True
                elif any(self.keyword in describe for describe in [project.kor_describe, project.eng_describe]):
                    project.is_show = True
                else:
                    project.is_show = False
        else:
            for project in self.projects:
                project.is_show = True


@rx.page(
    route=GALLERY_ROUTE,
    title=f"{GalleryState.page_title[GalleryState.language]} | MoonsRainbow",
    on_load=[GalleryState.initial]
)
@wrap_template
def gallery() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading(
                rx.cond(
                    GalleryState.language,
                    GalleryState.page_title[1],
                    GalleryState.page_title[0]
                ),
                width='100%',
                size='9',
                text_align='center',
            ),
            rx.input(
                rx.input.slot(
                    rx.icon(
                        'search',
                        size=20,
                    )
                ),
                width='100%',
                variant='soft',
                radius='full',
                size='3',
                on_change=GalleryState.searching,
                placeholder=rx.cond(
                    GalleryState.language,
                    'Please enter the name of the skill stack.',
                    '기술 스택 이름을 입력해주세요.'
                )
            ),
            rx.vstack(
                rx.foreach(
                    GalleryState.projects,
                    lambda project, index: rx.cond(
                        project.is_show,
                        rx.card(
                            rx.vstack(
                                rx.vstack(
                                    rx.hstack(
                                        rx.text.strong(
                                            rx.cond(
                                                GalleryState.language,
                                                project.eng_title,
                                                project.kor_title
                                            ),
                                            font_size=20
                                        ),
                                    ),
                                    rx.text(
                                        '[',
                                        project.start_month,
                                        ' ~ ',
                                        project.end_month,
                                        ']',
                                        font_size=12,
                                    ),
                                    width='100%',
                                    spacing='1'
                                ),
                                rx.flex(
                                    rx.foreach(
                                        project.sub_tags,
                                        lambda tag: rx.badge(
                                            f'#{tag}',
                                        )
                                    ),
                                    spacing='3',
                                ),
                                width='100%',
                                spacing='4',
                            ),
                            width='100%',
                        ),
                        rx.fragment()
                    )
                ),
                width='100%',
                align='center',
                justify='start',
            ),
            width='60%',
            align='center',
            justify='center',
            spacing='6',
        ),
        **pages_style,
    )
