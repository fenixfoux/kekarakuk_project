import flet as ft

from pages.home_page import HomePage as main_h
from pages.test.test_page import PageTest as p_tests


def page_route_change_handler(page):
    page_home = main_h().main()
    page_tests = p_tests().content_page
    pers_page = p_tests().pers_content_page
    pers_page_2 = p_tests().create_pers_page_content()

    pages = {
        '/': ft.View(
            "/",
            [page_home],
        ),
        '/page_tests': ft.View(
            "page_tests",
            [page_tests],
            scroll=ft.ScrollMode.AUTO
        ),
        '/pers_page': ft.View(
            route='pers_page',
            controls=[pers_page]
        ),
        '/pers_page_2': ft.View(
            route='pers_page_2',
            controls=[pers_page_2]
        )
    }

    page.views.clear()
    page.views.append(
        pages[page.route]
    )
    page.update()
