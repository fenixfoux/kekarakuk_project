import flet as ft
from pages.home_page import HomePage
from pages.personages.pers_page import PersPage


def page_route_change_handler(page):
    home_page = HomePage().create_content_page()
    pages = {
        '/': ft.View(
            "/",
            [home_page],
        ),
    }

    if page.route.startswith('/pers_page'):
        person_id = page.route.split('/')[-1]
        pers_page = PersPage(person_id).create_content_page()
        pages[page.route] = ft.View(
            route=page.route,
            controls=[pers_page]
        )

    page.views.clear()
    page.views.append(pages.get(page.route, pages['/']))
    page.update()