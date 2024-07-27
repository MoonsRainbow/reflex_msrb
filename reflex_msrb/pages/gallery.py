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
        'kor_title', 'eng_title',
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
        # ['PF with Bank', 'PF 대출과 재무건전성', '2022.9', '2022.10'],
        # ['Predicting the spread of forest fires', '산불의 확산 규모 예측', '2022.9', '2022.10'],
    ]

    sub_tags: list[list[list[str]]] = [
        ['Python 3.x', 'SQL', 'Maria DB', 'Multi-Processing', 'Selenium', 'Chrome Driver', 'RESTful API'],
        ['Python 3.x', 'SQL', 'Maria DB', 'UI Design', 'Selenium', 'Chrome Driver'],
        ['Python 3.x', 'SQL', 'Maria DB', 'UI Design', 'WinAPI'],
        ['Android', 'Java', 'SQL', 'PHP', 'Tomcat Apache', 'Mysql DB', 'Application'],
        ['Team Lead', 'Policy Design', 'UI/UX Design', 'Structure', 'Axure 9', 'Adobe XD', 'AWS', 'SQL', 'VUE2', 'JavaScript', 'Jira'],
    ]

    projects: list[Project] = []

    def initial(self):
        self.keyword = ''

        if not self.projects:
            for c, s in zip(self.contents, self.sub_tags):
                self.projects.append(
                    Project(
                        kor_title=c[1],
                        eng_title=c[0],
                        start_month=c[2],
                        end_month=c[3],
                        sub_tags=s,
                    )
                )

    def searching(self, text: str):
        self.keyword = text.lower()

        if text != '':
            for project in self.projects:
                if any(self.keyword in attr_name.lower() for attr_name in project.attr_str_names):
                    project.is_show = True
                elif any(self.keyword in sub_tag.lower() for sub_tag in project.sub_tags):
                    project.is_show = True
                elif any(self.keyword in month for month in project.attr_date_names):
                    project.is_show = True
                else:
                    start_year, start_month = [int(s) for s in project.start_month.split('.')]
                    start_day = 1

                    end_year, end_month = [int(s) for s in project.end_month.split('.')]
                    end_day = calendar.monthrange(end_year, end_month)[1]
                    if self.keyword.isdigit():
                        # TODO 범위 안에 있는 월이면 검색 결과에 노출 되도록 수정
                        if len(self.keyword) == 4:
                            if start_year <= int(self.keyword) <= end_year:
                                project.is_show = True
                            else:
                                project.is_show = False
                        elif len(self.keyword) == 5:
                            # TODO month_keyword 가 내부 범위에 속해 있는 지 확인
                            year_keyword = int(self.keyword[:-1])
                            month_keyword = int(self.keyword[-1])
                            # if all([start_year <= year_keyword <= end_year,
                            #         start_month <= month_keyword <= end_month]):
                            #     project.is_show = True
                            # else:
                            #     project.is_show = False
                        elif len(self.keyword) == 6:
                            # TODO month_keyword 가 내부 범위에 속해 있는 지 확인
                            year_keyword = int(self.keyword[:-2])
                            month_keyword = int(self.keyword[-2:])
                            # if all([start_year <= year_keyword <= end_year,
                            #         month_keyword < 13,
                            #         start_month <= month_keyword <= end_month]):
                            #     project.is_show = True
                            # else:
                            #     project.is_show = False
                    else:
                        try:
                            if '-' in self.keyword:
                                date_keyword = datetime.strptime(self.keyword, '%Y-%m-%d')
                            else:
                                date_keyword = datetime.strptime(self.keyword, '%Y.%m.%d')

                            if datetime(start_year, start_month, start_day) <= date_keyword <= datetime(
                                    end_year, end_month, end_day):
                                project.is_show = True
                            else:
                                project.is_show = False
                        except ValueError:
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
            ),
            rx.vstack(
                rx.foreach(
                    GalleryState.projects,
                    lambda project, index: rx.cond(
                        project.is_show,
                        rx.card(
                            rx.text(
                                rx.cond(
                                    GalleryState.language,
                                    project.eng_title,
                                    project.kor_title
                                )
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
